# Layer model and QA

## Default representation map

| Layer group | Preferred representation | Keep separate because |
|---|---|---|
| Solid background | Vector rectangle | Enables recoloring and guarantees clean page edges |
| Grain, fibers, faint noise | Transparent raster or compact SVG pattern | Preserves texture while keeping the base editable |
| Grid and contours | SVG | Enables recoloring and scaling |
| Background maps or illustrations | Transparent PNG/SVG | Enables replacement and repositioning |
| Papers and files | One transparent raster per independently moving object | Preserves tears, printing, shadows, and overlaps |
| Tape and simple decoration | SVG/native shape | Enables recoloring, rotation, and resizing |
| UI lines, scales, frames, dots | SVG/native vector | Preserves crisp edges and editability |
| Ordinary title and body copy | Editable text | Enables content changes |
| Logo and brand-critical lettering | Original SVG or transparent PNG | Prevents font and geometry deformation |
| Safety areas | Hidden vector guides | Preserves production constraints without appearing in export |

## Segmentation decisions

Use object boundaries and intended independent movement, not color similarity alone.

- Split two papers when they overlap or may be replaced independently.
- Keep a paper’s printed map attached to that paper when separating it would break perspective or material realism.
- Split tape from paper when it is a reusable decoration.
- Keep shadow with the object casting it when Canva cannot reproduce the blur reliably.
- Rebuild crop marks, registration crosses, scales, arrows, circles, and bars as vectors.
- Preserve transparent padding only when it is required for rotation, shadow, or exact alignment.

## Layer naming

Use numbered Chinese names that remain readable in Canva:

```text
01_纯色底
02_纹理
03_背景地图
04_纸张与文件
05_胶带与装饰
06_青橙图形与刻度
07_文字与信息
08_LOGO与安全区
```

Use object names such as `主地图纸张`, `右上地图`, `标题橙色斜杠`, and `LOGO安全区_默认隐藏` inside each group.

## Suggested project structure

```text
project/
  reference/
    source.png
  assets/
    texture.svg
    background-map.png
    main-paper.png
    tape.svg
  source/
    index.html
    styles.css
  export/
    canva-editable.pdf
    preview.png
  layer-manifest.json
```

All source URLs must be local relative paths.

## PDF and Canva constraints

- PDF does not guarantee Photoshop Optional Content Group behavior inside Canva.
- Canva reconstructs many PDF text, vector, and image objects, while masks, blend modes, filters, clipping chains, and some fonts may flatten or shift.
- Prefer independent SVG and image objects over one full-page raster.
- Avoid a single full-canvas texture image when a small repeating pattern produces the same appearance.
- Keep complex photographic collages as multiple transparent image objects rather than redrawing them inaccurately.
- Outline text only when the user values shape fidelity over text editing.

## Visual QA checklist

Before import:

- PDF page has the exact target size and orientation.
- Rendered PDF and source share the same major object bounding boxes.
- No seams appear between tiled image crops.
- No opaque rectangles appear around transparent paper or map layers.
- Title width, baseline, and line breaks match the source.
- Grain remains visible without changing the base color.
- Logo and QR protection zones remain unchanged.
- No external resource URL or iframe is present.

After Canva import:

- Page dimensions remain correct.
- Title or selected text can be edited without reflow damage.
- Simple vector accents can be recolored.
- Each complex paper/map object can be moved independently.
- Logo is selectable as one protected object.
- Hidden guides stay hidden or are placed on a clearly named guide layer.
- Exported Canva preview matches the verified local preview.

## Completion statement

State the exact page size and identify:

- editable text layers;
- editable vector layers;
- independent raster image layers;
- protected logo or guide layers;
- any effect Canva flattened during import.
