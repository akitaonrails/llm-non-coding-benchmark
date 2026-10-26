#!/bin/bash
# Keep the guarded RTX 5090 benchmark server alive while its lane is unfinished.
# Same configuration and same reserve guard as the original launch; it never
# touches desktop processes and stops as soon as the lane writes its summary.
set -u
cd /mnt/data/Projects/llm-non-coding-benchmark || exit 1
export XDG_RUNTIME_DIR="/run/user/$(id -u)"
UNIT=noncoding-rtx5090-full-server-20261024-r2
CONFIG=/mnt/data/Projects/llm-non-coding-benchmark/results/rtx5090-full-setup-20261024-r2/server.json
LANE=results/rtx5090-flash-next-full-20261024
LOG=/tmp/opencode/lanes/watchdog-5090.log

echo "$(date -u +%FT%TZ) watchdog start" >> "$LOG"
while [ ! -f "$LANE/lane-summary.json" ]; do
  if ! systemctl --user is-active --quiet "$UNIT"; then
    echo "$(date -u +%FT%TZ) server inactive; relaunching $UNIT" >> "$LOG"
    systemctl --user reset-failed "$UNIT" 2>/dev/null
    systemd-run --user --unit="$UNIT" --collect \
      python3 -u /mnt/data/Projects/llm-non-coding-benchmark/scripts/guard_gpu_reserve.py --minimum-mib 3072 -- \
      /home/akitaonrails/.local/share/strata/terminal/0.1.45.3/python/bin/python3.12 \
      /home/akitaonrails/.local/share/strata/terminal/0.1.45.3/strata.py serve --config "$CONFIG" --offline --shutdown-timeout 1 >> "$LOG" 2>&1
    for i in $(seq 1 120); do
      if curl -s -m 4 -H "Authorization: Bearer local" http://127.0.0.1:18082/v1/models | grep -q flash-next; then
        echo "$(date -u +%FT%TZ) server ready after ${i}0s" >> "$LOG"
        break
      fi
      sleep 10
    done
  fi
  sleep 30
done
echo "$(date -u +%FT%TZ) lane finished; stopping owned server" >> "$LOG"
systemctl --user stop "$UNIT" 2>/dev/null
