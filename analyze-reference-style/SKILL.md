---
name: analyze-reference-style
description: 已停用。禁止启动、禁止使用。本技能无适用任务；不得自动匹配、显式调用或由其他技能与 Agent 间接启动。仅用户明确要求重新启用后方可恢复。
---

# Analyze Reference Style（已停用）

## 停用状态

本技能已按用户要求停用。禁止自动匹配、显式调用及由其他技能或 Agent 间接启动；收到调用请求时保持停用，仅用户明确要求重新启用后方可恢复。

以下工作流程与附属资源保留用于恢复和维护，不得在停用期间执行。

## Mission

Produce a faithful visual analysis of the supplied image. Explain what is visible, how the visual system works, and which mechanisms most strongly determine the style. Treat the first analysis as provisional until every testable detail claim has passed the screenshot audit.

Treat this as image analysis, not prompt engineering. Keep the global style system separate from the depicted objects and scene content.

## Required references

Read these files before analyzing:

- `references/analysis-dimensions.md` — use for the full dimensional analysis.
- `references/evidence-language.md` — use for evidence, inference, tone, and anti-overreach rules.
- `references/object-scene-analysis.md` — additionally use whenever the image contains recognizable objects, figures, environments, or layered scene content.
- `references/detail-screenshot-audit.md` — always use after drafting; follow it to create and inspect claim-level crops, correct errors, and run the final whole-image review.

## Core operating rule

Use **fixed dimensional coverage with image-dependent depth**:

- Examine every required dimension.
- Do not force equal length across dimensions.
- Expand the dimensions that visibly carry the image's style.
- Briefly report dimensions with little evidence instead of inventing content.
- Describe a visual phenomenon once, in the dimension where it is most explanatory.

Completeness means covering the visual system, not accumulating terminology.

## Workflow

### 1. Establish the task and evidence

- Confirm that the image is available and visually inspect it at full-frame scale.
- Determine whether the task concerns one image, shared traits across several images, or a comparison.
- Locate the highest-fidelity available source. Do not audit a chat thumbnail when the original file is available.
- Use measurements or color sampling only when they clarify an important claim. Do not measure by default.
- Do not browse for artists, movements, periods, or production methods unless the user explicitly requests attribution or external research.

### 2. Form the overall visual judgment

Describe, in grounded language:

- what kind of visual system the image uses;
- its first-order organization and visual hierarchy;
- its broad relationship among composition, form, color, space, and detail;
- the provisional factors that appear most decisive to its style.

Do not begin with an art-movement, decade, artist, or medium label. Description must precede naming.

### 3. Analyze every visual dimension

Follow `references/analysis-dimensions.md`.

For each dimension, use this reasoning sequence:

1. **Visible condition** — state what can actually be seen.
2. **Operating principle** — explain how those visible choices work together.
3. **Stylistic effect** — explain what they contribute to the image's visual character.
4. **Boundary** — mark anything that cannot be determined from the image alone.

Avoid checklist prose. Synthesize related observations into a coherent explanation.

### 4. Isolate the decisive style mechanisms

After the dimensional analysis, identify the 3–5 mechanisms that most strongly determine the image's style.

For each mechanism:

- cite concrete visual evidence;
- identify which dimensions it connects;
- explain why it matters more than secondary features;
- state what would materially change if it were removed.

Do not output a list of fashionable style keywords.

### 5. Analyze objects and scene content separately

When recognizable content is present, follow `references/object-scene-analysis.md`.

Describe:

- what each important object or group is;
- where it appears;
- its scale, silhouette, color, internal detail, cropping, overlap, and layer;
- how that object manifests the already-described visual system.

Do not mix object inventory into the global style definition. Do not let a style label replace concrete object description.

### 6. Run the mandatory detail screenshot audit

Follow `references/detail-screenshot-audit.md` after completing the provisional analysis.

1. Split the draft into atomic, visually testable claims.
2. Build a claim ledger covering counts, identity, position, boundary contact, shape, orientation, color/value, line behavior, overlaps, layer order, perspective cues, light/shadow, texture, repeated motifs, and any object-level detail mentioned in the draft.
3. Create a fresh crop for every local claim. Use the source image, include enough surrounding context to test the relationship, and do not reuse a thumbnail or mentally rely on the first inspection.
4. When the image is available as a local raster file, prefer `scripts/make_audit_crops.py` to generate non-destructive evidence crops. View every generated crop at original detail.
5. Mark each claim `verified`, `corrected`, or `unresolved`. Rewrite every corrected claim and qualify or remove every unresolved claim.
6. Reopen the full image and read it once more from top to bottom and bottom to top. Recheck global composition, counts, rhythm, color hierarchy, and whether local crops were misread out of context.

Do not skip the audit because the image appears simple. Do not claim verification if a crop was generated but not visually inspected. Keep crops and the ledger internal unless the user asks to see the audit trail.

### 7. Write the final report

Match the user's language and requested depth. Unless the user asks for another structure, use:

1. **Overall visual judgment**
2. **Decisive style mechanisms**
3. **Dimensional analysis**, with a distinct named subsection for every dimension in `references/analysis-dimensions.md`
4. **Object and scene analysis**
5. **Layering, overlap, and spatial relationships**
6. **Facts, interpretations, and unresolved uncertainties**
7. **Integrated style summary**

Do not merge several dimensions into a single subsection merely to shorten the report. Sections may differ substantially in length, but each dimension must remain explicit and independently readable. Combine dimensions only when the user specifically requests a condensed response.

The integrated summary must remain an analytical conclusion, not an image-generation prompt.

Before sending, confirm that the report reflects the corrected post-audit state rather than the provisional draft.

## Comparison mode

When comparing a reference with another image:

- analyze the reference's visual system first;
- compare the second image against the same dimensions;
- audit each image independently before auditing cross-image correspondences;
- distinguish content mismatch from style-system mismatch;
- rank differences by perceptual impact;
- do not infer that a prompt or workflow caused a difference unless evidence is available.

## Scope boundary

Do not generate an image, rewrite the analysis as a prompt, or prescribe a production workflow under this skill alone. If the user later requests one of those tasks, treat it as a separate downstream operation and preserve the analytical report as the source of truth.
