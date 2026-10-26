#!/bin/bash
# Re-run, one at a time, the four GLM cases whose first attempts were contaminated
# by controller errors. Sequential on purpose: one case at a time against the pod.
set -u
cd /mnt/data/Projects/llm-non-coding-benchmark || exit 1
RUN=results/b300-glm53-flash-full-20261024
LOG=/tmp/opencode/lanes/rerun-glm-clean.log
: > "$LOG"
for CASE in brlaw_10_cobranca_prescrita usacc_01_schedule_c usacc_06_sale_asset_vs_stock uslaw_09_retaliation_termination; do
  echo "=== $(date -u +%FT%TZ) $CASE ===" >> "$LOG"
  python3 scripts/rerun_case.py \
    --run-dir "$RUN" \
    --case "$CASE" \
    --reason "controller-fault clean re-run after a recorded over-release of scripted facts" \
    --endpoint http://127.0.0.1:18081 \
    --ssh-host b300-noncoding \
    --model glm-5.3-flash \
    --hardware "RunPod 1xB300 SXM6; GLM 5.3 Flash NVFP4; vLLM 0.32.0" >> "$LOG" 2>&1
  echo "=== $(date -u +%FT%TZ) $CASE rc=$? ===" >> "$LOG"
done
echo "ALL DONE $(date -u +%FT%TZ)" >> "$LOG"
