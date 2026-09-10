---
name: analyze-image-for-generation
description: Analyze reference illustrations into source-specific reconstruction blueprints or transferable drawing and visual-organization rules. Use for same-style subject replacement, generation prompts, and reference-to-output checks. Rank the defining mechanisms for each reference, keep source content separate from style, and preserve reference images as generation anchors. Analysis alone does not generate images or establish generation fidelity.
---

# Analyze Image for Generation

## Responsibility and boundary

**Type:** Capability. **Reuse scope:** illustration reconstruction and style-transfer workflows.

Convert visible reference evidence into a blueprint for a later image-generation task. Identify what most determines this image's visual identity and express it as drawing actions, relationships, supported variation, and observable acceptance criteria.

Analyze visible construction before applying style labels. A single image supports the style visible in that image; it does not establish an entire artist/brand style or universal transfer. Do not infer attribution, exact authoring history, or hidden decoration. Photography, UI design, editable-template production, and 3D production are outside the main scope.

## Input contract and task modes

Inspect the highest-fidelity available reference at full-frame scale. Record the requested deliverable, exactness, target content, frozen requirements, palette direction, source limitations, and actual authorization for generation or comparison. For multiple references, identify each source's role and conflicts without averaging them.

- **reconstruction:** preserve the source's identity, composition, proportions, occlusion, and appearance. Default to this mode only when purpose is unspecified; state the assumption. Pixel equality requires an original-pixel workflow and a dedicated comparison. Never promise an identical generative redraw or silently substitute copying for requested generation.
- **style_transfer:** derive reusable drawing and organization rules for new subjects. Keep source identities, poses, text, counts, and coordinates separate. Apply rules only to supplied targets; otherwise provide a separate target-content input.
- **both:** share source evidence once, then produce independently labeled blueprints, prompts, and criteria.

**Failure handling:** ask for missing references when source evidence is indispensable. Mark ambiguous geometry or cross-category extensions as unresolved/hypothetical. Resolve routine choices from evidence and user intent. Ask only about conflicting explicit requirements or missing evidence that blocks the requested fidelity.

**Stop condition:** stop at the requested analysis, blueprint, prompt, JSON, or comparison. Generate or edit images only when the user requests that action. Preserve actual reference images as anchors in image-capable generation; never invent attachment status. Identify text-only delivery as such.

## Reference routing

Read these shared references completely for every source analysis:

- `references/global-visual-conclusion.md` for the initial whole-image scan.
- `references/illustration-type-routing.md` for type selection.
- `references/generation-blueprint-schema.md` for output depth and the **single authoritative priority and prompt-compilation policy**.
- `references/evidence-audit.md` for verification proportional to claims.
- `references/generation-validation.md` for acceptance criteria and validation status.

After the initial scan, read the selected subtype references and the dimensions that materially affect this task. For a full blueprint, read all applicable dimension references. Loading order and report field order never establish perceptual priority.

| Evidence or task | Reference |
| --- | --- |
| Focal hierarchy, visual weight, motifs, grouping or story devices | `references/visual-organization.md` |
| Silhouette, shape grammar, volume, light, material or object-detail behavior | `references/object-modeling.md` |
| Color roles, large color masses, adjacency or palette mapping | `references/color-relationships.md` |
| Line, edge, fill, brushwork or texture | `references/line-color-texture.md` |
| Density rhythm, quiet fields, clustering or competing target content | `references/density-rhythm.md` |
| Decisive overlap, windows, clipping, interlocks or visibility | `references/layering-hidden-shapes.md` |
| Reconstruction geometry or decisive projection/direction | `references/camera-geometry-orientation.md` |
| Style transfer or both modes | `references/style-transfer.md` |

Subtype references: `references/subtype-flat-graphic.md`, `references/subtype-painterly.md`, `references/subtype-collage-print.md`, `references/subtype-character-narrative.md`, `references/subtype-technical-information.md`. Load only those selected by routing.

For requested JSON, read `references/task-blueprint.schema.json` and every schema referenced by the selected mode: `references/generation-blueprint.schema.json`, `references/layering-system.schema.json`, `references/object-modeling.schema.json`, and `references/color-relationship.schema.json`. Preserve their field contracts; they do not prescribe prose length or prompt order.

## Workflow

### 1. Classify and establish the whole-image conclusion

Select one primary illustration type and up to two supporting types from visible construction. Record classification confidence and conflicts internally; disclose only material limitations by default.

Scan the whole image for large shapes and proportions, focal order, large color/value masses, shape abstraction, edge/line/mark behavior, modeling, density rhythm, visual layering, and narrative action. Treat these as candidate mechanisms, without a permanent hierarchy. Use the selected subtype to refine the scan.

Select the few mechanisms whose loss would most change the requested identity, usually 3–5 without a quota. Describe the visible consequence of each and rank them. A character's gesture or a painterly edge can outrank quiet space or spatial layering. A dense reference can require abundant marks and little quiet area. Verify the provisional ranking after the detailed audit.

### 2. Analyze the decisive systems

Keep visual layering, object modeling, color relationships, density rhythm, and visual organization distinct in analysis. Inspect all at the scan level; expand only what changes the blueprint or establishes an important exception. A simple system can be recorded in one sentence. Unsupported nonessential fields remain internal or are omitted from prose.

- **Geometry and shape:** establish a screen-relative view, silhouette, main/secondary masses, deformation, projection, and recognition cues. In reconstruction, register the primary and major objects' position, bounds, width/height spans, visible silhouette occupancy, frame contact, and measurement status. Keep bounding-box area distinct from visible area and inferred full shape. Use one anchor or the canvas for ratios. In style transfer, measure only relations that support drawing rules; derive new anatomy and proportions from the target.
- **Direction:** for decisive elongated objects, separate endpoint roles, screen path, depth trajectory, visible faces, and content direction. Preserve mixed projections; do not force a physical camera or unsupported angles.
- **Visual organization:** identify first-read order, dominant mass and counterweights, motif cadence, semantic groups, and graphic narrative devices. For character scenes, establish focal action, gaze, expression, and causal relations.
- **Layering:** separate projected placement, spatial order, production order, and perceptual order. Record only supported bands and decisive local relations, contour ownership, masks, protected identity cues, and visible exposure. Keep interlocks local. Exact production history from a flattened image remains unresolved. Infer only the minimum necessary hidden geometry.
- **Object modeling:** preserve recognition strategy and shape grammar along with modeling mode, value structure, light, material cues, line-based volume, and detail progression. Record required behavior and upper bounds where relevant. Do not let object/material nouns introduce unsupported shading or microdetail. Also protect decisive brushwork, value masses, and complexity against under-modeling.
- **Color:** record functional roles, large-area allocation, hue distances, warm/cool relationships, value order, saturation, and adjacency. Preserve the source's supported blending or lost boundaries as well as its separation. Grayscale is diagnostic; hue-based separation may disappear there.
- **Line, fill, texture:** distinguish silhouettes, external frames, and internal lines; inspect edges, fill opacity, contour adherence, mark scale/direction, and local exceptions. Texture gets space proportional to its actual importance.
- **Density:** distinguish canvas activity from object-internal detail. Identify quiet/dense topology, peak separation, activity drivers, and clean subject masses when present. Do not require empty space or sparse modeling from a source that lacks them.

### 3. Map the target and resolve capacity

Separate user-required items, candidates, and incidental suggestions from their labels and story role. “Available,” “optional,” and “environment cues” are candidate pools unless the user requires all items. Identity-bearing and causally essential details remain required even when they are small.

For style transfer, separate fixed drawing rules, supported variables, source-specific choices, and provisional extensions. Preserve source hue families by default when no recoloring is requested; state this as a task default, not proof that those hues define every work in the style. Exact source layout and counts remain source-specific unless explicitly frozen or supported as defining organization rules.

When several target elements compete for space, assign included details to semantic groups and bounded clusters or permitted interruptions. Check the resulting visual activity, including contrast, text, texture, and overlaps. All candidates may be retained when their roles and combined load fit; deletion is not a success criterion.

Resolve actual overflow by removing incidental content, selecting candidates, merging related cues, or reusing an existing panel. Preserve required recognition and story content. Ask only when conflicting required items remain impossible to accommodate. Do not solve overflow by shrinking everything or filling protected quiet fields.

Use estimated ranges or qualitative bounds when measurements are uncertain. State tolerances for numerical acceptance criteria. An approximate source percentage is not automatically a hard target threshold; see `references/generation-validation.md`.

### 4. Rank and compile

Apply the priority and compilation policy in `references/generation-blueprint-schema.md`. Keep explicit user requirements separate from source-derived style priorities. Rank hard mechanisms internally as well as across hard/medium/soft tiers; give a reason and a visible failure sign. Preserve uncertainty independently of importance.

Compile only the requested deliverable. State how the target should be drawn positively, then add a small number of concrete drift exclusions. Place decisive mechanisms early, regardless of dimension. Keep controls near the content they govern. Do not front-load a universal inventory of density, lighting, or layering limits, and do not repeat the full analysis in the execution prompt.

### 5. Audit, accept, and stop

Verify important claims against separated source regions and a likely counterexample; use fresh crops and alternate views only where they resolve a concrete claim. Inspect every generated diagnostic before citing it. Reconcile local findings with the full frame, then correct the ranking and report.

Check mode separation, source-content leakage, actual reference use, required identity/action, candidate allocation when applicable, palette instructions, and consistency between top priorities, prompt, and acceptance. Report source-analysis confidence separately from inspected generation results. Without generated results, set generation validation to `not_run`.

When generation and revision are authorized, inspect the defining mechanisms first. Change the largest deviation through only 1–2 relevant variables while preserving successful parts. Default to at most two corrective attempts unless the user sets another budget; report remaining deviations. Passing selected cases supports only that tested scope.

## Output contract

Lead with the ranked visual conclusion and the requested deliverable. Follow the compact/full/JSON output modes in `references/generation-blueprint-schema.md`.

Default to a short ranked mechanism list, useful fixed/variable distinctions, relevant target decisions, and acceptance/status. In a full blueprint, expose distinct system blocks ordered by reference-specific priority, with simple systems kept brief. Show detailed object cards only when useful for reconstruction or requested control. Keep audit ledgers, source sampling, and repeated evidence internal.

Analysis rigor, report length, prompt order, and model execution are separate properties. Textual priority expresses requested importance; it does not guarantee a model's internal weighting or generation outcome.
