# Generation Blueprint Schema

## Contents

1. Reconstruction report sections
2. Style-transfer output
3. Machine-readable output
4. Prompt compilation

## Default human-readable report

Begin with mode, desired fidelity, source/reference roles, illustration classification, classification confidence, and loaded subtype modules. For both modes, share the visual evidence once, then keep reconstruction and style-transfer outputs independent. Use the following Sections 1–13 for reconstruction unless the user requests another format.

## 1. Global visual conclusion

Write compact, mechanism-based paragraphs for:

- graphical modeling;
- visual-layering system and visibility priorities;
- object-modeling system and intensity limits;
- color construction and role relationships;
- fill mechanism;
- shape and deformation;
- volume and light;
- detail distribution;
- density rhythm and negative-space structure;
- focal hierarchy, visual weight, motif grammar, narrative devices, and semantic grouping;
- spatial construction.

Do not include crop history or reasoning narration.

## 2. Frame and camera

Report:

- frame orientation and aspect;
- crop and frame crossings;
- fixed view;
- dominant visible faces;
- camera height;
- perspective strength;
- framing distance;
- unresolved camera ambiguity.

## 3. Composition and geometry skeleton

Report:

- anchor object;
- primary subject and major-object registry;
- primary and secondary axes;
- center of gravity;
- density-zone map: meaningful bounds, level, area share or estimate, drivers, and boundary character;
- largest continuous quiet field and its allowed interruptions;
- density-peak count, cluster separation, transition direction, and breathing gaps;
- primary-subject cleanliness and frame-edge accumulation;
- object registry;
- projected size and spacing;
- for the primary subject and every major object:
  - normalized projected center;
  - projected bounding-box limits;
  - canvas-width and canvas-height spans;
  - bounding-box area as a fraction or percentage of the canvas;
  - visible silhouette area as a fraction or percentage of the canvas;
  - edge margins, frame crossings, and measurement status.

Keep visible silhouette occupancy separate from bounding-box occupancy. If an occluded full shape is estimated, label that inferred value separately rather than replacing the visible value.

## 4. Visual organization

Report each dimension as observation, evidence and scope, generation constraint, failure sign, and acceptance check:

- focal hierarchy and viewing path;
- visual weight and balance;
- motif grammar;
- graphic narrative devices;
- semantic grouping.

Follow `visual-organization.md`. Record subtype-specific additions from the loaded modules without importing unused module fields.

## 5. Object direction and depth

For each directional object:

- connection/start endpoint;
- outer/end endpoint;
- endpoint screen positions;
- endpoint near/far roles;
- projected path;
- depth trajectory;
- visible faces;
- perspective result.

## 6. Visual-layering system and hidden shapes

Report:

- global spatial-order status and meaningful back-to-front bands;
- decisive local occlusion relations, overlap types, contour ownership, and interlocking attachments;
- visibility profiles: bounding-box occupancy, visible silhouette, inferred full envelope, visible fraction, protected cues, and allowed coverage;
- masks, clipping, cutouts, windows, knockouts, shared borders, and transparent overlays;
- production stages, outline redraw, text/finishing order, and recoverability of exact authoring history;
- reusable layer roles, category order, overlap budget, visibility priority, and target mapping;
- hidden geometry needed for reproduction;
- alternate hypotheses and unresolved parts.

Follow `layering-hidden-shapes.md`. Keep size, spatial depth, production order, and perceptual priority independent.

## 7. Object-modeling system

Report:

- recognition strategy, shape grammar, and mass hierarchy;
- global modeling mode and scoped exceptions;
- value-plane count, light-to-dark order, value span, adjacent contrast, area relations, edge behavior, and gradient policy;
- lighting ceiling for highlights, shadows, cast shadows, ambient occlusion, specular response, reflections, transparency, refraction, and glow;
- material-response rules and forbidden expansions;
- line-based volume roles;
- object-detail density, protected clean masses, and progression across object tiers;
- over-modeling and under-modeling signs plus acceptance checks.

Follow `object-modeling.md`. Keep canvas-density rhythm separate from object-internal modeling density.

## 8. Color relationship system

Report:

- palette mode and explicitly frozen colors;
- functional color roles, regions, and approximate area shares;
- hue-distance relations among major roles;
- warm/cool/neutral allocation and spatial counterweights;
- value ladder and saturation budget;
- adjacency policies and separation devices;
- color-adhesion failure signs and acceptance checks.

Follow `color-relationships.md`. Keep literal hue choices separate from transferable relations.

## 9. Surface systems

Report:

- color and fill;
- material, light, and volume;
- subject contours;
- external frames and borders;
- internal lines;
- overall texture and distinctive local texture.

## 10. Selected subtype findings

For each loaded subtype module, report:

- module name and evidence;
- decisive findings;
- generation constraints;
- visible failure signs;
- acceptance checks.

Do not include unloaded subtype fields.

## 11. Object detail cards

For each object:

- identity and role;
- importance tier;
- geometry and proportion;
- frame position and occupancy, mandatory for the primary subject and major objects;
- direction and visible faces;
- attachment, layer role, local occlusion, visible fraction, protected cues, production-stage evidence, and crop;
- object-modeling override, value planes, lighting ceiling, material response, line-based depth, detail density, and protected clean regions;
- color, fill, material, and volume;
- line treatment;
- text, symbols, hardware, stickers, and decoration;
- semantic group, focal role, visual-weight contribution, and narrative-device membership;
- uncertainties.

## 12. Generation constraints

Separate:

- hard constraints;
- medium constraints;
- soft constraints;
- avoidances.

Assign priorities dynamically from task intent and decisive style mechanisms. Record evidence, scope, priority reason, allowed variation and visible failure sign for each decisive rule. No dimension has a permanent priority: source geometry can be hard in reconstruction; line or texture behavior can be equally hard. Distinguish uncertainty from flexibility.

## 13. Uncertainties

List only uncertainties that affect reconstruction or generation.

Add generation acceptance criteria, source-audit status, generation-validation status, and tested scope. Mark generation `not_run` without inspected outputs.

## Style-transfer output

1. Illustration classification, confidence, and loaded subtype modules.
2. Overall visual system and decisive mechanisms, with supporting observations.
3. Fixed rules, variables, source-specific content, and hypotheses/unknowns.
4. Visual-layering system: spatial bands, local occlusion graph, overlap types, interlocks, contour ownership, visibility profiles, masks/clipping, production order, layer grammar, and hidden-shape limits.
5. Object-modeling system: shape grammar, mass hierarchy, modeling mode, value structure, lighting ceiling, material response, line-based volume, object-detail density, object-tier rules, exceptions, and over/under-modeling signs.
6. Palette mode and color relationship system: roles, area shares, hue-distance pattern, temperature allocation, value ladder, saturation budget, adjacency rules, and adhesion failures.
7. Drawing transformations: recognition/simplification, layering/occlusion, deformation, line/edge, fill/color, light/volume, brushwork/texture, detail hierarchy, spatial organization, and typography when applicable.
8. Visual organization: focal hierarchy and viewing path, visual weight, motif grammar, graphic narrative devices, and semantic grouping.
9. Density rhythm and content-capacity gate: zone map, protected quiet fields and floors, density peaks, cluster separation, subject cleanliness, transition direction, cluster/text limits, required/candidate/incidental inventory, allocation ledger, overflow decisions, and target density budget.
10. Selected subtype findings and their target application.
11. Interactions and exceptions; transfer scope and unsupported categories.
12. Target application when supplied, kept separate from reusable rules.
13. Dynamic constraint priorities and concrete drift exclusions.
14. Reusable style prompt when requested, plus a separate target-content block.
15. Acceptance criteria, source-audit status, generation-validation status and tested scope.

Section 4 is mandatory and must appear as a labeled block before object modeling. Use explicit subfields for spatial-order status, layer roles, local relations and overlap types, visibility profiles and protections, production-order evidence and recoverability, fixed rules, variables, target mapping, failure signs, and acceptance checks. Do not collapse it into drawing transformations, spatial organization, density rhythm, or interactions; use unresolved fields when evidence is insufficient.

Follow style-transfer.md for rule derivation and generation-validation.md for acceptance. Keep source identities/counts/coordinates out of the reusable prompt unless explicitly frozen by the user.

## Machine-readable output

When the user requests JSON:

- use `task-blueprint.schema.json` as the dual-mode envelope; resolve its local reference to the retained `generation-blueprint.schema.json` only for reconstruction payloads;
- record one primary illustration type, up to two supporting types, classification evidence, confidence, and loaded modules;
- use normalized coordinates only when measured or explicitly estimated;
- encode canvas occupancy as a fraction from 0 to 1 and keep bounding-box area distinct from visible silhouette area;
- use `null` or `unknown` rather than invented values;
- encode the selected palette mode and the independent color relationship system; preserve measurement status for area shares;
- encode the independent object-modeling system, including explicit ceilings, object-tier rules, clean-area measurement status, and over/under-modeling signs;
- encode the density content-capacity gate: protected quiet-zone floors, cluster and text-group limits, required/candidate/incidental items, included-item allocation, overflow decisions, and measurement status;
- encode the independent visual-layering system, including spatial-order status, local relations, overlap types, production-order recoverability, visibility profiles, and transfer grammar;
- keep internal crop evidence outside the JSON unless requested;
- include concise conclusions, not the full reasoning process.

The envelope separates source audit from generation validation, requires evidence-linked mechanisms with priorities, and selects reconstruction, style_transfer, or both payloads. Each source binding identifies an actual available source and its role. Use null for unrun prompt/output fields. The reconstruction payload retains the original geometry format; its `verification` refers only to source audit. Do not fill reconstruction fields for style-only tasks.

## Prompt compilation

When the user requests a reconstruction prompt, compile the blueprint in this order, introducing the highest-priority style mechanisms alongside the main geometry rather than burying them under secondary details:

1. frame and fixed camera result;
2. first-read subject, viewing path, dominant weight, and counterweights;
3. density budget, protected quiet zones, semantic groups, and graphic devices;
4. anchor, primary subject, major-object placement, and composition skeleton;
5. object count, frame occupancy, projected proportion, endpoints, and depth;
6. visual-layering system: spatial bands, local occlusions, overlap types, contour ownership, masks/clipping, visibility profiles, and supported production stages;
7. motif grammar and selected subtype treatment;
8. recognition strategy, shape grammar, and mass hierarchy;
9. modeling mode and object-tier rules; value-plane count/span/contrast; lighting ceiling; material response; line-based volume; object-detail density and protected clean masses;
10. palette mode, color roles and area shares, hue-distance pattern, temperature allocation, value ladder, saturation budget, adjacency rules, then literal colors;
11. fill and remaining surface systems;
12. text, symbols, and decoration;
13. avoidances, including unsupported layer and modeling expansion;
14. preservation priority.

Do not insert every audit detail. Preserve dynamically selected hard constraints before flexible details. Bind actual references to their stated roles when image inputs are available, without inventing model parameters.

For style_transfer, compile: execution contract (quiet-zone floor/exclusions → cluster/text limits → clean-subject floor → overflow rule → modeling/value/light/material/line-volume/detail ceilings) → target identity and required recognition cues → first-read subject and viewing path → visual-weight relation → semantic groups and graphic devices → motif grammar → layer roles and spatial bands → local occlusions, overlap types, masks/clipping, visibility protections, and production conventions → target-specific mass mapping → only capacity-admitted supporting details inside their assigned clusters → selected subtype treatment → palette mode → color roles and area shares → hue-distance, temperature, value, saturation, and adjacency rules → literal colors → remaining spatial relationships → specific exclusions and preservation priorities. Keep the reusable style block independent of target nouns. Do not paste candidate pools into the prompt. For both, output separate prompts; do not concatenate constraints.
