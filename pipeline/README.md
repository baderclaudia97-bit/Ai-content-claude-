# Portrait explainer prototype

Produces H.264/AAC 1080x1920 video from original narration and timed segments. This is a production component, not a publisher or autonomous social media manager.

Run `bash pipeline/setup.sh` in an isolated environment with Python 3.11–3.13, ffmpeg, and Inter or DejaVu Sans. Activate `.venv`. Confirm model licenses and download availability before use. No paid API is used. The generic synthetic voice is a prototype; editorial approval is still needed before public use.

Input: a nonempty JSON list of `{"k":"Short heading","t":"Original narration."}`. Generate narration with `python pipeline/tts.py segments.json am_michael voice.wav --timed-output timed.json`. Render with `python pipeline/render_short.py timed.json voice.wav out.mp4 --cta "Useful next action"`.

Only English narration is configured. Do not route Swedish or Arabic through an English voice. Caption timings are approximate per segment, not forced audio alignment; review the output. Each production needs original storytelling and appropriate visual variation. The same generic visual template alone does not establish monetization eligibility.

Validate actual output with ffprobe and inspect playback, audio, framing, subtitles, rights, factual claims and platform metadata. Store account mappings, queue, approvals, metrics and costs in the owner's private project store. Never commit credentials or user analytics.

Test evidence: renderer smoke-tested at full portrait resolution with a local test WAV; TTS/model installation must be verified in each target environment. The native Claude scheduled task is managed separately and must read its persistent state, deduplicate existing drafts and record actual results.
