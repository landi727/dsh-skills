---
name: audit-wechat-article-compatibility
description: Audit interaction designs, media, source packages, and pre-publication drafts for WeChat Official Account articles. Use when planning or reviewing long-form image articles, HTML copied into the WeChat editor, SVG or GIF effects, native video or audio, links, mini-program entry points, continuous-image joins, or device compatibility. Produce evidence-graded findings, safe fallbacks, and an iOS/Android release test plan; do not use for general visual critique or content-policy review.
---

# Audit WeChat Article Compatibility

## Contract

- **Type:** Capability / technical review.
- **Responsibility:** Determine which proposed article behaviors are safe for the main version, which require proof in the real WeChat route, and which need a fallback before production.
- **Boundary:** Do not redesign the whole article, review copy legality, operate the user's account, publish content, or promise universal compatibility from a local browser render.
- **Input:** Accept a plan, module list, screenshots, HTML/ZIP, asset folder, published URL, WeChat draft preview, or test evidence. Work with partial inputs and identify only the missing facts that change the verdict.
- **Output:** Deliver a verdict, feature matrix, blockers, minimal repairs, fallback map, evidence ledger, and release-test checklist.
- **Failure handling:** Mark unsupported claims and inaccessible artifacts as `证据不足`. Never convert an untested behavior into a compatibility claim.
- **Validation:** A release-ready verdict requires the four gates below. Reasoning or a published precedent alone cannot satisfy the device gate.
- **Stop condition:** Stop after every critical feature is either verified, replaced with a safe fallback, or listed as a precise blocker.
- **Reuse scope:** WeChat Official Account article planning, source inspection, and pre-publication technical review.
- **Maturity:** Level 0 Draft. Structure validation is complete; same-account editor and dual-device production validation remain unverified.

## Select the review mode

Use the narrowest mode that fits the request:

| Mode | Input | Main decision |
| --- | --- | --- |
| `plan-audit` | Storyboard, campaign plan, module specification | Can this be designed for WeChat without depending on fragile behavior? |
| `source-audit` | HTML, ZIP, asset package, or published article | What does the source actually use, and what may be removed or changed on import? |
| `release-audit` | Saved draft, preview, screenshots, recordings, device results | Did the final WeChat route preserve and run the intended result? |

Do not claim a later mode was completed from an earlier-mode artifact.

## Establish the real delivery route

Record these facts before assigning a final compatibility status:

- Account type, verification state, and relevant permissions when links, mini-programs, video, audio, or other account-scoped features are used.
- Production path: direct WeChat editor, third-party editor paste/import, API draft creation, or another stated route.
- Intended clients: at minimum iOS and Android WeChat; add desktop or older devices only when audience or interaction requires them.
- Essential behaviors and optional enhancements.

Ask only for missing facts that change a major verdict. When facts remain unknown, continue with a conservative plan review and label the assumptions.

## Audit workflow

### 1. Inventory every behavior

Create one row per static image, GIF, SVG/CSS effect, native media block, link, mini-program entry, tap area, reveal, animation trigger, or continuous-image join. Give each row a stable module ID.

For HTML or a ZIP, inspect the actual DOM, CSS, asset types, remote URLs, dimensions, and file availability. Asset counts do not prove visible behavior. A missing remote asset makes the package incomplete.

### 2. Separate content from enhancement

Identify what the reader must understand or act on. Put all critical copy, prices, dates, instructions, brand marks, and calls to action in a readable base state.

Apply this invariant:

> When animation, SVG, video, links, or client-specific styling fails, the article still communicates its complete essential meaning.

For image-led production, editable HTML/CSS may remain the production source; the WeChat upload version may bake all text into PNG or GIF frames. Judge the exported upload assets, not the editability of the production source.

### 3. Grade evidence and status

Read [references/evidence-and-status.md](references/evidence-and-status.md) whenever assigning compatibility status. Verify time-sensitive platform facts from current first-party documentation or the current editor when accessible. Record the source and check date.

A published article proves that a technique worked for that article, route, account, and time. Use it as precedent, not as a guarantee for a new draft.

### 4. Review by feature family

Read [references/feature-baseline.md](references/feature-baseline.md) for the relevant feature families. Preserve the intended visual effect where evidence supports it. Reduce or replace only the mechanism that creates the compatibility risk.

Use the saved-and-reopened WeChat draft as the implementation source of truth. Local HTML and third-party editor previews are design evidence only because WeChat may clean markup, rewrite resources, or change layout.

### 5. Design the fallback

For each conditional or fragile behavior, specify:

- What appears before interaction or media playback.
- What remains when the behavior fails.
- The lowest-cost replacement that preserves the communication goal.
- Whether the fallback is already present in the delivered asset.

Prefer static frames or GIFs for decorative motion, visible platform-native links for navigation, and poster-plus-summary treatment for native media. Do not hide critical navigation inside transparent or invisible tap areas.

### 6. Build the release test

Read [references/release-tests.md](references/release-tests.md) for `release-audit` and whenever a plan contains conditional behavior. Produce a manual checklist the user can execute without granting account access.

### 7. Issue the verdict

Use only these verdicts:

- `可发布`: all four gates pass, and every critical behavior has evidence from the real delivery route.
- `可发布，有已知降级`: all critical content survives; only optional enhancement differs, with an accepted fallback.
- `暂缓发布`: a critical behavior lacks same-route proof, fails on a required client, or has no fallback.
- `仅完成策划审查`: implementation or device evidence has not yet been supplied.

Never shorten `仅完成策划审查` to `可发布`.

## Four release gates

1. **Content gate:** Essential meaning and action remain in the base state.
2. **Editor gate:** The final import path survives save, close, and reopen in the WeChat editor.
3. **Device gate:** The saved draft is previewed and tested on required iOS and Android devices, with app and OS versions recorded.
4. **Fallback gate:** Every conditional enhancement has a visible, tested fallback.

The Skill creates release-level assurance through these gates. Platform updates, account permissions, device differences, and network conditions prevent a permanent universal guarantee; re-run the affected gates after any editor route, asset, interaction, or platform change.

## Deliver the report

Use [references/report-template.md](references/report-template.md). Lead with the verdict and blockers. Keep evidence, observation, inference, and recommendation distinct.

When the user asks for a revised plan, edit only the incompatible implementation choices and preserve approved content, visual hierarchy, pacing, and campaign decisions. End with the exact items requiring user-side preview evidence.

Respond in the user's language. Use direct labels and avoid unexplained technical vocabulary.
