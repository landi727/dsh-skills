# Transferable Illustration Style

## Evidence to reusable rules

Start from the shared visual analysis. Identify the few mechanisms that most strongly determine perceptual identity; usually 3–5 suffice, without forcing a quota. For each, state visible support, scope, interacting dimensions, and what would change perceptually if it were removed. 'Flat', 'retro', or 'hand-drawn' alone does not specify a drawing rule.

Classify findings as:

- **fixed rule**: supported behavior to preserve across target content;
- **variable**: what can change, with conditions or a supported range;
- **source-specific**: this scene's identities, exact arrangements, incidental marks, and text;
- **hypothesis/unresolved**: plausible extensions with insufficient evidence.

Spatial scope (global/local/mixed) and transfer confidence are independent. A feature appearing everywhere in one picture may still be content-specific. Use contrasting objects or multiple references to support transfer; do not invent absent subject categories. Multiple references may contain meaningful variants; document their conditions.

Classify the illustration through `illustration-type-routing.md` and apply only the selected subtype modules. Record which decisive rules come from the shared visual system and which come from a subtype module.

Inspect layering and modeling before target mapping, expanding their references when they affect the task. Treat the subtype as supporting evidence and refinement, not an automatic layer, modeling-mode, or priority assignment. Follow generation-blueprint-schema.md for output depth and final compilation.

## Drawing transformations

For dimensions with usable evidence, express an action and its visible consequence. Mark unsupported dimensions briefly rather than inventing instructions.

| Dimension | Transfer rule to extract |
| --- | --- |
| Recognition and simplification | Which silhouette or structural cues preserve identity; which detail types are omitted, merged, or symbolized; which masses remain clean |
| Shape and deformation | Primitive construction, primary/secondary mass hierarchy, connections, curve/corner behavior, inflation/compression, exaggeration of parts, intentional asymmetry; connect proportions to the relevant part/category |
| Line and edge | Relative contour/internal-line weights; closure, taper, wobble scale, breaks; where edges are crisp, soft, missing, or fill-defined; which line families may construct volume |
| Fill and color | Opacity and contour adherence; palette mode, color roles and area shares, hue-distance structure, temperature allocation, value ladder, saturation budget, adjacency/separation, and fixed hues |
| Light and volume | Modeling mode, value-plane count/span/contrast, visible side treatment, edge behavior, gradient policy, lighting ceiling, shadow shape, and coherent versus symbolic illumination |
| Brushwork and texture | Mark size relative to object/canvas, density, direction, contrast, boundary crossing; surface-following marks versus global overlay |
| Detail hierarchy | Identity, structural, decorative, and surface microdetail density; clean-area share; how detail changes with focal importance and object size |
| Layering and occlusion | Spatial bands, local front/rear relations, overlap types, interlocks, contour ownership, visibility profiles, masks/clipping, protected cues, and production-stage conventions |
| Density rhythm and negative space | Quiet/transition/dense zone topology, largest quiet-field continuity, density-peak count and separation, breathing gaps, subject cleanliness, transition direction, and density drivers; follow `density-rhythm.md` |
| Focal hierarchy and viewing path | First-read entry, primary and secondary focal order, saliency drivers, path, loops, and exits; follow `visual-organization.md` |
| Visual weight | Dominant mass, counterweights, balance axis, edge tension, and the contribution of area, contrast, saturation, detail, and isolation |
| Motif grammar | Repeated shape, line, border, color, symbol, spacing, scale progression, orientation, alternation, and controlled mutation |
| Graphic narrative devices | Windows, panels, cutaways, arrows, labels, diagrams, sequences, badges, and nested scenes mapped to their functions |
| Semantic grouping | Story or functional groups, membership, hierarchy, boundaries, and connectors; every target element receives one group and role |
| Space and composition | Projection convention, mass balance, negative-space rhythm, overlap behavior, depth compression; distinguish organization grammar from exact source coordinates |
| Typography, when present | Letter construction, weight/scale, spacing, relation to imagery; keep literal source copy separate |

Describe interactions: a soft silhouette may coexist with crisp interior divisions; color contrast may replace outlines. Avoid assigning the same line, shade, or texture treatment uniformly when the source distinguishes object types.

## Apply to new subjects

Keep a reusable style block independent from a target-content block. For each supplied target, map identity cues → simplification/deformation → contour and internal structure → fill/volume/texture → scene role. Let the target's recognizable structure survive the transformation. Do not insert source props or poses to make a new subject seem stylistically similar.

Preserve the selected fixed style rules; recompute target composition and proportions using the supported organization grammar. Separate broad drawing rules from a single source's palette/layout choices; mark the latter as task defaults or source-specific choices unless evidence establishes their wider scope. User-requested frozen composition is a separate layout constraint, not evidence that those coordinates define the style. For unsupported categories, identify the exact extrapolation and label it provisional. Use available references first; request an additional example only when that missing evidence blocks the requested fidelity.

Recompute a density budget for the target. Preserve quiet/dense relationships that define the reference; retain exact zone topology or peak counts only when explicitly frozen or supported as defining organization mechanisms. A single source's coordinates and counts do not establish a universal template. Protect named quiet regions, group secondary elements into bounded clusters, retain breathing gaps, and keep supported clean areas inside the main subject. Before allocation, classify user content as required, candidate, or incidental from its labels and wording. Assign every included supporting element to a semantic group, graphic device, focal role, and density cluster or quiet-zone exception. Apply the capacity order from `density-rhythm.md`; do not carry an unassessed candidate pool into the prompt; retaining all candidates is valid when their combined load fits.

Recompute the target layer map after assigning semantic and focal roles. Preserve protected visibility and overlap grammar while allowing target-specific object identities, sizes, and coordinates.

## Visual-layering transfer

Keep layering distinct in analysis. In a full blueprint, give it a labeled block ordered by importance; use a short statement for simple relations and expand supported fields for decisive overlaps. Compact output includes it when it affects the requested identity.

Follow `layering-hidden-shapes.md` and preserve these independently when supported:

- layer-role families and spatial-band order;
- local front/rear grammar and allowed reversals;
- overlap types, edge ownership, contour termination, shared borders, and outline redraw;
- masks, clipping, windows, insets, cutaways, knockouts, and transparent overlays;
- visibility priorities, protected identity cues, and allowed coverage by object tier;
- production-stage conventions whose evidence survives subject replacement.

Use exact source object relations only for reconstruction. For style transfer, map target semantic groups into the source-derived roles, then recompute a partial stack and local occlusion graph. Keep exact layer count, incidental crossings, and authoring history source-specific. Mark single-example category rules as provisional.

For decisive layering, report the applicable spatial-order status, roles, local relations, visibility protections, target mapping, and acceptance checks. Report production-order recoverability only when consequential; keep irrelevant unknowns internal. Formal JSON retains its required fields.

## Object-modeling transfer

Follow `object-modeling.md` and preserve these independently when supported:

- recognition strategy and shape grammar;
- main and secondary mass hierarchy;
- modeling mode and object-tier progression;
- value-plane count, value span, adjacent contrast, edge behavior, and gradient policy;
- lighting ceiling for highlights, shadows, cast shadows, ambient occlusion, specular response, reflections, transparency, refraction, and glow;
- material-response cues and forbidden expansions;
- line-based volume roles;
- object-detail density and protected clean masses.

Create one global profile plus evidence-supported overrides for the primary subject, major objects, supporting objects, background elements, nested scenes, and special materials. Keep canvas density in `density-rhythm.md` and object-internal modeling density in `object-modeling.md`.

Map each target's identity cues into the source-derived shape grammar; qualify material and part names locally with the rendering behavior that applies. A target noun does not authorize physical shading or optical behavior absent from the reference. State both the minimum mechanism required to preserve the source and the maximum rendering intensity allowed.

## Palette-mode routing

Follow `color-relationships.md` and select exactly one palette mode before compiling the prompt:

- `preserve_source` when the user gives no color instruction; preserve literal source hue families together with their roles and relationships;
- `relationship_transfer` only when the user explicitly requests a different color direction or environmental/brand adaptation;
- `custom_palette` when the user supplies an overall palette, color set, or role mapping.

Do not infer recoloring permission from target subject matter. Treat isolated required object colors as frozen roles within the current mode rather than an automatic custom palette. In recoloring modes, map the palette as a coordinated system: functional roles and area shares → hue-distance pattern → warm/cool/neutral allocation → value ladder → saturation budget → adjacency and separation devices → literal target hues. Reject unintended collapse only where the source or task requires separation. Preserve evidence-supported near-value hues, blending, and lost boundaries; grayscale separation is not universal.

Apply the same literal-versus-relational distinction to viewpoint, aspect ratio, object count, and background content.

## Prompt and leakage check

Before compiling, assess the combined load of included content: each included item has a role and allocation, source-supported quiet areas and required visibility remain intact, and content fits the selected density pattern. Retain all candidates when they fit. Stop and report a conflict only when required content cannot fit after consolidation.

Compile using the single policy in `generation-blueprint-schema.md`: task anchor → dynamically ranked visual core → target mapping with local controls → remaining nonredundant controls. A decisive color, brushwork, gesture, layer relation, or density rule belongs early according to its importance. Keep material limits close to the relevant nouns; no universal execution-contract prefix is required.

Preserve actual reference images as anchors in image-capable generation; support a standalone text style block when requested and state which delivery was tested. Before delivery, remove literal source objects, named scenes, exact poses, coordinates, and source text from reusable rules unless explicitly frozen. Check that the prompt describes how to draw an unfamiliar target. Report observed scope and untested categories rather than claiming arbitrary transfer.
