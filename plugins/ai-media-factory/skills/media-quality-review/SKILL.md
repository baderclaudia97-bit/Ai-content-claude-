---
name: media-quality-review
description: Independently inspect an actual rendered social video and return timestamped evidence of picture, sound, factual and delivery quality. Use before a sample is shown as approved, before a full video is delivered or before a specific piece is considered for publication.
---

# Independent media quality review

Review the actual final media. Do not generate, repair, spend, schedule, publish or reply to comments. Return defects to the coordinator; do not approve your own revision.

## Require evidence first

Require the playable MP4, episode/run ID, script, storyboard, source table, delivery manifest and the render's SHA256 or equally specific immutable version reference. If the MP4 is missing, inaccessible, unplayable or represented only by a thumbnail, script, URL claim or generation success message, return `BLOCKED` immediately. State the missing artifact and do not award a score.

Inspect the beginning, middle and end at minimum, watch the complete short video, and listen to its audio. Read available media metadata. If the review tools cannot play motion or sound, return `BLOCKED` for that portion; contact sheets alone cannot prove smooth animation or clean audio. Separate checks actually performed from unavailable checks.

## Apply acceptance gates

| Gate | Pass evidence | Failure examples |
| --- | --- | --- |
| Story | The action communicates the stated problem/takeaway | Generic spectacle, misleading outcome or unsupported claim |
| Animation | Subjects perform coherent staged actions through time | Mostly static cards, still-image zooms, unrelated clips |
| Continuity | Identity, layout and motion remain consistent | Morphing faces/hands, disappearing props, direction jumps |
| Edit | Shots connect intentionally; the hook is legible in the first two seconds | Dead opening, unmotivated transitions, clipped ending |
| Voice/sound | All words intelligible; no audible clipping; effects support the action | Music masks speech, broken words, abrupt audio cuts |
| Captions | Accurate words, timing and readable phone layout | Wrong numbers, spelling errors, cut text, UI-obscured text |
| Technical | Measured duration, dimensions, video/audio streams and playback match the brief | Wrong aspect ratio, missing audio, black/frozen frames |
| Evidence | Claims match sources; assets and render version are identifiable | Invented benchmarks, unlicensed assets, mismatched file hash |

Use a proposed safe region for a 1080×1920 master of x=90–900 and y=240–1500 for essential text, then check current platform overlays and actual previews. This is a working layout target, not an official universal platform specification. Require a 9:16 export, normally 1080×1920 with H.264/AAC unless the brief and provider constraints justify another delivery. Do not silently upscale low-resolution media and call it native quality.

For a sample, require 10–15 seconds of actual measured playback and an intentional ending. For a full piece, evaluate its authorized brief rather than forcing the sample duration.

## Report the result

Write `quality-review.md` with run ID, render reference/hash, reviewer role, checks performed, `PASS`, `FAIL` or `BLOCKED`, and each defect's timestamp, severity, observation and required correction. Mark a missing capability explicitly. Any failed gate prevents PASS. Do not average a serious failure away with scores.

Include a concise phone-viewing assessment and the remaining risk. A PASS means the reviewed version passed these checks; it does not establish audience performance, user visual approval, licensing beyond the evidence provided, monetization or permission to publish. Any changed render needs review again against its new hash.
