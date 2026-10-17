# Generation Acceptance and Validation

## Separate three kinds of confidence

1. **Source analysis**: claims verified against source regions; use evidence-audit.md.
2. **Prompt/specification**: rules are coherent, prioritized, mode-appropriate, and traceable to evidence.
3. **Generated output**: actual output inspected against acceptance criteria.

Never substitute one for another. Record source-audit and generation-validation status separately. For analysis/prompt-only requests, define criteria and leave generation status `not_run`; finish without producing test images. A supplied generated output permits comparison within the user's review request. New generation requires authorization and an available image tool.

## Reconstruction acceptance

Check at matched canvas aspect and display scale, with full-frame and decisive detail comparisons:

- content identity/count, silhouette, projected proportions, placement and crop;
- direction, visible faces, spatial bands, decisive local occlusions, overlap types, contour ownership, masks/clipping, visibility profiles, hidden-shape limits, and meaningful negative space;
- quiet-field continuity and area, density-peak count, cluster separation, transition direction, breathing gaps, and primary-subject cleanliness;
- first-read order, viewing path, dominant visual weight, counterweights, motif cadence, narrative-device function, and semantic-group clarity;
- recognition strategy, shape grammar, mass hierarchy, modeling mode, value-plane count/span/contrast, lighting ceiling, material response, line-based volume, object-detail density, protected clean masses, and object-tier progression;
- color-role area distribution, hue-distance structure, temperature allocation, value ladder, saturation budget, adjacency/separation behavior, contour/fill behavior, light, detail and texture mechanisms;
- exact text or frozen brand elements when specified.

Rank deviations by explicit frozen constraints and reference-specific priorities. Use measurements for meaningful geometry/color claims; mark estimates. Do not treat prompt coordinates as achieved coordinates. Keep composition and style findings separate so good placement cannot conceal a changed drawing style.

For literal pixel equality, require original and candidate with matching dimensions/channels and compare decoded pixel values deterministically; file-byte differences alone do not prove visible differences, and perceptual similarity does not prove pixel equality. Do not claim this check ran without performing it. A generative redraw may fail strict equality even when visually close; report that result without silently lowering the target.

## Style-transfer acceptance

Check the target's intended identity separately from the style match. Compare defining mechanisms, simplification/deformation, visual-layering grammar, object modeling, line/fill, color relationships, focal hierarchy, visual weight, motif grammar, narrative devices, semantic grouping, canvas-density rhythm, and spatial grammar. Apply acceptance criteria only from the selected subtype modules. Source object count or pose is not an acceptance requirement unless explicitly frozen.

For visual layering, follow `layering-hidden-shapes.md`. Compare layer-role families, spatial-band order, decisive local front/rear relations, supported overlap types, contour termination and redraw, masks or clipping, visibility priorities, protected identity cues, and production-stage conventions. Treat a reversed relation, lost window or cutout, flattened stack, over-covered identity cue, unsupported hidden detail, or invented exact authoring history as a layer-system failure. Revise the target layer map before changing color or object modeling.

For object modeling, follow `object-modeling.md`. Inspect representative primary, supporting, background, nested-scene, and special-material objects at normal size, thumbnail, grayscale, and mild blur. Check shape grammar, mass hierarchy, modeling mode, value-plane count and area, value span, adjacent contrast, edge behavior, gradient policy, highlight/shadow footprint, cast shadows, ambient occlusion, specular/reflection behavior, transparency treatment, line-based depth, clean-area share, and detail progression across tiers.

Treat unsupported glossy highlights, rounded gradients, reflections, refraction, glow, ambient occlusion, perspective subdivisions, turning lines, panel seams, material microtexture, and uniformly complete secondary-object modeling as over-modeling failures. Treat missing decisive value masses, edge transitions, shadows, or material cues as under-modeling failures when the source depends on them. Revise the specific modeling axis or object-tier rule before changing unrelated composition or color rules.

For canvas density and organization, compare protected quiet fields, density peaks, cluster separation, first-read order, viewing path, balance, motif cadence, device function, group clarity, and clean areas inside the primary subject at full-frame, thumbnail, and mildly blurred views. Diagnose whether lost clean area comes from added scene content or added object-internal modeling.

For color, first verify that the selected palette mode matches the user's instruction. Then inspect full-frame color roles and area shares, thumbnail mass separation, grayscale value order, warm/cool/neutral partition, and an adjacency or flat-color map. Check hue-distance categories, temperature counterweights, value steps, saturation concentration, required outlines or neutral buffers, and bounded accent area.

Treat color adhesion as a critical failure when large neighboring roles use nearby hues, the same temperature role, and similar value/saturation without an effective separator. Also fail the color system when the counter-color survives only as fragmented small accents and no longer balances the dominant field. Revise role assignment, value band, temperature counterweight, or adjacency separation before changing unrelated drawing rules.

Treat broadly uniform activity as a critical density-rhythm failure when the reference depends on distinct quiet and dense zones, even when content and palette match. Also fail the gate when a protected quiet zone loses continuity or falls below its stated floor, cluster/text maxima are exceeded, an unallocated candidate appears independently, primary clean masses are subdivided below their floor, or breathing gaps collapse. Content completeness never compensates for these failures; omission of a candidate item is acceptable when required by the capacity budget. Identify the largest spillover region and revise element count, contrast, scale, or placement there before changing unrelated rules.

For an authorized reusable-prompt test, use a small task-relevant set with meaningfully different structure (for example, one organic and one constructed subject). Prefer supplied targets and results. Keep the reusable style block unchanged across subjects and report any target-specific additions. A rule changed after a failure must be rechecked on earlier cases before claiming all cases pass. Record the actual model/tool, reference-image use, style-block version, targets, and inspected outputs. Passing selected cases supports only that tested scope, not all subjects or models. Text-only and reference-assisted runs establish different evidence.

## Results and revision

Report `pass`, `partial`, `fail`, or `not_run`, with concrete findings, unresolved limits, and tested scope. Avoid uncalibrated similarity percentages. A `pass` requires all declared critical criteria in the inspected result, and never implies universal transfer or pixel equality without its dedicated check. Do not describe a generated task as complete when a critical density, layering, modeling, color, identity, or exact-content gate failed; show or identify the candidate and state the failed gate.

When revision is authorized, identify the largest deviation and change only the relevant 1–2 variables while preserving successful parts and the original reference. For density failure, first remove leaked candidate content, restore the largest protected quiet field, or reduce one overflowing cluster; do not rewrite the palette or subject. For over-modeling, lower the exact lighting, value, material, line-volume, or detail-density rule and state the new ceiling. For color adhesion, revise a specific role relation rather than adding a broad mood label. Respect the user's iteration/time budget; default to at most two corrective attempts per task, then report remaining deviations. Do not retry by adding unrelated adjectives or changing the task's acceptance target.
