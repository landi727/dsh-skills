---
name: rebuild-layered-canva-template
description: Rebuild a supplied flat poster, long image, editorial graphic, or reference design into a PSD-style layered, Canva-editable PDF/template. Use when the user asks to separate a finished image into editable background, texture, image, decoration, vector, text, logo, or safety-area layers and import or prepare it for Canva. Do not trigger for ordinary image generation, simple resizing, or a flattened PDF export.
---

# Rebuild Layered Canva Template

Reconstruct the supplied design as an editable object tree while preserving the original image as the visual source of truth.

Read [references/layer-model-and-qa.md](references/layer-model-and-qa.md) before creating the layer manifest, rebuilding the page, exporting the PDF, or importing it into Canva.

## Non-negotiable rules

- Use the exact user-selected source image. Never substitute a similar image or another image from the conversation.
- Attach the exact source image to every image-generation or image-edit call. Do not generate from an extracted style description alone.
- Stop and request a new attachment when the exact source cannot be opened or passed to the image tool.
- Preserve the source canvas size and aspect ratio unless the user explicitly changes them.
- Reconstruct only what is visible or required for editing. Do not invent characters, brand assets, copy, or hidden artwork.
- Preserve logo placement and protection zones. Keep logos and typography that would deform in Canva as image or SVG layers.
- Respect analysis-only requests. Do not create, export, upload, or import files until the user asks.

## Workflow

### 1. Lock the source and canvas

Record the exact source path or attachment, pixel dimensions, page count, target Canva size, and any brand assets. Render or inspect the source before editing.

### 2. Build a layer manifest

Map every meaningful object to a named layer with:

- z-order;
- bounding box and rotation;
- representation: solid, vector, editable text, transparent raster, or guide;
- source crop or recreation method;
- expected Canva editability.

Use the default PSD-style order unless the source requires additional sublayers:

1. solid background;
2. texture and grid;
3. background maps or illustrations;
4. papers, files, photographs, and main image content;
5. tape and decoration;
6. accent colors, UI marks, frames, scales, and contours;
7. editable text and information;
8. logo and safety guides.

### 3. Choose the least destructive representation

- Recreate lines, boxes, dots, tape, grids, contours, and simple icons as SVG or native vector objects.
- Recreate ordinary text as editable text only after confirming a sufficiently close font and line metrics.
- Keep logos, custom lettering, distressed typography, and brand-critical text as transparent image or SVG layers when conversion could deform them.
- Isolate complex maps, photographs, torn paper, printed files, shadows, and material textures as cropped transparent PNGs.
- Use image editing only to recover occluded edges or clean transparent boundaries. Include the full source image in the edit call and preserve the original geometry.
- Flatten only a single complex visual effect when Canva cannot preserve its masks, blend modes, or filters. Keep that flattened effect in its own named layer.

### 4. Rebuild the page

Create an exact-size HTML/SVG or equivalent vector-first composition with local relative assets. Use absolute positioning for fidelity and stable z-order. Give every major object a human-readable layer name.

Keep the background color and texture separate. Keep independent objects separately movable. Add hidden guide layers for logos, QR codes, and protected content regions.

### 5. Export a Canva-oriented PDF

Export at the exact canvas size. Preserve text, SVG, and simple shapes as PDF objects. Avoid unsupported blend modes, nested masks, filters, external URLs, and iframe-based composition.

Treat “layered PDF” as a PDF containing separable page objects that Canva can reconstruct. Do not claim Photoshop-native layer compatibility.

### 6. Verify before Canva import

Render the PDF back to PNG at the exact source dimensions and compare it with the source. Check page size, object positions, cropping, title metrics, texture, logo safety area, and edge seams.

Correct visual discrepancies before upload. Import to Canva only when requested and only after the local PDF passes inspection.

### 7. Verify in Canva

Confirm that the imported page size is correct and that representative text, vector, image, accent, and guide elements can be selected independently. Check for merged layers, font substitution, transparent-edge halos, shifted crops, and flattened masks.

When Canva merges an unsupported effect, return to the source composition, simplify that effect, export again, and re-import. Do not report completion until the Canva design itself has been checked.

## Deliverables

Unless the user narrows the request, retain:

- Canva-oriented PDF;
- exact-size preview PNG;
- local source composition and assets;
- layer manifest;
- Canva design link after a verified import.

Report which elements remain editable text/vector and which remain raster image layers.

## Stop conditions

Stop and ask for user input only when:

- the exact selected source is unavailable;
- a required logo, font, or brand asset is missing and substitution would alter the design;
- Canva requests authentication, permission, or a destination choice;
- import verification shows unavoidable flattening that materially reduces editability.
