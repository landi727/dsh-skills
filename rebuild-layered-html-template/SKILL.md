---
name: rebuild-layered-html-template
description: Rebuild a supplied flat poster, long image, editorial graphic, or generated design into a PSD-style layered, locally runnable HTML and CSS template. Use when the user wants editable text, separable background, texture, imagery, paper, decoration, vector, logo, or guide layers while keeping the exact source image as the visual reference. Exclude style-only analysis, new visual-direction generation, general websites, and Canva-only or Figma-only reconstruction.
---

# Rebuild Layered HTML Template

## Repository Contract

**Type**: Workflow (Creative / Visual Production).

**Trigger**: Use when an exact supplied flat visual must become a layered, editable HTML and CSS file package that runs locally and remains traceable to that source.

**Responsibility**: Reconstruct supplied flat visuals as PSD-style HTML + CSS layers, with editable text, replaceable local assets, explicit layer metadata, and visual traceability to the exact source.

**Boundary**: Do not invent a new visual direction, build an editor application, add a backend, publish a site, import into Canva or Figma, or claim recovery of unavailable source layers. Do not recreate proprietary brand characters or logos through generative approximation.

**Input Contract**: Obtain the exact source image for every target page, target canvas dimensions or source-size rule, required editable fields, fixed logo or brand zones, and output location. Use current conversation files before asking. A style description without the actual source does not support fidelity claims.

**Output Contract**: Deliver standalone `index.html`, CSS, local assets, the preserved source reference, `template-manifest.json`, brief editing notes, and a packaged folder when useful. Every meaningful layer must be addressable through `data-layer`, `data-module`, or `data-field`.

**Failure Handling**: Stop for a missing exact source or an unresolved frozen-brand conflict. Record unavailable fonts and irreducible flattened regions. When visual rendering is unavailable, run structural checks, label visual QA unverified, and never describe the package as fully verified.

**Validation**: Run `scripts/check_layered_package.py`, open the package through `file://`, render at the target canvas, and compare it with the preserved source at whole-page and detail scales.

**Stop Condition**: Finish when requested files exist, local-resource checks pass, target canvas and layer order are confirmed, and visual QA either passes or has one precise reported blocker.

**Reuse Scope**: Flat-to-editable reconstruction for posters, fixed-screen graphics, covers, long-image pages, and editorial layouts across brands.

**Maturity**: Level 0 Draft. Extracted from one real long-image production run and structurally back-tested; independent full-flow evaluation and browser-verified revision remain pending.

## Outcome

Produce an editable reconstruction whose hierarchy and composition remain grounded in the exact supplied source. Preserve the source inside the package as a locked comparison reference. Separate elements according to a practical PSD layer panel.

Read [references/layer-model-and-qa.md](references/layer-model-and-qa.md) before planning assets or writing HTML. It defines source locking, representation choices, layer order, image-edit constraints, file contract, and comparison method.

## Workflow

### 1. Lock the source and production frame

Inspect the exact target image at original detail. Record its path, dimensions, aspect ratio, page role, and immutable brand zones. Copy it into the output package under `references/` before deriving assets.

Use the user's explicit canvas. Otherwise preserve source dimensions. Normalizing a near-match to a requested export size is allowed only when disclosed, such as 992 × 1586 to 1000 × 1600.

Do not replace the selected target with another conversation image, a previous generation, or a text-only style summary.

### 2. Build the layer and representation plan

Inventory visible elements from back to front, including occluded and repeated parts. Assign every element to the standard eight-layer model in the reference.

Choose the smallest faithful representation:

- DOM text for ordinary editable copy.
- CSS for solid fills, rules, grids, dots, tape, simple frames, crop marks, rulers, and basic geometric decoration.
- SVG for reusable line art, contours, irregular vectors, or exact scalable marks.
- PNG or WebP for photos, maps, grain, torn materials, shadows, and complex printed texture.
- Exact supplied PNG or SVG for logos, custom lettering, and brand characters.

Record elements that remain raster composites. Editable reconstruction does not imply perfect source-layer recovery.

### 3. Derive assets without duplicating layers

Prefer deterministic cropping, masking, vector redraw, and CSS reconstruction. Use image generation or editing only for clean-background recovery, object removal, cutouts, texture repair, or similarly material tasks.

Every generative edit must include the exact source image in that call and state what may change and what must remain invariant. Inspect each output before using it. Copy accepted outputs into the project; never leave project assets only in a generator's default folder.

Keep generated full-page results out of the final composition. Use them only as derived asset sheets or layer materials. When an accent, tape, text, or symbol will be recreated in CSS or SVG, remove it from the raster underneath first. This prevents baked-in and editable copies from appearing together.

### 4. Rebuild the page

Use plain HTML + CSS and local relative paths by default. Keep the target canvas exact and visually stable. Fixed posters may use absolute positioning; flexible body sections should use normal document flow and the modular longform workflow instead.

Use explicit stacking and semantic hooks. Include:

- A pure base-color layer beneath all texture.
- Independent texture and imagery layers.
- Separate papers, photos, tape, decorations, vectors, text, logo, and guide layers.
- `contenteditable` or clearly marked `data-field` nodes for requested text.
- A hidden source-reference overlay for alignment checking.
- A hidden logo or safety-area guide when required.

Do not use iframes, remote fonts, CDNs, hosted images, runtime HTML includes, or remote URLs. Avoid JavaScript unless the user requested an actual interaction.

### 5. Verify through evidence

Run the package checker:

```bash
python3 scripts/check_layered_package.py /absolute/path/to/package
```

Render `index.html` with a browser or Playwright at the target canvas. Compare the whole composition, then inspect title geometry, major overlaps, whitespace, image crops, paper edges, text legibility, accent duplication, logo protection, and footer alignment. Use the source overlay to tune coordinates.

Correct visible drift before delivery. When browser rendering is blocked, keep the reference overlay and report that screenshot comparison remains unrun.

### 6. Deliver

Deliver actual files, not only code snippets, screenshots, or prompts. Keep editing instructions short and identify where text, style tokens, images, and reference overlays live. Package the folder as ZIP for transfer when appropriate.

Do not upload, publish, or import the result into another design platform without explicit authorization.
