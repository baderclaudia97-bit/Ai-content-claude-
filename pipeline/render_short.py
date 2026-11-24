"""Render an original portrait explainer from timed segments and narration."""
import argparse
import json
import math
import shutil
import subprocess
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

W, H, FPS = 1080, 1920, 30
BG, FG, ACC = (12, 18, 32), (245, 247, 250), (255, 196, 0)

def font(size):
    for path in ("/usr/share/fonts/opentype/inter/Inter-Bold.otf",
                 "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"):
        try:
            return ImageFont.truetype(path, size)
        except OSError:
            pass
    raise RuntimeError("Install Inter or DejaVu Sans before rendering.")

def wrap(draw, text, face, width):
    lines, current = [], ""
    for word in text.split():
        candidate = (current + " " + word).strip()
        if current and draw.textlength(candidate, font=face) > width:
            lines.append(current)
            current = word
        else:
            current = candidate
    return lines + ([current] if current else [])

def validate(segments):
    if not isinstance(segments, list) or not segments:
        raise ValueError("Provide a nonempty list of timed segments.")
    previous_end = 0
    for s in segments:
        if not all(k in s for k in ("k", "t", "start", "end")):
            raise ValueError("Each segment needs k, t, start and end.")
        start, end = s["start"], s["end"]
        if (not isinstance(start, (int, float)) or not isinstance(end, (int, float))
                or not math.isfinite(start) or not math.isfinite(end)
                or start < previous_end or end <= start):
            raise ValueError("Segment times must be finite, ordered and nonoverlapping.")
        if not isinstance(s["t"], str) or not s["t"].strip() or not isinstance(s["k"], str):
            raise ValueError("Segment text must be nonempty; k must be text.")
        previous_end = end

def render(segments, audio, output, cta):
    validate(segments)
    if not shutil.which("ffmpeg"):
        raise RuntimeError("ffmpeg is required.")
    if not Path(audio).is_file():
        raise ValueError("Narration file does not exist.")
    if Path(audio).resolve() == Path(output).resolve():
        raise ValueError("Output cannot overwrite narration.")
    total = segments[-1]["end"] + 0.6
    if total > 180:
        raise ValueError("This portrait renderer supports at most 180 seconds.")
    title_font, body_font, small_font = font(72), font(58), font(38)
    args = ["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo",
            "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
            "-i", str(audio), "-c:v", "libx264", "-preset", "veryfast", "-crf", "20",
            "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "160k",
            "-af", "apad,loudnorm=I=-16:TP=-1.5:LRA=11", "-t", str(total),
            "-movflags", "+faststart", str(output)]
    proc = subprocess.Popen(args, stdin=subprocess.PIPE)
    try:
        for n in range(math.ceil(total * FPS)):
            t = n / FPS
            index = max((i for i, s in enumerate(segments) if s["start"] <= t), default=0)
            s = segments[index]
            im = Image.new("RGB", (W, H), BG)
            d = ImageDraw.Draw(im)
            shift = (t * 20) % 90
            for x in range(-90, W + 90, 90):
                d.line([(x + shift, 0), (x + shift, H)], fill=(24, 33, 51), width=2)
            for y in range(-90, H + 90, 90):
                d.line([(0, y + shift), (W, y + shift)], fill=(24, 33, 51), width=2)
            d.rectangle([0, 0, int(W * t / total), 10], fill=ACC)
            title_lines = wrap(d, s["k"], title_font, 880)
            if len(title_lines) > 4:
                raise ValueError("On-screen keyword is too long; shorten k.")
            d.rounded_rectangle([70, 330, W - 70, 390 + len(title_lines) * 90],
                                radius=28, fill=(26, 36, 58), outline=ACC, width=4)
            for i, line in enumerate(title_lines):
                d.text(((W-d.textlength(line, font=title_font))/2, 360+i*90),
                       line, font=title_font, fill=FG)
            d.text((110, 850), f"{index+1:02d} / {len(segments):02d}",
                   font=small_font, fill=ACC)
            words = s["t"].split()
            fraction = min(0.9999, max(0, (t-s["start"])/(s["end"]-s["start"])))
            word_index = min(len(words)-1, int(fraction * len(words)))
            chunk_start = (word_index // 5) * 5
            caption = " ".join(words[chunk_start:chunk_start+5])
            if s["start"] <= t <= s["end"] + 0.15:
                lines = wrap(d, caption, body_font, 860)
                d.rounded_rectangle([65, 1220, W-65, 1280+len(lines)*76],
                                    radius=20, fill=(0, 0, 0))
                for i, line in enumerate(lines):
                    d.text(((W-d.textlength(line, font=body_font))/2, 1240+i*76),
                           line, font=body_font, fill=FG)
            if index == len(segments)-1 and cta:
                lines = wrap(d, cta, small_font, 860)
                for i, line in enumerate(lines[:2]):
                    d.text(((W-d.textlength(line, font=small_font))/2, 1010+i*52),
                           line, font=small_font, fill=ACC)
            proc.stdin.write(im.tobytes())
    finally:
        proc.stdin.close()
        code = proc.wait()
    if code:
        raise RuntimeError(f"ffmpeg failed with exit code {code}; output is not verified.")
    return total

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("timed_json")
    parser.add_argument("audio")
    parser.add_argument("output")
    parser.add_argument("--cta", default="")
    a = parser.parse_args()
    with open(a.timed_json, encoding="utf-8") as f:
        duration = render(json.load(f), a.audio, a.output, a.cta)
    print(json.dumps({"output": a.output, "duration_seconds": duration}))
