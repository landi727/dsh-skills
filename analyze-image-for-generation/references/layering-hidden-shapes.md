# Visual Layering, Occlusion, and Hidden Shapes

## Contents

1. Purpose and independent systems
2. Spatial stack and local occlusion graph
3. Overlap grammar and visibility budget
4. Production stack and compositing evidence
5. Hidden-shape inference
6. Style transfer and prompt compilation
7. Failure signs and acceptance

## Purpose

Convert visible stacking into an executable layer system. Analyze which elements cover others, how contours behave at overlaps, how much of each object remains visible, and which production operations are supported by the finished image.

Infer the minimum layer relations required by visible evidence. A flattened raster usually cannot reveal the original Photoshop, Illustrator, or drawing-app layer history. Record exact authoring order as unresolved unless an editable source exposes it.

## 1. Keep four systems independent

Separate:

- **projected placement**: canvas position, bounds, size, crop, and visible silhouette;
- **spatial order**: what appears behind or in front in the depicted scene;
- **production order**: background, fills, contours, masks, text, and finishing marks as likely drawing or compositing stages;
- **perceptual order**: what the viewer notices first, handled by `visual-organization.md`.

Do not derive layer order from object size, vertical canvas position, semantic importance, detail density, or focal weight. A small object can sit on the top visual layer and remain fully exposed; a large primary subject can lose substantial visible area while retaining first-read dominance.

## 2. Build the spatial stack

Classify the global order as `total`, `partial`, `multiple_local`, or `unresolved`.

Where a global stack is supported, list `L0`, `L1`, and onward from back to front. Give each layer a role, its contents, evidence, and confidence. Treat this as a partial ordering when unrelated elements never overlap.

Add local relations for every decisive overlap:

`A ≺ B @ region` means A is behind and is occluded by B in that region.

Record:

- rear and front object or role;
- overlap region;
- overlap type;
- which front contour remains continuous;
- where the rear contour terminates, reappears, merges, or remains visible through the front element;
- whether a shared border, knockout gap, or redrawn outline separates them;
- whether the relation reverses elsewhere;
- evidence and confidence.

Do not force disjoint objects into a total order. For clamps, straps, rings, limbs, cables, foliage, or woven assemblies, retain multiple region-specific relations and name the interlock.

## 3. Classify overlap and visibility

Use an evidence-supported overlap type:

- `cover`: one opaque element covers another;
- `crossing`: two elongated elements cross once;
- `interlock`: the relation reverses across regions;
- `inset`: an element sits inside a bounded host region;
- `window`: a nested scene is visible through an opening;
- `cutout`: a foreground shape removes or reveals part of another;
- `clip`: content is visibly constrained by a frame or silhouette;
- `transparent_overlay`: both layers remain visible through compositing;
- `text_or_mark_overlay`: lettering, symbols, or finishing marks sit over imagery;
- `frame_crop`: the canvas edge hides part of an element;
- `shared_boundary`: adjacent shapes meet without clear front/rear depth;
- `unresolved`.

For each primary or major object, and for any small front element whose exposure is compositionally important, record a visibility profile:

- projected bounding-box occupancy;
- visible-silhouette occupancy;
- inferred full-envelope occupancy when supported;
- visible fraction or qualitative exposure level;
- number of separated visible fragments;
- identity-bearing cues that remain exposed;
- protected visible regions;
- allowed occlusion and prohibited coverage;
- measurement status.

Keep object size independent from exposure. A small top-layer label may have a low canvas share and a high visible fraction. A large rear object may have a high inferred envelope and a much lower visible fraction.

## 4. Infer the production stack conservatively

Record only production stages supported by edge and compositing evidence. Common roles include:

1. ground or background field;
2. rear environment fills;
3. primary and supporting object fills;
4. foreground fills or inserted fragments;
5. redrawn silhouettes, borders, and shared outlines;
6. internal structure and decorative lines;
7. clipped windows, nested scenes, labels, text, and symbols;
8. finishing texture, registration effects, or global marks.

For each stage, state the operation, affected content, evidence, confidence, and whether its exact order is recoverable. Record visible evidence for:

- masks and clipping containers;
- knockouts or reserved gaps;
- transparent overlays, overprint, or underlayer visibility;
- outline redraw after fills overlap;
- text or marks that consistently sit above object fills;
- nested groups such as panels, windows, badges, and cutaways.

Do not invent blend modes, layer names, hidden groups, or editable structure from a flattened image. Spatial depth and production order may disagree: a rear object can receive a finishing outline above a front fill, and a foreground texture can cross several spatial layers.

## 5. Reconstruct hidden geometry conservatively

Use:

- collinear edges;
- continuous curvature;
- repeated width;
- symmetry;
- known structural continuity;
- matching fill and border systems;
- object semantics only as a lower-confidence aid.

Separate:

- visible shape;
- strongly supported hidden envelope;
- plausible alternate continuation;
- unresolved hidden content.

Do not reconstruct hidden texture, exact torn edges, damage, lettering, hardware, brush marks, or small symbols without direct support elsewhere.

When two fragments may belong to one shape or separate objects, retain both hypotheses. Use `high`, `medium`, `low`, or `unresolved` confidence and state what evidence would discriminate them.

## 6. Transfer the layer grammar

The visual-layering output block is mandatory for reconstruction and style transfer. Do not merge it into generic composition or spatial-construction prose. Report `unresolved` for unsupported production history or category rules rather than omitting the system.

For style transfer, retain the organization rules that survive subject replacement:

- layer-role families such as field, rear environment, primary mass, nested scene, annotation, and foreground accent;
- supported category ordering and local reversals;
- preferred overlap types and bounded overlap frequency;
- contour termination, shared-border, knockout, and outline-redraw behavior;
- mask, window, inset, cutaway, or clipping conventions;
- visibility priority by object tier;
- identity cues and quiet masses that must remain exposed;
- allowed coverage of supporting and background elements;
- production-stage conventions supported by repeated evidence.

Treat exact source object IDs, layer counts, coordinates, and incidental crossings as source-specific. Recompute the target stack from its semantic groups, identity cues, focal roles, and density budget. Mark category-to-category rules inferred from a single example as provisional.

Compile prompts in this order: target and visual hierarchy → density and composition → layer roles and spatial bands → decisive local occlusions and masks → visibility protections → production-stack conventions → object modeling and surface systems. Use exact object relations for reconstruction and role-based grammar for style transfer.

Use this minimum labeled human-readable block before object modeling:

- `Spatial-order status`
- `Layer roles`
- `Local relations and overlap types`
- `Visibility profiles and protections`
- `Production-order evidence and recoverability`
- `Fixed rules`
- `Variables`
- `Target mapping`
- `Failure signs`
- `Acceptance checks`

Do not compress the system into one composition bullet. Use `unresolved` where evidence is unavailable.

## 7. Failure and acceptance

Treat these as failures when they violate the source-derived system:

- ordering objects by size or importance instead of visible overlap evidence;
- flattening all elements onto one depth band;
- forcing an interlock into one global front/back statement;
- reversing a decisive local relation;
- covering a protected identity cue, face, label, window, or clean mass;
- exposing hidden rear details unsupported by the source;
- losing a window, inset, cutout, clipping boundary, knockout, or shared border;
- adding cast shadows or optical depth solely to explain a graphic overlap;
- merging separate overlap clusters until the source's breathing gaps disappear;
- claiming an exact production history from a flattened image.

At normal size, inspect decisive contour terminations, masks, shared borders, and local reversals. At thumbnail and mild blur, compare spatial-band separation, primary-subject exposure, foreground interruptions, and cluster readability. In reconstruction, compare the local occlusion graph and visibility profiles. In style transfer, compare layer-role grammar, overlap types, protected visibility, and production conventions without requiring the source's literal stack.

Report `pass`, `partial`, `fail`, or `not_run` separately from source-analysis confidence.
