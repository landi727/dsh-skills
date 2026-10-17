# Tool Profiles

Route by capability rather than memorized version numbers. If a tool's current official documentation conflicts with this reference, follow the documentation.

## Contents

1. General language models
2. Reasoning-native models
3. Coding assistants
4. Agentic coding tools
5. Research and search tools
6. Browser and computer-use agents
7. Image tools
8. Video tools
9. Audio and voice tools
10. 3D tools
11. Workflow automation

## 1. General Language Models

Examples include chat models and API text-generation models operating without a dedicated reasoning mode.

- State the task, relevant context, output contract, and constraints.
- Use headings or delimiters only when they clarify long or mixed inputs.
- Add a role only when domain perspective changes the answer.
- Add examples only for demonstrated formatting or decision-boundary failures.
- Keep instructions independent of provider-specific syntax unless the user names an API feature.

## 2. Reasoning-Native Models

Use this profile when the selected mode performs internal reasoning or exposes a reasoning-effort control.

- Give a concise goal, constraints, evidence requirements, and definition of done.
- Do not request chain-of-thought, scratch work, simulated deliberation, or "internal reasoning"; native reasoning is implicit.
- Try zero-shot first.
- Use native reasoning controls outside the prompt when the tool provides them.
- Ask for calculations or a concise justification only when the visible result needs them.

## 3. Coding Assistants

Use for inline completion or chat assistants that suggest code without autonomous execution.

- Include the language, version, file or function, current behavior, desired behavior, and edge cases.
- State interfaces and tests that must remain compatible.
- Identify protected files or APIs when relevant.
- Request the smallest change that satisfies the acceptance criteria.

## 4. Agentic Coding Tools

Examples include coding agents that inspect repositories, edit files, run commands, or open browsers.

- Describe the starting state and final deliverable.
- Bound the editable paths and protected areas.
- Define allowed tools and whether dependency changes are permitted.
- Require relevant tests or runtime verification.
- Add approval gates before deletion, external writes, schema changes, deployments, or credential use.
- Define when the agent should stop and report a blocker.

## 5. Research and Search Tools

- Specify the research question, geography, time range, and decision the research supports.
- Distinguish discovery, verification, comparison, and synthesis.
- Require primary or authoritative sources when accuracy matters.
- Require claim-level citations and publication or event dates for changing information.
- Tell the tool how to handle missing, conflicting, or uncertain evidence.

## 6. Browser and Computer-Use Agents

- Describe the outcome and constraints instead of fragile click-by-click navigation.
- State whether the task is read-only or may change external state.
- Require confirmation before submitting forms, sending messages, purchasing, publishing, deleting, or accepting legal terms.
- Provide account, budget, date, and selection constraints without embedding credentials.
- Define success evidence, such as a saved draft, confirmation page, or screenshot.

## 7. Image Tools

For generation:

- Describe subject, action, environment, composition, viewpoint, lighting, color, material, and intended use.
- Separate exact required content from stylistic preferences.
- Put literal text in quotation marks and specify placement when text is required.
- Use native aspect ratio, seed, reference-strength, or negative-prompt controls outside the prose prompt when available.

For editing:

- Identify the reference image.
- Describe only the requested changes.
- State the elements, identity, composition, or geometry that must remain unchanged.
- Define output size, crop, and transparency requirements when relevant.

## 8. Video Tools

- Define subject, action, location, duration, shot size, camera movement, pacing, lighting, and visual continuity.
- Describe the temporal sequence when more than one event occurs.
- Separate dialogue, ambient sound, and music requirements when the tool supports audio.
- Avoid mutually incompatible camera or motion directions.

## 9. Audio and Voice Tools

- Supply the exact script separately from delivery instructions.
- Define language, pronunciation, speaker character, emotion, pace, pauses, and emphasis.
- Use native voice, stability, seed, or timing controls when available.
- For music, define structure, instrumentation, tempo, mood, and vocal requirements.

## 10. 3D Tools

- Define subject, style, proportions, pose, materials, topology needs, texture resolution, and intended downstream use.
- State whether the asset needs rigging, animation readiness, watertight geometry, separate parts, or a specific export format.
- Use native geometry and texture settings outside the prose prompt when available.

## 11. Workflow Automation

- Define the trigger, conditions, ordered actions, field mappings, authentication assumptions, error handling, retries, and idempotency.
- Identify data that must never be logged or sent to another service.
- Specify test data and a dry-run path before enabling live execution.
- Define the expected final state for each success and failure branch.

## Routing Examples

- ChatGPT, Claude, Gemini, Qwen, or a local chat model: general language model; switch to reasoning-native when that mode is active.
- Copilot-style inline completion: coding assistant.
- Codex, Claude Code, Cursor Agent, Cline, Devin, or similar: agentic coding tool.
- Perplexity-style evidence gathering: research and search tool.
- Browser automation or computer control: browser and computer-use agent.
- Midjourney, Stable Diffusion, or image-generation APIs: image tool.
- Sora, Runway, Kling, or similar: video tool.
- Voice synthesis or music generation: audio and voice tool.
- Text-to-3D or in-engine asset generation: 3D tool.
- Zapier, Make, n8n, or similar: workflow automation.
