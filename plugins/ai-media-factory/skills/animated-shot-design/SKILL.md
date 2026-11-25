---
name: animated-shot-design
description: Design coherent animated video shots and an edit plan from a verified script. Use for a 10–15 second visual sample, storyboard, generation prompts, scene continuity or a montage plan that needs real staged action rather than text-card animation.
---

# Animated shot design

Plan the visuals and edit without calling generation tools or spending credits. Hand every executable request to the coordinator.

## Build the direction

1. Read the brief, script, brand decisions and current user feedback. Do not treat a rejected format as an approved template.
2. Choose a clear visual premise that demonstrates the story. Prefer a small number of motivated actions over a collage of unrelated effects. Use original descriptions; do not imitate a living artist or protected character.
3. For an initial 10–15 second sample, design two or three shots in a single coherent world. State subject, action, environment, camera, lighting, palette, motion and beginning/end state for each shot.
4. Establish a continuity sheet: character/object identity, wardrobe, material, proportions, light direction, spatial layout and screen direction. Use reference frames only if actually available and permitted.
5. Make the first two seconds understandable on a phone without narration. Use camera motion to reveal or emphasize an action. Do not equate a zoom on a still, a moving background grid or animated typography with the requested staged animation.

## Prepare the production handoff

Create a per-shot table with shot ID, intended duration, action, camera, continuity anchor, narration segment, sound cue and transition. Timing remains a proposal until the rendered source is measured.

Write one concise generation prompt per shot: subject + specific action + environment + camera + light + style/materials + continuity. Specify what must remain stable. Keep text, logos and exact numeric labels for the edit where possible; do not rely on a generator to spell them correctly.

List required settings for the coordinator to verify from the provider's current schema: model availability, supported duration, 9:16 ratio, resolution, reference support, audio and estimate. Mark unverified settings `TO_VERIFY`; do not invent parameter names or provider IDs. If a model cannot follow the design, propose a feasible shot change before generation.

Provide an edit decision list: ordered source shot IDs, source in/out times when known, transition, narration, captions, music/effects, and final target duration. Keep voice intelligible, avoid unlicensed audio and use intentional quiet where useful. Do not add 4K by default.

Deliver:

- `storyboard.md`: the visual premise, continuity sheet and timed shot table.
- `shot-plan.md`: generation prompts, settings to verify, source requirements and edit decision list.
- Actual file references, version and run ID; explicitly label every missing asset and unrendered shot.

Do not report a video, animation or montage as produced because these plans exist. Do not use publication, scheduling, deletion or comment tools.
