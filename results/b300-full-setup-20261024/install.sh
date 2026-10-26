#!/bin/bash
set -euo pipefail
uv venv /workspace/noncoding-venv --python python3.12
uv pip install --python /workspace/noncoding-venv/bin/python 'vllm==0.32.0' 'nvidia-cuda-nvcc==13.0.88' 'nvidia-cuda-crt==13.0.88' 'nvidia-nvvm==13.0.88'
/workspace/noncoding-venv/bin/python -c 'import vllm; print(vllm.__version__)'
