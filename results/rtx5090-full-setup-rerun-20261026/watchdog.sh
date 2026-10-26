#!/bin/bash
# Relaunch the guarded RTX 5090 re-run server while the re-run supervisor is alive.
set -u
cd /mnt/data/Projects/llm-non-coding-benchmark || exit 1
export XDG_RUNTIME_DIR="/run/user/$(id -u)"
UNIT=noncoding-rtx5090-rerun-server-20261026
CONFIG=/mnt/data/Projects/llm-non-coding-benchmark/results/rtx5090-full-setup-rerun-20261026/server.json
LOG=/mnt/data/Projects/llm-non-coding-benchmark/results/rtx5090-full-setup-rerun-20261026/watchdog.log
echo "$(date -u +%FT%TZ) watchdog start" >> "$LOG"
while pgrep -f "run_lane.py --run-dir results/rtx5090-flash-next-full-20261024" >/dev/null; do
  if ! systemctl --user is-active --quiet "$UNIT"; then
    echo "$(date -u +%FT%TZ) server inactive; free=$(nvidia-smi --query-gpu=memory.free --format=csv,noheader,nounits) MiB; relaunching $UNIT" >> "$LOG"
    systemctl --user reset-failed "$UNIT" 2>/dev/null
    systemd-run --user --unit="$UNIT" --collect \
      python3 -u /mnt/data/Projects/llm-non-coding-benchmark/scripts/guard_gpu_reserve.py --minimum-mib 3072 -- \
      /home/akitaonrails/.local/share/strata/terminal/0.1.45.3/python/bin/python3.12 \
      /home/akitaonrails/.local/share/strata/terminal/0.1.45.3/strata.py serve --config "$CONFIG" --offline --shutdown-timeout 1 >> "$LOG" 2>&1
    for i in $(seq 1 120); do
      if curl -s -m 4 -H "Authorization: Bearer local" http://127.0.0.1:18082/v1/models | grep -q flash-next; then
        echo "$(date -u +%FT%TZ) server ready after ${i}0s" >> "$LOG"; break
      fi
      sleep 10
    done
  fi
  sleep 20
done
echo "$(date -u +%FT%TZ) supervisor gone; stopping owned server" >> "$LOG"
systemctl --user stop "$UNIT" 2>/dev/null
