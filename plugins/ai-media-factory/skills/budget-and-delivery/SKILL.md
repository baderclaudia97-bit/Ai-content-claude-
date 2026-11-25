---
name: budget-and-delivery
description: Gate media generation and delivery using verified subscription costs, provider balances, per-action estimates, artifact evidence and specific user approvals. Use before generating video or audio, retrying a paid action, creating publication records or reporting monthly budget compliance.
---

# Budget and delivery control

Apply this procedure as coordinator. Specialists can identify missing data but must not execute spending or distribution.

## Budget gate

Use a configurable monthly project ceiling; the default planning target is **2,000 SEK per calendar month in Europe/Stockholm**. This target is not an established current spend or a provider-enforced cap. Read the user's current private ceiling and allocation if present.

Before any video/audio/image generation or other credit-consuming action:

1. Verify the intended provider account, current plan, available included credits, reset date and whether the exact action could incur any incremental charge. Use a current account response; a connector label is not sufficient. Do not change payment or overage settings. An action quoted entirely within included credits with a verified safety margin does not require changing an existing overage setting.
2. Verify all recurring subscriptions allocated to the project's total ceiling, including Claude and the production/distribution tools in use. Record monthly amounts, currency, tax treatment and source date. Do not inspect unrelated billing or mail. If a required fee is unknown, report `BLOCKED_BUDGET_TOTAL`; do not assert remaining monthly capacity, compliance with the ceiling or an affordable recurring production cadence. The single-sample exception below may still apply.
3. Obtain the exact action estimate from the provider's estimate function or current authoritative pricing for the available model, duration, resolution, ratio, quantity and audio. Record credits and any incremental monetary charge separately. A guess or a different model's quote is not an estimate for this action.
4. Calculate total committed monthly cost: allocated recurring fees + completed metered charges + pending/reserved authorized charges. Convert currencies using a verified current exchange rate with an explicit tax/FX margin. Do not count included credits as a second cash charge; still record their depletion.
5. Reserve the estimated cost of every authorized attempt before submitting it. For ordinary or recurring production, require both enough included balance and verified headroom below the total ceiling. Unknown account, balance, action cost or incremental charge blocks every generation. An unknown subscription total blocks ordinary production, subject only to the explicit single-sample exception below. Continue scripts, storyboards and access diagnosis without spending when blocked.
6. Never buy credits, subscribe, upgrade, enable overage or authorize a new payment. If needed, return one concrete request stating provider, amount/credits, purpose and estimated monthly consequence. Wait for the user's decision.

On submission, save provider job ID and estimate. On completion or failure, reconcile actual charged credits/cost and release unused reservations. Check whether a failed generation was charged before considering another attempt. Retry only within the user's existing allowance and recorded attempt limit; never create an unbounded quality loop.

### Narrow exception: one authorized sample

An explicit user instruction to produce one visual sample is sufficient authorization for that sample; do not add another approval merely because this workflow has a gate. When allocated subscription fees are still unknown, permit only that single 10–15 second sample if all of the following are evidenced before submission:

- The intended account and current included-credit balance are verified.
- The provider gives an exact quote for the selected model, duration, settings and number of attempts, with **zero incremental monetary charge**.
- After existing reservations and the complete quoted sample cost, the current included balance retains an explicit safety margin of at least the greater of 10% of the pre-action included balance or the cost of one additional quoted attempt. Record the calculation; if the provider cannot verify included-credit treatment, block.
- The sample's total credit allowance and maximum attempts are explicitly authorized. Do not broaden a sample authorization into a full video, retries beyond that limit, recurring production or publication.

Keep `BLOCKED_BUDGET_TOTAL` on the monthly plan while performing this exception. Record the sample as included-credit use, its quote, reservation, actual deduction and zero verified additional charge. Do not claim the 2,000 SEK total has been checked. Never buy credits, enable overage, change payments or rely on an unknown charge to complete the sample.

## Asset and approval gate

Save every real deliverable to the authorized private project location. Record filename, ID/URL, byte size, duration/dimensions when relevant, SHA256/version, creation timestamp, and whether it is a master or compressed backup. Distinguish attached media from a provider job, draft or public post. If storage fails, preserve the existing master and report the component failure; do not regenerate an asset to solve an upload limit.

Require explicit user approval of the specific 10–15 second visual sample before full-video generation. Require independent review tied to the exact final render before delivery/publication. Require specific publication authorization identifying the asset and destinations; style approval alone is insufficient. Preserve current editorial holds.

Before distribution, inspect the project manifest and destination records for the same episode, version and file hash. If a matching post/draft exists or a previous request's result is uncertain, reconcile its status first. Do not repost to fix uncertainty. A draft must retain `draft=true` and `autoPublish=false` where those parameters exist; use only fields exposed by the actual connector.

After an authorized publication, read back provider status and platform post ID/public URL. Record `PUBLISHED_VERIFIED` only when supported by provider/platform evidence. A scheduled time, tool acceptance or stored instructions is not proof of publication. Do not delete or alter existing live posts without authorization.

## Platform packaging and account evidence

Create a distinct package per authorized destination. Read back the actual account/channel ID and handle through the connected service and associate it with the episode's draft/post ID. Never infer the destination account from a display name, a previous session or a connector being listed. Do not add new channels or languages without a brief.

For YouTube, deliver a specific truthful title, a thumbnail/cover concept that matches the piece, a strong opening, a concise description and a logical series/playlist proposal. Keep the visual sample gate intact; do not create extra assets or uploads just to fill these fields. Distinguish Shorts packaging from a long-form episode. Review measured retention and completion when available; record date range, video ID and metric definition, and do not invent missing analytics. Before publication, check current official altered/synthetic-content disclosure rules against the actual piece and record the labeling decision and reason. Do not assume every animation requires the same disclosure or that adding a label grants monetization eligibility.

For Instagram, TikTok and Facebook, adapt the opening frame, short truthful caption, aspect ratio/crop, cover and relevant hashtags to each destination. Avoid repeated keyword/hashtag blocks, unrelated trending tags, misleading hooks and identical boilerplate across accounts. Verify the current upload fields, platform overlays, duration/resolution limits and applicable AI labeling requirements with the connector and official platform guidance before posting; do not invent fields or universal limits. Check the actual draft preview where available.

For each platform, include the exact account ID/handle, destination type, episode/version/hash, proposed title/caption/cover, labeling decision, and actual saved draft ID/URL. A proposal is not a saved draft. A saved draft is not a public post. Record eligibility or revenue only when verified from that specific account; views, follower counts and an active account do not prove monetization eligibility or earnings.

## Comments and measurement

Verify platform-specific read capability before claiming monitoring coverage. Reading analytics is not reading comments. Limit this workflow to verified read access and a private queue of proposed responses; do not send replies from a routine merely because a post performs well. If a platform lacks a verified reader, record `BLOCKED_COMMENT_ACCESS` for that account and state the exact missing component. Do not infer zero comments from an empty analytics response.

Read only comments on project posts and keep platform/post/comment IDs, timestamps and moderation status in private project storage. Prioritize real questions and support needs; flag abuse or sensitive matters for the user. Avoid spam, repetitive replies, engagement bait and unsupported claims. Sending any response requires separate applicable user authorization, a verified reply tool and duplicate/status checks. Do not fetch unrelated direct messages or mail.

Maintain private `cost-ledger` and `delivery-manifest.json`. Report actual verified totals separately from unknown costs, included credit use and proposed spending. Never infer profit from views or promise revenue.
