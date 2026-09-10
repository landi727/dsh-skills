# Camera, Geometry, Proportion, and Orientation

## Contents

1. Visible camera result
2. Direction types and endpoint pairs
3. Geometry skeleton and anchor proportions
4. Perspective consequences
5. Composition skeleton

## 1. Describe the camera through visible results

Keep one screen-relative coordinate convention for the whole scene. Preserve visible mixed or conflicting projections rather than imposing a physical camera. For coherent perspective, use natural-language camera properties by default:

- frontal, three-quarter, side, top, or bottom emphasis;
- eye-level, slightly high, high, slightly low, or low view;
- front face, left side, right side, top, or underside visibility;
- near-orthographic, weak, ordinary, strong, or wide-angle perspective;
- full view, medium framing, close framing, or deliberate crop.

Do not require azimuth, elevation, focal length, or field of view unless the source supports them or the user requests a technical scene specification.

For flat or contradictory illustration, state that no unique physical camera is recoverable and describe only the visible projection.

## 2. Separate four kinds of direction

Do not use one “direction” field for all of these:

1. **Screen projection:** where the object's long axis appears to travel across the image.
2. **Depth trajectory:** toward the viewer, away into the scene, parallel to the image plane, or ambiguous.
3. **Face orientation:** which surface faces the viewer and which edge is nearer.
4. **Content direction:** where an arrow, gaze, figure, or printed symbol points.

Clock directions may describe screen projection only. They never encode depth.

## 3. Use endpoint pairs

For each elongated or directional object, describe:

- connection or start endpoint;
- outer or end endpoint;
- each endpoint's screen position;
- each endpoint's near, far, equal, or uncertain depth role;
- projected path between them;
- depth change between them;
- near/far size change;
- edge convergence;
- foreshortening;
- visible faces;
- self-occlusion and overlap with other objects.

Prefer “connection endpoint” and “outer endpoint” over the technical term “free end” unless the term has already been defined.

The connection endpoint is not automatically near or far. Either endpoint may be closer to the viewer.

## 4. Build the geometry skeleton before appearance

Register all important objects without color, material, or decoration first.

For each object, record:

- identity and role;
- visual center;
- projected length;
- projected thickness;
- visible area or visual mass when useful;
- local axis;
- attachment point;
- endpoint pair;
- visible faces;
- frame contact and crop.

Use rotated bounding geometry for tilted objects. An axis-aligned box alone exaggerates the size of diagonal objects.

## 5. Use one anchor for proportion

Select a primary object as anchor `A` when possible.

Express:

- `B` length relative to `A` length;
- `B` thickness relative to `A` thickness;
- `B` visible area relative to `A` visible area;
- center-to-center distance in units of `A` width or length;
- attachment height as a fraction of `A`.

Do not say “B's position is 1.5 times A.” Position is not a scalar. State the direction and distance of the offset.

Avoid chains such as `C` relative to `B`, then `D` relative to `C`. Relate important objects directly to the anchor or canvas.

Distinguish projected visible proportion from real-world physical proportion. A single image can measure the former; the latter may be unrecoverable.

## 6. Describe perspective through visible consequences

Translate depth into:

- which endpoint is near or far;
- which endpoint is larger or smaller;
- where long edges converge;
- which side plane becomes visible;
- what overlaps what;
- how much the long axis is foreshortened.

Do not rely on raw XYZ coordinates alone in a generation prompt.

## 7. Composition skeleton

Conclude:

- primary and secondary axes;
- center of gravity;
- large, medium, and small masses;
- density and quiet zones;
- negative-space distribution;
- repeated directions;
- frame crossings and crops;
- whether objects radiate, stack, cross, alternate, or form a grid.
