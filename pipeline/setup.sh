#!/usr/bin/env bash
set -euo pipefail
command -v ffmpeg >/dev/null || { echo "Install ffmpeg first." >&2; exit 1; }
python3 -m venv .venv
. .venv/bin/activate
python -m pip install 'kokoro-onnx==0.4.9' 'soundfile>=0.13,<1' 'Pillow>=11,<14' 'numpy>=2,<3'
model_dir="${KOKORO_DIR:-models}"
mkdir -p "$model_dir"
base=https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0
for filename in kokoro-v1.0.onnx voices-v1.0.bin; do
  if [ ! -f "$model_dir/$filename" ]; then
    curl --fail --location --output "$model_dir/$filename.partial" "$base/$filename"
    mv "$model_dir/$filename.partial" "$model_dir/$filename"
  fi
done
