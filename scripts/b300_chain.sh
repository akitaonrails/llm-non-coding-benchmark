#!/bin/bash
# One-shot chain: re-run the controller-faulted B300 case, then hand the pod to
# GLM 5.3 Flash. Kept in a file so the command line is stable and auditable.
set -u
cd /mnt/data/Projects/llm-non-coding-benchmark || exit 1

python3 scripts/rerun_case.py \
  --run-dir results/b300-flash-next-full-20261024 \
  --case bracc_03_cbs_ibs_ano_teste \
  --reason "controller released the ponto_fixo fact (different supplier) against the ATLAS regime question" \
  --endpoint http://127.0.0.1:18081 --ssh-host b300-noncoding --model qwen3.8-flash-next \
  --hardware "RunPod 1xB300 SXM6; Qwen3.8 Flash-Next NVFP4; vLLM 0.32.0" \
  --wait-for-summary > /tmp/opencode/lanes/rerun-b300-cbs.log 2>&1
echo "rerun finished rc=$? at $(date -u +%FT%TZ)" >> /tmp/opencode/lanes/rerun-b300-cbs.log

python3 scripts/b300_sequence.py \
  --wait-lane results/b300-flash-next-full-20261024 \
  --model glm-5.3-flash \
  --run-dir results/b300-glm53-flash-full-20261024 \
  --preflight-dir results/preflight-b300-glm53-flash-full-20261024 \
  --hardware "RunPod 1xB300 SXM6; GLM 5.3 Flash NVFP4; vLLM 0.32.0" \
  --stop-after > /tmp/opencode/lanes/sequence-b300.log 2>&1
echo "sequence finished rc=$? at $(date -u +%FT%TZ)" >> /tmp/opencode/lanes/sequence-b300.log
