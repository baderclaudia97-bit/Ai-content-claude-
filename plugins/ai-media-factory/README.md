# AI Media Factory plugin

This package defines a production coordinator and four specialist agents for evidence-led animated social videos. It contains generic instructions only. It is **source code for a Claude plugin, not evidence of installation, an active team, a scheduled run, generated media or publication**. It adds no executable scripts, hooks, MCP servers, subscriptions or credentials.

## Components

| Component | Purpose | Main deliverable |
| --- | --- | --- |
| `production-coordinator` skill | Delegate work and control every generation/distribution action | Private delivery manifest |
| `research-writer` agent + `evidence-led-script` skill | Verify claims and write the narration | `script.md` |
| `creative-director` agent + `animated-shot-design` skill | Define action, staging, continuity and camera | `storyboard.md` |
| `animation-editor` agent + `animated-shot-design` skill | Prepare exact shot prompts and edit decisions | `shot-plan.md` |
| `quality-controller` agent + `media-quality-review` skill | Independently inspect the actual rendered video | `quality-review.md` |
| `budget-and-delivery` skill | Gate spending, approvals, archiving and publication evidence | Private cost ledger and artifact records |

Specialists plan and review; only the coordinator may execute an authorized generation or distribution action. These are instruction-level boundaries. This package does not technically restrict inherited connector tools. Inspect actual tool permissions and test the deployment before relying on separation of duties.

The monthly planning target defaults to 2,000 SEK and is configurable in the private project brief. Verify recurring fees before claiming monthly compliance or enabling recurring production. Unknown account, action cost, included-credit balance or incremental charge blocks generation. A single explicitly authorized 10–15 second sample may proceed while fixed fees remain unknown only with an exact provider quote, verified included-credit balance and safety margin, zero incremental monetary charge, and an authorized credit/attempt limit. Keep `BLOCKED_BUDGET_TOTAL` on the monthly plan; the exception does not prove the monthly ceiling. Do not buy credits, upgrade, enable overage, change payment settings or create a new payment. No workflow guarantees audience growth or income.

## Runtime and installation

- In legacy ordinary Claude.ai chat, plugin skills load, but plugin agents are ignored. The unified Claude experience and Cowork on the web can run tasks with account-installed plugins; the actual session type and a successful delegation test determine whether agents are available, not the visible word "chat" alone.
- In Cowork and Claude Code, installed plugin agents can load. Verify this in the actual account/runtime.
- Files in a GitHub repository do not install a plugin in a Claude account. Claude Code project files under `.claude/agents/` and `.claude/skills/` have a different loading scope.
- Account-installed plugins can be available to cloud Cowork and scheduled tasks. A CLI-only install does not install the plugin in the account.

For a manual package, zip this folder so `.claude-plugin/plugin.json` is at the archive root or inside its single top-level folder. In Claude, use **Customize → Plugins → Add → Upload plugin**. Install on the intended account, then start a new Cowork task. A marketplace in the existing repository is an optional distribution method, not required to use this package.

Run `/ai-media-factory:production-coordinator` where supported, or ask Claude to apply the production-coordinator skill and delegate to this plugin's named agents. The skills preloaded by agents use their plugin-qualified names. Confirm all four agents and their skills resolve in the deployed runtime; syntax validation alone cannot prove that.

Use existing authorized remote connectors for research, media, project storage and distribution. This package does not configure or authenticate them. Do not add duplicate servers or embed tokens in a public repository. Store runtime briefs, billing evidence, comments, renders and manifests in the authorized private project storage.

## Validate before claiming activation

1. Parse `plugin.json` and every Markdown frontmatter. Check unique names and all agent skill references. If Claude Code is available, run `claude plugin validate <this-folder>`; record its actual output.
2. Install the plugin in the intended account. In Cowork, ask which four named specialist agents are available. Confirm the skills actually preload; a name in this README is not runtime evidence.
3. Run a planning-only smoke task using a generic brief. Request research and direction in parallel, then an edit handoff. Require separate agent results and saved artifact references. Do not generate or publish for this test.
4. Ask the quality reviewer to evaluate a missing media file. It must return `BLOCKED`, identifying the missing playable MP4. Test an unknown price/balance case: the coordinator must block generation and continue planning.
5. Record the real test session URL, component names loaded, artifact references and result privately. Until this passes, report the package as prepared, not active or tested.
6. Reuse the project's existing scheduled task only after installation and testing. Do not create a second production routine. Preserve editorial holds and unrelated tasks.

## Production acceptance

Begin with a 10–15 second sample containing actual staged animation, coherent scenes, deliberate editing and clean sound. Text cards are not an adequate substitute. Verify the playable file, dimensions, duration, source evidence and SHA256, then obtain an independent review. Missing media or unavailable motion/audio inspection blocks approval.

Show the specific sample for explicit user approval before generating a full piece. Independently review the exact final file again. Approval of a style is not authorization to publish every later piece. Keep publication under the current user's specific authorization, reconcile existing drafts/posts first and record returned IDs and read-back status. Never call scheduled instructions or an accepted job a proved publication.

## Official references

Checked 2026-11-25; confirm current platform behavior during deployment.

- [Plugin structure, ZIP installation and testing](https://claude.com/docs/plugins/build)
- [Component support by app and installation scope](https://claude.com/docs/plugins/platform-support)
- [Use plugins in Claude](https://support.claude.com/en/articles/13837440-use-plugins-in-claude)
- [Plugin components and agent frontmatter](https://code.claude.com/docs/en/plugins/components)
- [Subagents and skill preloading](https://code.claude.com/docs/en/sub-agents)
- [Skills in Cowork and cloud sessions](https://code.claude.com/docs/en/skills#use-skills-in-cowork-and-cloud-sessions)
- [Scheduled tasks in Cowork](https://support.claude.com/en/articles/13854387-schedule-recurring-tasks-in-claude-cowork)

The package intentionally omits a `CLAUDE.md` at its root: plugin loading does not treat that file as project context. The coordinator skill carries the workflow instead.
