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

Build the shared `layering-hidden-shapes.md` and `object-modeling.md` systems before applying target objects. Treat the subtype as supporting evidence and refinement, not an automatic layer or modeling-mode assignment.

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

Preserve fixed style rules; recompute target composition and proportions using the organization grammar. User-requested frozen composition is a separate layout constraint, not evidence that those coordinates define the style. For unsupported categories, identify the exact extrapolation and label it provisional. Use available references first; request an additional example only when that missing evidence blocks the requested fidelity.

Recompute a density budget for the target while preserving the reference's zone topology. Protect named quiet regions, group secondary elements into bounded clusters, retain breathing gaps, and keep supported clean areas inside the main subject. Before allocation, classify user content as required, candidate, or incidental from its labels and wording. Assign every included supporting element to a semantic group, graphic device, focal role, and density cluster or quiet-zone exception. Apply the capacity order from `density-rhythm.md`; do not carry the complete candidate pool into the prompt.

Recompute the target layer map after assigning semantic and focal roles. Preserve protected visibility and overlap grammar while allowing target-specific object identities, sizes, and coordinates.

## Visual-layering transfer

This is a required independent output section. Do not absorb it into `Space and composition`, density rhythm, or visual organization.

Follow `layering-hidden-shapes.md` and preserve these independently when supported:

- layer-role families and spatial-band order;
- local front/rear grammar and allowed reversals;
- overlap types, edge ownership, contour termination, shared borders, and outline redraw;
- masks, clipping, windows, insets, cutaways, knockouts, and transparent overlays;
- visibility priorities, protected identity cues, and allowed coverage by object tier;
- production-stage conventions whose evidence survives subject replacement.

Use exact source object relations only for reconstruction. For style transfer, map target semantic groups into the source-derived roles, then recompute a partial stack and local occlusion graph. Keep exact layer count, incidental crossings, and authoring history source-specific. Mark single-example category rules as provisional.

Report spatial-order status, layer-role families, decisive local relations and overlap types, visibility protections, production-order recoverability, fixed rules, variables, target mapping, failure signs, and acceptance checks even when some fields are unresolved.

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

Map each target's identity cues into the source-derived shape grammar before naming materials or parts. A target noun does not authorize physical shading or optical behavior absent from the reference. State both the minimum mechanism required to preserve the source and the maximum rendering intensity allowed.

## Palette-mode routing

Follow `color-relationships.md` and select exactly one palette mode before compiling the prompt:

- `preserve_source` when the user gives no color instruction; preserve literal source hue families together with their roles and relationships;
- `relationship_transfer` only when the user explicitly requests a different color direction or environmental/brand adaptation;
- `custom_palette` when the user supplies an overall palette, color set, or role mapping.

Do not infer recoloring permission from target subject matter. Treat isolated required object colors as frozen roles within the current mode rather than an automatic custom palette. In recoloring modes, map the palette as a coordinated system: functional roles and area shares → hue-distance pattern → warm/cool/neutral allocation → value ladder → saturation budget → adjacency and separation devices → literal target hues. Reject mappings that collapse large neighboring roles into the same temperature, nearby hue, and similar value without an effective separator.

Apply the same literal-versus-relational distinction to viewpoint, aspect ratio, object count, and background content.

## Prompt and leakage check

Before compiling, run a capacity preflight: every included item has one allocated cluster or permitted interruption; protected quiet zones have explicit exclusions; cluster and text-group maxima are not exceeded; candidate pools were reduced; and primary clean masses retain a floor. Stop and report a conflict only when required content cannot fit after consolidation.

Compile generation prompts in this order:

1. `Execution contract`: protected quiet-zone floor and exclusions; cluster/text limits; clean-subject floor; overflow rule; global modeling mode; value-plane, gradient, highlight, shadow, reflection, line-volume, and microdetail ceilings.
2. Target identity and required recognition cues, phrased through the established shape grammar.
3. First-read path, visual-weight relation, semantic groups, narrative devices, and motif grammar.
4. Layer roles, spatial bands, local occlusions, masks, visibility protections, and production conventions.
5. Only the supporting details admitted by the capacity gate, each named inside its assigned cluster.
6. Selected subtype rules, palette mode, color-role map, color relationships, remaining spatial relations, and concrete drift exclusions.

Do not place material-rich target nouns, a long environment list, or a text/symbol list before the execution contract. Preserve actual reference images as anchors in image-capable generation; also support a standalone text style block when requested. State which delivery was tested.

Before delivery, remove literal source objects, named scenes, exact poses, coordinates, and source text from the reusable block unless the user explicitly freezes them. Check that the prompt still describes how to draw an unfamiliar target. Do not claim the prompt transfers to arbitrary elements without tests; report observed scope and untested categories.
