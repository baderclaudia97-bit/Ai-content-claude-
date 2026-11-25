---
name: production-coordinator
description: Coordinate a small specialist team for an original animated social video, a production review or a daily media-factory run. Use to delegate research, visual direction, edit planning and independent review while controlling every generation, cost and publication decision.
---

# Production coordinator

Act as the sole operator for generation and distribution. Keep specialists focused on decisions and verifiable deliverables. A role description is an instruction, not proof of technical tool isolation.

## Establish the run

1. Read the current private project brief, editorial decisions and delivery manifest. Resolve the audience, language, purpose, visual direction and requested action from that evidence. Ask only for a missing decision that blocks useful work.
2. Distinguish a supervision run, planning run, sample generation and approved publication. Do only the authorized action. Reuse the existing schedule; never create another routine merely to run this workflow.
3. Verify the relevant account and connector state without reading mail or unrelated project data. Record an access failure by component and observed error; do not infer access from a listed connector.
4. Load `ai-media-factory:budget-and-delivery` before any generation, scheduling or publication. Unknown account, balance or action cost blocks generation. An unverified monthly total blocks monthly budget compliance and recurring production; apply only the skill's narrow exception for one explicitly authorized sample using verified included credits with zero incremental charge. Continue useful work without spending when a gate fails.
5. Use the current private brief to choose deliverable filenames and storage. Keep this public plugin free of accounts, credentials, billing records, audience comments and unpublished assets.

## Delegate bounded work

Run independent planning work in parallel when the runtime supports it. Give every specialist the relevant brief and source files; do not assume they inherit conversation history.

| Agent | Assignment | Required handoff |
| --- | --- | --- |
| `ai-media-factory:research-writer` | Verify the story and write the spoken script | `script.md` with claim/source table and exact spoken words |
| `ai-media-factory:creative-director` | Turn the story into staged animated action | `storyboard.md` with timed shots, continuity and sound |
| `ai-media-factory:animation-editor` | Convert the approved direction into executable generation and edit instructions | `shot-plan.md` with prompts, settings to verify and edit timeline |
| `ai-media-factory:quality-controller` | Inspect the actual render independently | `quality-review.md` tied to the exact file/hash, with PASS, FAIL or BLOCKED |

If named agents or their skills are unavailable, report that exact limitation. A single model following role headings is not a proved multi-agent execution. Do not claim installation or delegation without runtime evidence.

Specialists must not call generation, purchase, scheduling, publication or comment-reply tools. Perform any authorized generation yourself after the budget gate. Request revision from the responsible specialist rather than silently approving your own changes.

## Produce a sample before a full piece

1. Select one coherent visual direction and prepare a 10–15 second animated sample with staged action, camera choices, scene continuity and deliberate sound. Text overlays support the action; moving text cards are not sufficient animation.
2. Obtain a provider estimate for exact duration, ratio, resolution, model, number of attempts and any audio. Verify it against the budget skill and the user's current authorization. Never start generation from an unpriced prompt.
3. Generate only the authorized sample. Allow at most the authorized number of attempts; do not retry blindly after errors or quality failures.
4. Save the actual playable MP4 and its manifest. Send the file to `quality-controller`; require a timestamped review of picture and sound, not a review of the storyboard.
5. Deliver the sample and review for user approval. A technical PASS is not the user's visual approval. Wait for explicit approval of the specific sample before generating a full video. Any current user restriction against spending remains binding.
6. For a full piece, repeat the evidence, budget and independent review gates. Approval of a style is not approval to publish every future piece. Publish only the specific asset and destinations authorized by the user.

## Close with evidence

Maintain private `delivery-manifest.json` with `run_id`, `mode`, `status`, `episode_id`, timestamp/timezone, specialist handoff references, claims/sources, generation estimate and actual usage, render reference and SHA256, quality-review reference, approval evidence, and platform draft/post IDs when applicable. Use null plus a reason for missing evidence; never invent IDs.

Use explicit states: `PLANNED`, `BLOCKED_ACCESS`, `BLOCKED_BUDGET`, `SAMPLE_READY`, `REVIEW_FAILED`, `AWAITING_USER_APPROVAL`, `FULL_VIDEO_READY`, `DRAFT_SAVED`, `PUBLISHED_VERIFIED`. Advance only when the corresponding evidence exists. An instruction, API acceptance or scheduled timestamp is not a successful production or public post.

End each run with what was completed, the strongest available file/ID/URL evidence, and the next exact blocker. Do not promise monetization or gains. Do not modify unrelated tasks, repost existing content or remove live posts.
