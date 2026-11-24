"""Generate generic synthetic English narration; no cloning and no API keys."""
import argparse
import json
import os
from pathlib import Path
import numpy as np
import soundfile as sf
from kokoro_onnx import Kokoro

if __name__ == "__main__":
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("segments_json")
    p.add_argument("voice")
    p.add_argument("audio")
    p.add_argument("--timed-output", required=True)
    a = p.parse_args()
    paths = [Path(a.segments_json).resolve(), Path(a.audio).resolve(), Path(a.timed_output).resolve()]
    if len(set(paths)) != 3:
        p.error("Input, audio output and timed output must be distinct files.")
    segments = json.loads(paths[0].read_text(encoding="utf-8"))
    if not isinstance(segments, list) or not segments:
        p.error("Provide a nonempty list of segments.")
    model_dir = Path(os.environ.get("KOKORO_DIR", "models"))
    model = Kokoro(str(model_dir/"kokoro-v1.0.onnx"), str(model_dir/"voices-v1.0.bin"))
    arrays, elapsed, expected_sr = [], 0.0, None
    for s in segments:
        if not isinstance(s.get("t"), str) or not s["t"].strip() or not isinstance(s.get("k"), str):
            p.error("Each segment needs text t and keyword k.")
        samples, sr = model.create(s["t"], voice=a.voice, speed=1.0, lang="en-us")
        if expected_sr is not None and sr != expected_sr:
            raise RuntimeError("The narration model returned inconsistent sample rates.")
        expected_sr = sr
        s["start"], s["end"] = elapsed, elapsed + len(samples)/sr
        elapsed = s["end"] + 0.28
        arrays.extend([samples.astype(np.float32), np.zeros(round(0.28*sr), dtype=np.float32)])
    sf.write(str(paths[1]), np.concatenate(arrays), expected_sr)
    paths[2].write_text(json.dumps(segments, ensure_ascii=False, indent=2), encoding="utf-8")
