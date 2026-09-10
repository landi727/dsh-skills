# Evidence Audit

## Contents

1. Claim ledger and multi-region support
2. Fresh crops and proportion checks
3. Direction and hidden-shape checks
4. Full-frame reconciliation and default disclosure

## Purpose

Verify externally testable conclusions against the source while keeping audit narration internal. Audit only claims used by the requested deliverable. Treat the lists below as evidence checks to select, not a requirement to produce every diagnostic for every image. Start with the full frame and use crops, thumbnail, blur, grayscale or color maps only when they resolve a consequential claim. Read detailed dimension references as routed by SKILL.md.

## 1. Build an internal claim ledger

Track:

- claim;
- claim class;
- source image;
- regions needed;
- status: pending, verified, corrected, or unresolved;
- final wording;
- scope: global, dominant, local, mixed, or unresolved.

Cover:

- count and identity;
- position and frame contact;
- projected size and proportion;
- endpoint roles and orientation;
- visible faces and perspective;
- spatial-order status, global layer bands, local occlusion relations, overlap types, contour ownership, masks/clipping, visibility profiles, production-order evidence, and layer grammar;
- hidden geometry;
- recognition strategy, shape grammar, mass hierarchy, modeling mode, value structure, lighting ceiling, material response, line-based volume, object-detail density, object-tier progression, and scoped exceptions;
- color roles, area shares, hue-distance relations, temperature allocation, value ladder, saturation budget, adjacency/separation, and fill;
- subject contours, borders, and internal lines;
- material, volume, texture, detail distribution, and density rhythm;
- illustration classification and loaded subtype modules;
- focal hierarchy, viewing path, visual weight, motif grammar, graphic narrative devices, and semantic grouping;
- text and symbols.

## 2. Require multi-region support for global surface and color claims

For global or dominant conclusions about object modeling, line, color, fill, detail, or texture:

- inspect at least three non-overlapping regions when the image provides them;
- cover at least two object types when available;
- inspect a likely counterexample;
- compare at consistent zoom;
- downgrade the claim to local when broader support is absent.

Do not force the minimum when the image contains fewer relevant regions. State the observed scope instead.

## 3. Create fresh crops

Use the source raster and include enough context to verify position, direction, overlap, and scale. For tiny details, make both context and close crops.

Prefer:

```bash
python3 scripts/make_audit_crops.py \
  --input /absolute/path/to/source.png \
  --regions /absolute/path/to/regions.json \
  --out-dir /absolute/path/to/audit-crops
```

Use normalized boxes `[left, top, right, bottom]` between `0` and `1`.

Inspect every generated crop. A generated crop is not evidence until viewed.

## 4. Verify proportions

Apply the full object-occupancy checks below in reconstruction. In style_transfer, verify only measurements used as evidence for transferable rules; do not require a source-object census or export source coordinates as target constraints. Numerical precision is not evidence of measurement: use tool-derived bounds/segmentation when available, otherwise label estimates or leave values unresolved.

- Use source dimensions.
- For the primary subject and every major object, verify normalized center, bounding-box limits, width and height spans, and canvas-area occupancy against the full frame.
- Keep visible silhouette area separate from bounding-box area. Do not use the bounding-box percentage as the object's actual filled-area percentage.
- When all bounding-box values are measured, cross-check that its area fraction agrees with width fraction multiplied by height fraction and that left ≤ right and top ≤ bottom.
- Use rotated object axes for tilted objects.
- Compare length with length and thickness with thickness.
- Distinguish visible projection from inferred hidden geometry.
- Label values as measured, estimated, or unresolved, and qualify measurements affected by crop, perspective, or occlusion.

## 5. Verify direction

Check independently:

- screen projection;
- near/far endpoint assignment;
- visible side planes;
- edge convergence;
- scale change;
- face orientation;
- content direction.

Do not infer depth from overlap alone.

## 6. Verify hidden shapes

Mark:

- visible;
- geometrically inferred;
- semantically inferred;
- unresolved.

Never claim exact hidden texture, text, damage, or hardware without evidence.

## 7. Reconcile the full frame

After local checks:

1. reopen the full image;
2. scan top-to-bottom and bottom-to-top;
3. recheck counts, hierarchy, axes, color roles and distribution, density, and layer order;
4. confirm that local findings remain valid globally;
5. rewrite corrected conclusions;
6. ensure no short global conclusion overstates a local feature.

Verify density rhythm separately at full-frame, thumbnail, and mildly blurred views. Recheck the largest quiet field, its continuity and interruptions, density-peak count, cluster separation, transition direction, breathing gaps, and clean areas inside the primary subject. Treat an edge-frequency or saliency map as supporting evidence only; contrast, text, overlap, and semantic grouping also affect perceived density.

Verify the object-modeling system separately through representative objects and likely counterexamples. At normal size, check shape grammar, mass hierarchy, line functions, material cues, and local exceptions. At thumbnail and mild blur, check the dominant modeling mode and value masses. In grayscale, check value-plane count, span, contrast, and area relations. Recheck highlight, shadow, cast-shadow, specular, reflection, transparency, ambient-occlusion, gradient, and microdetail claims against their actual footprint. Distinguish canvas-density spill from object-internal over-modeling.

Verify the visual-layering system separately. At normal size, check decisive contour terminations, local front/rear relations, relation reversals, masks, clipping boundaries, shared borders, transparent overlays, and outline redraw. Compare bounding-box occupancy, visible silhouette, inferred full envelope, visible fraction, fragment count, and protected identity cues for the primary subject, major objects, and compositionally important small front elements. At thumbnail and mild blur, check spatial-band separation, foreground interruptions, primary-subject exposure, and overlap-cluster readability. Mark exact production order unresolved when the source is flattened and no editable structure supports it.

Verify the color relationship system separately. At full-frame scale, check role locations, area balance, and warm/cool/neutral allocation. At thumbnail scale, check that major masses remain separated and accents remain bounded. Use grayscale to check the value ladder where relevant; hue-based separation and source-supported lost edges may merge there. In an adjacency or simplified flat-color view, check important touching pairs against their intended separation or blending behavior. Seek a counterexample to each global color rule and mark quantitative claims as measured, estimated, or unresolved. Do not let a color name or scene mood substitute for pairwise relationships.

Verify visual organization independently. At thumbnail size, confirm first-read order and major weight balance. At full-frame size, confirm the intended path, motif cadence and mutation, narrative-device function, semantic-group membership, and connectors. Reclassify the illustration when the selected subtype lacks global support or a supporting type contributes no distinct rule.

For style_transfer, also check that each established rule has visible support, a stated transfer scope, and explicit exceptions. Separate source-specific observations from general rules and hypotheses. Test whether the reusable wording specifies treatment of new subject structure rather than retaining source nouns. Confirm that target content is classified as required, candidate, or incidental; included secondary elements have appropriate story/group and visual roles, with cluster, layer, color, and visibility assignments expanded where they affect the task; and excluded candidates do not leak into the prompt. Confirm that target mapping uses role-based layer grammar instead of literal source IDs or coordinates, and that protected identity cues remain exposed. For consequential capacity controls, confirm bounds, estimation tolerance, allocations, and actual overflow decisions. All candidates may remain when their combined load fits. Confirm that the prompt follows the ranked visual core in generation-blueprint-schema.md and that object/material names have applicable local rendering qualifications without unsupported expansion. Do not require a universal execution contract or irrelevant quiet-space floors. Confirm that palette mode follows the user's instruction and defaults to `preserve_source` when no color direction was supplied. Confirm that prompt rules come only from the shared system and loaded subtype modules. A source audit verifies observations, not generated outcomes; track generation validation independently using generation-validation.md.

## 8. Default disclosure

Do not show:

- crop lists;
- sample matrices;
- claim ledgers;
- repeated evidence;
- internal confidence bookkeeping.

Show only:

- precise conclusions;
- decisive exceptions;
- unresolved items that affect reproduction.
