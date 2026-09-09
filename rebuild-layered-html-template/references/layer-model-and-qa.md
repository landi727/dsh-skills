# Layer Model and QA

Read this reference before asset preparation and again during final verification.

## Source lock

Create one source record per page:

| Field | Record |
| --- | --- |
| Source ID | Stable filename or user-provided identifier |
| Role | Exact edit target, secondary reference, or supplied brand asset |
| Original size | Pixel width and height |
| Target size | Requested export width and height |
| Scale rule | Preserve, proportional fit, crop, or disclosed normalization |
| Frozen regions | Logo, QR, character, legal copy, or safety zone |
| Allowed derivations | Crop, mask, clean background, cutout, texture repair |

The exact edit target remains the authority for composition and visual evidence. Secondary references may clarify hidden details; they do not replace it.

## Standard layer stack

| Order | Layer | Typical contents |
| --- | --- | --- |
| 01 | Solid base | One editable color or controlled gradient |
| 02 | Texture | Grain, fibers, stains, subtle grid, wear |
| 03 | Background imagery | Map, illustration, environmental image, large pattern |
| 04 | Papers and media | Documents, cards, photos, files, torn sheets |
| 05 | Attached decoration | Tape, clip, sticker, pin, stamp, scraps |
| 06 | Graphic system | Lines, frames, scale marks, barcode, dots, contours, accent blocks |
| 07 | Text and information | Title, labels, body copy, indices, captions |
| 08 | Brand and guides | Exact logo or character assets, safe area, crop marks, hidden reference overlay |

The source may require multiple sublayers inside one group. Preserve occlusion order explicitly; never rely on DOM accident.

## Representation decisions

| Evidence in source | Preferred output | Reason |
| --- | --- | --- |
| Uniform color field | CSS variable and element | Fast global editing |
| Lines, boxes, grids, dots, tape | CSS | Precise, lightweight, editable |
| Contours or complex line art | SVG | Scalable and recolorable |
| Ordinary title and copy | DOM text | Direct editing and accessibility |
| Logo or custom distorted lettering | Exact PNG or SVG | Prevents font substitution drift |
| Photo, map, rich illustration | Independent raster | Preserves visual detail |
| Paper grain or torn material | Raster texture plus CSS geometry | Separates material from shape |
| Irrecoverable overlap | Small disclosed raster composite | Avoids false editability claims |

Avoid cutting every visible object into an opaque rectangle. Opaque crops can erase lower layers and create seams. Prefer clean cutouts, clipping paths, or a small composite region whose limitation is recorded.

## Asset derivation order

1. Preserve the untouched source under `references/`.
2. Recover the clean base texture when foreground objects prevent reuse.
3. Crop or isolate complex photos, maps, illustrations, and brand assets.
4. Remove baked-in elements that will be recreated separately.
5. Rebuild deterministic shapes with CSS or SVG.
6. Inspect derived assets at original detail and in position.

### Generative-edit prompt frame

Use this only when deterministic extraction cannot produce a usable layer:

```text
Use case: precise-object-edit
Asset type: layer asset for editable HTML/CSS reconstruction
Input image: Image 1 is the exact edit target and sole visual source.
Primary request: change only <named region or object> to produce <specific layer material>.
Invariants: preserve canvas, composition, geometry, palette, lighting, texture scale and every unlisted element.
Constraints: no new objects, no text changes, no logo changes, no watermark.
```

For a clean base, list every foreground family to remove. For accent removal, name each color and location. Re-state invariants on every retry.

Never ask a generator to recreate an exact brand logo, licensed character, QR code, or small legal text. Preserve supplied pixels or use a clearly labeled replacement slot.

## Portable package

Use the narrowest useful form:

```text
layered-template/
├── index.html
├── styles.css
├── assets/
├── references/
│   └── source-reference.png
├── template-manifest.json
└── EDITING.md
```

Split styles into `styles/tokens.css` and `styles/layers.css` only when scale justifies it. Keep image paths relative. `index.html` must open through `file://` without a build step.

The manifest should contain canvas dimensions, source reference, ordered layer selectors, editable fields, fixed regions, local assets, known approximations, and guide or reference-overlay controls.

## Visual comparison

Render at the exact target pixel size. Review in this order:

1. Silhouette and dominant mass placement.
2. Main title scale, width, baseline, and negative space.
3. Paper and photo overlap and depth order.
4. Image crop, contrast, and texture scale.
5. Accent color location and duplication.
6. Repeated line rhythm, grids, rulers, and footer geometry.
7. Logo, QR, or character fidelity and protection zones.
8. Edge seams, unexpected opaque rectangles, clipping, and overflow.

Use a hidden `.reference-overlay` layer with the exact source stretched according to the declared scale rule. Toggle it at partial opacity to expose drift.

## Verification status

- **PASS**: Structural checks pass and browser comparison shows no material drift.
- **PARTIAL**: Files and local resources pass; a named visual substitution or unavailable font remains.
- **UNVERIFIED**: Browser rendering or source access was unavailable. Do not use the word “verified”.
- **FAIL**: Missing files, remote dependencies, wrong canvas, duplicate baked-in elements, protected-zone violations, or material visual mismatch.

Record the smallest actionable blocker. Avoid compensating for blocked rendering with unsupported confidence.
