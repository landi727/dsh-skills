---
name: analyze-image-for-generation
description: Classify reference-illustration types and analyze them into either a source-specific reconstruction blueprint or reusable style rules for new subjects. Use for faithful illustration reconstruction, extracting transferable visual-layering, object-modeling, drawing, color-relationship, density-rhythm, content-capacity, and visual-organization rules, same-style subject replacement, generation prompts, and reference-to-output checks. Separate content from style; control spatial order, local occlusion, visibility, production order, volume, lighting, material, line-based depth, detail density, quiet-space allocation, and supporting-element capacity explicitly; load only relevant subtype modules; prioritize defining mechanisms; and report evidence and generation-test limits. Analysis alone does not generate images or guarantee exact reproduction.
---

# Analyze Image for Generation

## Mission

Convert supplied reference images into an evidence-backed blueprint that can control a later image-generation task. Describe visible construction precisely before using style labels. Separate observed projection from inferred depth, and separate global visual rules from object-specific content.

## Task modes and limits

- **reconstruction**: Preserve this image's subject identity, composition, proportions, occlusion, and appearance for high-fidelity reconstruction. Treat pixel-identical reproduction as a separate exactness requirement: retain/copy original pixels when requested and authorized; never promise that a generative redraw will be identical. Do not silently replace a requested redraw with a file copy.
- **style_transfer**: Extract reusable drawing and visual-organization rules for different subjects. Keep source-specific content separate from the reusable prompt. Apply rules to new subjects only when targets are supplied; otherwise deliver a reusable style specification with a separate target-content input.
- **both**: Analyze shared visual evidence once, then deliver two independently labeled blueprints/prompts and validation criteria. Do not combine their incompatible constraints into one prompt.

Select the mode from the user's purpose, independently of output format (analysis, prompt, JSON, generation). A request to reproduce this image selects reconstruction; a request to change subjects while keeping the style selects style_transfer. When unspecified, state reconstruction as the default. Ask only when ambiguity would materially change the result.

## Illustration type routing

Classify the illustration after selecting the task mode. Task mode answers what the user wants; illustration type answers which visual mechanisms require specialized analysis.

- Assign one primary type: `flat_graphic`, `painterly`, `collage_print`, `character_narrative`, `technical_information`, or `mixed`.
- Assign up to two supporting types only when they materially change the blueprint.
- Use `mixed` only when two or more construction systems are comparably decisive; list those systems as supporting types.
- Base classification on visible construction, not subject nouns. A character image may be primarily flat graphic with character narrative as a supporting type.
- Record evidence, confidence, conflicts, and the modules actually loaded.
- Follow `references/illustration-type-routing.md` and load only the subtype references it selects.

Treat one image as evidence of the style visible in that image, not proof of a complete artist/brand style or transfer to every possible subject. Mark unsupported extensions as hypotheses. Preserve supplied references as visual anchors in downstream image-capable generation when authorized and available. Text-only prompts are supported, with their untested fidelity stated explicitly; never invent a reference attachment or promise universal transfer.

Keep the internal audit rigorous and the user-facing report concise. Do not expose crop-by-crop reasoning unless the user asks for evidence.

Do not generate or edit an image unless the user separately requests that downstream action. When the user asks for a prompt, compile it only after completing the blueprint.

## Required references

Read these shared files completely before analysis:

- `references/global-visual-conclusion.md`
- `references/layering-hidden-shapes.md`
- `references/object-modeling.md`
- `references/line-color-texture.md`
- `references/color-relationships.md`
- `references/density-rhythm.md`
- `references/illustration-type-routing.md`
- `references/visual-organization.md`
- `references/generation-blueprint-schema.md`
- `references/evidence-audit.md`

After routing, read only the selected subtype references:

- `references/subtype-flat-graphic.md`
- `references/subtype-painterly.md`
- `references/subtype-collage-print.md`
- `references/subtype-character-narrative.md`
- `references/subtype-technical-information.md`

For reconstruction, also read `references/camera-geometry-orientation.md`. For style_transfer, read `references/style-transfer.md`; load the detailed camera reference only when geometry is decisive or the user requests it. For both, read both sets. Read `references/generation-validation.md` when defining acceptance criteria or comparing an actual generated result. Defining criteria is required; generating test images requires a generation request.

Use `references/task-blueprint.schema.json` for machine-readable JSON or a formal schema. It wraps the retained `references/generation-blueprint.schema.json` reconstruction format and the separate style-transfer format; both use `references/layering-system.schema.json`, `references/object-modeling.schema.json`, and `references/color-relationship.schema.json` for the executable layer, modeling, and color systems. Read the task schema and every schema it references for the requested mode. The nested reconstruction `verification` field concerns source analysis only.

Every reconstruction or style-transfer blueprint must expose separate blocks for visual layering, object modeling, color relationships, density rhythm, and visual organization. Never fold visual layering into generic space or composition. Emit a labeled `Visual-layering system` block before `Object-modeling system` with these fields: spatial-order status; layer roles; local relations and overlap types; visibility profiles and protections; production-order evidence and recoverability; fixed rules; variables; target mapping; failure signs; acceptance checks. Use `unresolved` or empty evidence-linked lists when the source lacks support; do not omit or compress this block into a single bullet.

## Core rules

1. Establish a consistent screen-relative view before describing directions. Preserve mixed projections when visible; do not force a physically consistent camera onto graphic illustration.
2. In reconstruction, define the geometry of important objects before materials and decoration. In style_transfer, inspect representative geometry to derive drawing rules.
3. Analyze visual layering as an independent system after geometry and before surface treatment. Separate projected placement, spatial order, production order, and perceptual order. Use a global partial stack, region-specific occlusion relations, visibility profiles, and conservative hidden-shape inference. In style transfer, preserve role-based layer grammar and visibility priorities without copying the source's literal stack.
4. Use one anchor object or the canvas for relative measurements. Do not build long ratio chains.
5. In reconstruction, report the primary subject's and every major object's frame occupancy and placement. In style_transfer, measure only relations that support reusable rules; do not turn source coordinates into target constraints. Distinguish visible silhouette area from bounding-box area and inferred full shape.
6. When reconstructing or inspecting a decisive directional relationship, describe elongated objects through endpoint roles:
   - connection or start endpoint;
   - outer or end endpoint;
   - each endpoint's screen position;
   - each endpoint's near, far, equal, or uncertain depth role;
   - projected path and visible perspective result.
7. Treat screen projection, depth trajectory, face orientation, and content direction as different properties.
8. Separate flatness from vector precision, and abstraction from volume modeling.
9. Analyze lines as three systems:
   - subject or silhouette contours;
   - external frames and borders;
   - internal structural and decorative lines.
10. Never promote a line, fill, detail, texture, or density observation from one region into a global claim.
11. Analyze density rhythm independently from object count and detail hierarchy. Map quiet, transition, and dense zones; record their extent, continuity, separation, and density drivers. A flat colored area may be visually quiet even when it belongs to a large object.
12. Expand texture or any other dimension in proportion to its stylistic importance. Distinguish texture scale, density, direction, contrast, and placement behavior from the incidental positions of individual marks.
13. Mark hidden geometry as inferred, not observed. Never invent hidden text, texture, damage, or hardware.
14. Use exact qualifiers such as global, dominant, local, mixed, and unresolved. Avoid vague labels standing in for visible mechanisms.
15. Analyze focal hierarchy, visual weight, motif grammar, graphic narrative devices, and semantic grouping as independent systems. Convert each decisive system into a transferable rule, generation constraint, failure sign, and acceptance check.
16. Apply subtype rules only when visible evidence supports the classification. Do not load every subtype checklist into one prompt.
17. Treat color as a role-and-relationship system, not a mood label or swatch list. Record hue distance, temperature allocation, value ladder, and adjacency policy. When the user gives no color instruction, use `preserve_source`; recolor only from an explicit request.
18. Treat object modeling as an independent system with explicit upper and lower bounds. Record shape grammar, modeling mode, value structure, lighting ceiling, material response, line-based volume, object-detail density, object-tier rules, and scoped exceptions. Do not let material or object nouns authorize unsupported volume, gloss, reflection, perspective lines, or microdetail.
19. Do not derive front/back order from size, screen height, focal importance, or semantic importance. Record exact production history as unresolved when only a flattened image is available.
20. Always output the visual-layering system even when it is simple, mostly flat, or unresolved. Keep it separate from spatial construction, focal hierarchy, and density rhythm.
21. Treat density as a capacity constraint, not an adjective. Before a target prompt is compiled, classify requested content as required, candidate, or incidental; assign every included secondary element to a bounded cluster or an explicitly permitted quiet-zone interruption; and omit unassigned content. User fields labeled “optional,” “available,” “possible,” or “environment cues” form a candidate pool unless the user explicitly requires every item.
22. Put a compact execution contract before material-rich target nouns in a generation prompt. State protected quiet-space share or qualitative minimum, cluster and text-module limits, primary-subject clean-area floor, modeling mode, value-plane ceiling, gradient/highlight/shadow policy, and overflow behavior first. Repeating these rules later does not replace front-loading them.

## Workflow

### 1. Establish source and task

- Inspect the highest-fidelity available source at full-frame scale.
- Determine whether the user wants analysis only, a generation blueprint, a prompt, JSON, or eventual image generation.
- Record task mode, desired exactness, supplied target content, frozen requirements, palette mode, explicitly frozen colors, and whether generation or comparison has actually been authorized. Parse target content into required items, candidate items, and incidental suggestions from the user's labels and wording; preserve ambiguity when the labels conflict. Analysis/prompt requests stop at their deliverable.
- For multiple references, identify the primary source and each reference's role; keep conflicts and local variants explicit rather than averaging them.
- Record image format, frame orientation, crop, and important source limitations.
- Do not browse for attribution unless the user requests it.

### 2. Classify the illustration

- Follow `references/illustration-type-routing.md`.
- Select the primary and supporting types from visible construction.
- Load the matching subtype references completely.
- Record classification confidence and unresolved conflicts before deriving style rules.

### 3. Form the global visual conclusion

Follow `references/global-visual-conclusion.md`.

Conclude, without narrating the evidence-gathering process:

- graphical modeling and representation degree;
- visual layering, occlusion grammar, visibility priorities, and production-stack evidence;
- object-modeling system and intensity limits;
- color construction and color-role relationships;
- fill mechanism;
- shape and deformation;
- volume and light;
- detail distribution;
- density rhythm and negative-space structure;
- focal hierarchy, visual weight, motif grammar, narrative devices, and semantic grouping;
- spatial construction.

Do not write generic labels such as “hand-drawn collage,” “vector style,” or “retro” without unpacking the visible construction.

### 4. Establish frame and camera

In style_transfer, describe the projection convention and its allowable variation; use detailed camera recovery only when relevant. Steps 5–6 and 9 contain source-specific reconstruction procedures. In style_transfer, inspect enough source objects to ground the layer grammar in Step 7 and the transferable rules in Step 9b without producing a complete source-coordinate registry.

For detailed geometry analysis, follow `references/camera-geometry-orientation.md`.

Describe the visible camera result in ordinary language:

- fixed view;
- dominant visible faces;
- eye-level, high, or low view;
- frontal, three-quarter, side, or flattened presentation;
- perspective strength;
- framing and crop.

Do not force numeric angles when the image does not support them. For flat or contradictory illustrations, state that no unique physical camera can be recovered.

### 5. Build the composition skeleton

- Follow `references/density-rhythm.md` for density and negative-space analysis.
- Follow `references/visual-organization.md` for focal hierarchy, visual weight, motif grammar, narrative devices, and semantic grouping.
- Select a primary anchor object when one exists.
- Identify the primary subject and all major objects before registering supporting objects. The anchor and primary subject may be different.
- Identify global axes, center of gravity, frame contacts, and the topology of quiet, transition, and dense zones.
- For each meaningful density zone, record its canvas region or bounds, approximate area share when supportable, density level, dominant drivers, boundary character, and measurement status.
- Record the largest continuous quiet field, interruptions within it, breathing gaps between clusters, dense-cluster count, and whether the primary subject keeps clean interior areas.
- When a target is supplied, create a content-capacity gate before prompt compilation: name each supported cluster, its element or module allowance, its text allowance, the target elements assigned to it, and the protected gaps around it. Record quiet-zone minimums and primary-subject clean-area floors numerically when the reference supports an estimate; otherwise use bounded qualitative constraints and mark them unresolved or estimated.
- Resolve overflow in this order: remove incidental content, select from candidate pools, merge related cues into one symbol or inset, reuse an existing panel, then ask about conflicting required items only when no evidence-supported allocation can contain them. Never solve overflow by shrinking every item or distributing it across quiet zones.
- Distinguish low object count from low visual activity: edges, contrast, text, texture, overlap, and small marks can make a sparsely populated zone visually dense.
- Record the entry point, primary and secondary focal points, saliency drivers, viewing path, balance axis, counterweights, and edge tension.
- Record motif families, repetition cadence, size progression, spacing, orientation, and controlled mutation.
- Assign every important object, label, and symbol to a semantic group; record the graphic device that presents or connects each group.
- Register all important objects before adding surface details.
- For the primary subject and every major object, always report:
  - projected center in normalized canvas coordinates or an unambiguous verbal region;
  - axis-aligned projected bounding box, or its left, top, right, and bottom limits;
  - width and height spans as fractions or percentages of the canvas;
  - bounding-box area as a fraction or percentage of the canvas;
  - visible silhouette area as a fraction or percentage of the canvas;
  - edge margins, frame crossings, and whether the value is measured, estimated, or unresolved.
- Keep visible silhouette occupancy, bounding-box occupancy, and inferred unoccluded occupancy separate. Do not substitute one for another.
- Measure projected position, length, thickness, area, and spacing only when useful.
- Use rotated geometry for tilted objects rather than axis-aligned boxes alone.
- Express every secondary object's size and spacing relative to the anchor or canvas.

### 6. Resolve direction and depth

For every directional object, record:

- connection or start endpoint;
- outer or end endpoint;
- screen-projected path;
- near and far endpoint roles;
- toward-viewer, away-into-scene, parallel, or ambiguous depth trajectory;
- visible faces and face orientation;
- near/far size change, edge convergence, foreshortening, and self-occlusion.

Use clock directions only as optional shorthand for the screen projection. Never use them as a substitute for depth.

### 7. Build the visual-layering system

Follow `references/layering-hidden-shapes.md`.

- Classify the global spatial order as total, partial, multiple-local, or unresolved; create a back-to-front stack only where valid.
- Add region-specific pairwise relations, overlap types, contour ownership, and local reversals for interlocking objects.
- Build visibility profiles for the primary subject, major objects, and compositionally important small front elements. Keep bounding-box size, visible silhouette, inferred full envelope, and visible fraction separate.
- Distinguish physical depth, projected placement, perceptual order, and production-layer order.
- Infer masks, clipping, knockouts, outline redraw, text overlays, and finishing stages only from visible evidence; mark exact authoring history unresolved for flattened sources.
- Reconstruct only the minimum hidden geometry supported by contour continuity and known structure.
- Record alternate hidden-shape hypotheses when the evidence permits multiple solutions.
- For style transfer, convert exact relations into layer roles, category ordering, overlap grammar, visibility priorities, and target-mapping rules.

### 8. Analyze object modeling and surface systems

Follow `references/object-modeling.md`, `references/line-color-texture.md`, and `references/color-relationships.md`.

Conclude:

- recognition strategy, shape grammar, mass hierarchy, and protected clean masses;
- modeling mode; value-plane count, span, contrast, and edge behavior; gradient policy;
- lighting ceiling; material response; line-based volume; object-detail density; object-tier rules and scoped exceptions;
- palette mode; color roles and area shares; hue-distance structure; temperature allocation; value ladder; saturation budget; adjacency policies; opacity and separation;
- flat, gradient, translucent, dense, thin, textured, or boundary-breaking fill behavior;
- material evidence versus material evocation;
- light, side planes, shadows, and volume construction;
- the three line systems and their hierarchy;
- overall texture plus decisive local exceptions.

### 9. Map details to each object

For each object, add:

- identity and role;
- importance tier: primary subject, major object, supporting object, or background element;
- geometry and proportions;
- frame position and occupancy, mandatory for the primary subject and major objects;
- endpoints, direction, depth, and visible faces;
- attachment and frame contact;
- layer role, local occlusion relations, overlap type, visible fraction, protected visible cues, and production-stage evidence;
- modeling mode and any object-level override;
- value planes, lighting ceiling, material response, line-based volume, object-detail density, and protected clean regions;
- fill, color role, adjacency/separation behavior, material, and volume;
- subject contour, border, and internal line treatment;
- text, symbols, stickers, hardware, damage, and other decoration;
- semantic group, focal role, visual-weight contribution, and narrative-device membership;
- visible facts, inferences, and unresolved parts.

Keep global rules out of the object inventory unless an object is a clear exception.

### 9b. Derive transferable drawing rules

For style_transfer or both, follow `references/style-transfer.md`. Extract the decisive mechanisms, distinguish fixed rules from variables and source-specific content, establish the visual-layering and object-modeling systems, select the palette mode, build the target content-capacity gate, and describe how a new subject is simplified, layered, occluded, exposed, deformed, outlined, filled, shaded, textured, composed, distributed across quiet and dense zones, grouped semantically, and guided through a focal path. Apply the selected subtype rules. Retain only evidence-supported rules as established; mark new-category decisions as hypotheses. Substituting object names with slots alone does not establish transferability.

### 10. Prioritize generation constraints

Rank constraints by user intent and this reference's perceptual identity, not a fixed geometry-over-style hierarchy:

- **hard**: explicit frozen requirements and evidence-supported mechanisms whose loss would break the requested reconstruction or style identity. Color, edge behavior, brushwork, or texture may belong here.
- **medium**: supporting mechanisms with bounded flexibility that preserve the hard constraints.
- **soft**: incidental variations such as individual grain positions or minor marks; never demote an entire stylistically decisive dimension automatically.

For each decisive mechanism, state evidence, scope, priority reason, what stays fixed, what may vary, and an observable failure sign. Keep confidence separate from importance: a high-impact unknown remains unresolved, not a fabricated hard fact. When requirements conflict, report the conflict and seek a choice only when it blocks the task.

In reconstruction, include source-specific geometry and appearance priorities. In style_transfer, retain drawing/organization rules and derive target-specific geometry from the new content; do not freeze source object counts, identities, poses, or coordinates unless explicitly requested. Separate literal palette colors from color relationships and mark which are actually fixed. Default to `preserve_source` when the user is silent about color. Use `relationship_transfer` only for an explicit recoloring direction and `custom_palette` when an overall palette, color set, or role mapping is supplied; isolated required object colors remain frozen roles inside the selected mode. In either recoloring mode, preserve or deliberately remap hue distance, temperature allocation, value ladder, saturation budget, and adjacency behavior.

In both modes, convert the observed modeling profile into explicit ceilings and floors before compiling target objects. Preserve the global modeling mode and object-tier progression; add exceptions only with visible support. For every material-rich noun, state the permitted rendering cue and prohibited expansion. Keep canvas-level density rhythm separate from object-detail density.

When layering affects recognition or composition, promote the visual-layering system to a hard constraint. Specify the spatial bands, decisive local front/rear relations, overlap types, contour termination or redraw behavior, visibility budget, protected identity cues, masks or clipping devices, and supported production-stage conventions. In style transfer, recompute target objects within the same role-based grammar instead of freezing source IDs or coordinates.

When density rhythm contributes materially to the reference identity, promote it to a hard constraint. Specify quiet-zone location, minimum share or qualitative floor, continuity, allowed interruptions, dense-cluster location and count or range, per-cluster module allowance, text-group allowance, breathing gaps, primary-subject clean-area floor, and concrete no-content areas. Run the content-capacity gate before writing any supporting-element list. Assign every included secondary element to a density cluster or permitted interruption; omit unassigned candidates. If required items exceed the supported capacity, report the conflict instead of silently filling the quiet field.

When focal hierarchy or visual organization defines the reference, specify the first-read subject, ordered viewing path, balance relation, motif cadence, semantic groups, and the graphic device assigned to each group before surface styling. Preserve the organization relation while recomputing target-specific objects and positions.

Compile concise mode-specific prompts according to `references/generation-blueprint-schema.md`. Begin generation prompts with the execution contract: density and clean-area floors, cluster/text limits, overflow rule, visual-layering grammar, and modeling/lighting ceilings. Then introduce target identity and only the target details admitted by the capacity gate. Express relationships rather than keyword piles, and use avoidances only for concrete style drift or explicit exclusions. A 'hard' textual constraint is a requested priority, not an execution guarantee.

Translate abstract depth into visible consequences. Do not rely on raw XYZ coordinates alone.

### 11. Audit before finalizing

Follow `references/evidence-audit.md`.

- Verify shape grammar, modeling mode, value structure, lighting ceiling, material response, line-based volume, object-detail density, line, fill, color-role relationships, texture, and canvas density across separated regions.
- Compare normal-size, thumbnail, grayscale, and mildly blurred views for over-modeling, under-modeling, added highlights or gradients, extra depth lines, lost clean masses, and incorrect detail progression across object tiers.
- Compare full-frame, thumbnail, grayscale, and adjacency/flat-color views for large-mass separation, temperature allocation, value order, bounded accents, and color adhesion.
- Verify the spatial stack, decisive local occlusions, contour ownership, masks or clipping, visibility profiles, and production-order claims. Keep exact authoring history unresolved for flattened sources.
- Verify the content-capacity gate before prompt delivery: every included secondary element has one cluster or permitted interruption, candidate pools were actually reduced, required items fit the stated capacity, protected quiet zones contain no prohibited content, and material-rich nouns appear after the execution contract.
- Compare the full frame at normal size, thumbnail size, and mild blur to confirm the same quiet fields, density peaks, cluster separation, and clean-subject areas remain legible.
- Verify first-read order, viewing path, visual-weight balance, motif repetition, narrative-device roles, and semantic grouping at both full-frame and thumbnail sizes.
- Verify that the selected subtype modules match visible evidence and that unselected subtype rules did not leak into the blueprint.
- Verify object counts, text, primary-subject and major-object position and occupancy, proportions, endpoints, visible faces, and occlusion with fresh crops.
- Seek counterexamples to every global claim.
- Reconcile all local findings against the full frame.
- Rewrite the final report from the corrected state.
- Audit style rules for source-content leakage and unsupported cross-category generalization. Only audit claims actually made; do not perform an exhaustive object census for a style-only task.
- Provide mode-specific generation acceptance criteria using `references/generation-validation.md`. Mark generation validation `not_run` when no generated result was inspected. A correct source analysis does not establish prompt effectiveness.

Keep the claim ledger and crop audit internal unless the user asks to see them.

## Default output order

For style_transfer, use the independent output order in `references/generation-blueprint-schema.md`. For both, share the visual conclusion once and label the following reconstruction section separately from the style-transfer section.

1. Task mode, source roles, illustration classification, and loaded modules
2. Global visual conclusion
3. Frame and camera
4. Focal hierarchy, viewing path, and visual-weight balance
5. Composition skeleton, primary-subject and major-object occupancy, and position
6. Density rhythm, quiet fields, cluster separation, and negative-space budget
7. Target content-capacity gate and overflow decisions, when target content is supplied
8. Motif grammar, narrative devices, and semantic groups
9. Relative proportions, endpoints, orientation, and depth
10. Visual-layering system: spatial stack, local occlusion, visibility, production order, and hidden shapes
11. Object-modeling system and object-tier rules
12. Color relationship system and palette mode
13. Fill and surface execution
14. Line system
   - subject contours
   - external frames and borders
   - internal lines
15. Texture summary
16. Object detail cards
17. Generation constraint priorities
18. Uncertainties
19. Generation acceptance criteria and validation status

Follow `references/generation-blueprint-schema.md` for field-level structure.

## Output style

- Lead with conclusions, not the inspection narrative.
- Preserve information density; concise does not mean vague.
- Give degree, scope, and meaningful exceptions.
- Keep texture short unless it is a decisive style mechanism.
- Scale report detail to the request; keep audit bookkeeping internal. Do not launch generation, broad test suites, template production, or file conversion merely because analysis produced a blueprint.
- Expand object details when the user needs generation control.
- Do not expose internal crop counts, sample matrices, or claim ledgers by default.
- Do not state artist, period, medium, intention, or hidden content as fact without independent support.
