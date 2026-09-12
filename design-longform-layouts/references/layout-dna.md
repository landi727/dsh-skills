# Transferable Long-form Layout DNA

## Contents

1. Fixed and variable layers
2. Proportional grid
3. Narrative skeleton
4. Density waveform
5. Module-width families
6. Section anatomy
7. Image hierarchy
8. Controlled asymmetry
9. Typography hierarchy
10. Container system
11. Repetition and variation
12. Quality gate
13. Compact production brief

## 1. Fixed and variable layers

| Preserve as layout DNA | Replace as visual skin |
|---|---|
| strong opener | palette |
| sectioned narrative | font personality |
| density waveform | surface material |
| image-to-text rhythm | image-making style |
| controlled asymmetry | icon language |
| module-width families | decorative motifs |
| overlap and bleed logic | brand elements |
| numbering and metadata | world-building symbols |
| repetition and variation cadence | borders, corners, and shadows |

Changing the right column must not destroy the relationships in the left column.

## 2. Proportional grid

Use these as recommended defaults when references do not provide measurable values.

For canvas width `W`:

- outer margin: `0.064W`, adjustable within `0.055W–0.08W`;
- 12 columns;
- gutter: approximately `0.016W`;
- base spacing unit: approximately `0.008W`;
- normal module gaps: `3u`, `4u`, `6u`, `8u`, or `12u`;
- major section gaps: `12u–20u`.

For `W = 1000px`:

- outer margins: `64px`;
- content width: `872px`;
- gutters: `16px`;
- columns: `58px`;
- base unit: `8px`;
- common gaps: `24, 32, 48, 64, 96px`;
- major section gaps: `96–160px`.

Align primary modules to the grid. Allow images, labels, rules, and decorative elements to break it selectively.

## 3. Narrative skeleton

A complete long image should normally contain these roles:

1. **Opener** — establish topic, identity, and visual promise.
2. **Orientation** — provide abstract, context, navigation, or key facts.
3. **Development** — unfold the main content through varied modules.
4. **Evidence** — show images, records, data, comparisons, or details.
5. **Climax** — create the strongest scale, contrast, or compositional shift.
6. **Breathing section** — reduce density after the climax.
7. **Resolution** — conclude, summarize, sell, or request action.
8. **Closing mark** — finish with restrained metadata or branding.

Do not force all eight into separate sections. A section may fulfill two adjacent roles.

## 4. Density waveform

Avoid uniform density. Use a waveform such as:

`high → medium → low → high → medium → low`

Trigger a visible compositional change every `0.6W–1.1W` of vertical distance:

- module width;
- image scale;
- column structure;
- background value;
- container type;
- whitespace;
- alignment axis.

Change one or two variables at a time. Changing all variables at every interval destroys unity.

After a climax, add a lower-density region before the next information-heavy section.

## 5. Module-width families

Prefer a limited family:

- `12` columns — full-width anchor or section opener;
- `8 + 4` — primary narrative plus supporting evidence;
- `7 + 5` — image and text relationship;
- `6 + 6` — two peers;
- `4 + 4 + 4` — records, facts, or comparisons;
- centered `8–10` columns — quote, abstract, or conclusion.

Do not use the same width and alignment for three consecutive major modules.

Avoid a page composed only of equal cards. Equal size implies equal importance.

## 6. Section anatomy

Give every major section:

1. one dominant anchor;
2. one primary information module;
3. one to three supporting modules;
4. one metadata family;
5. one transition to the next section.

The dominant anchor must be visibly stronger than the support modules by scale, contrast, position, or whitespace.

Possible anchors:

- section title;
- dominant image;
- oversized number;
- diagram;
- quote;
- data point;
- color or value field.

## 7. Image hierarchy

- Use no more than one dominant image per major section.
- Let a dominant image span `7–12` columns or occupy a clearly superior area.
- Keep secondary images around `2–4` columns unless they form an intentional sequence.
- Avoid three similarly sized images competing on the same screen.
- Specify aspect ratio, crop, subject position, and text-safe zone before generating an image.
- Use full bleed, controlled crop, or `24–80px` overlap to integrate images into layout.
- Add captions, labels, coordinates, and important annotations as real layout text.

## 8. Controlled asymmetry

Allow:

- uneven columns;
- left-right offsets;
- edge labels;
- image bleed;
- one main overlap per screen;
- a section number crossing two modules;
- limited tilted inserts.

Constrain:

- overlaps must not reduce text legibility;
- tilted elements should remain below roughly 20% of major modules;
- decorative elements must not become accidental focal points;
- every intentional offset should still relate to a grid line, edge, or neighboring module.

## 9. Typography hierarchy

Maintain at least six semantic levels:

1. long-image title;
2. section title;
3. module title;
4. body;
5. caption or support text;
6. metadata.

For long-form editorial images, use body text as `1.0` and begin with these ranges:

| Level | Ratio |
|---|---:|
| long-image title | `2.00–2.60` |
| section title | `1.45–1.85` |
| module title | `1.15–1.35` |
| body | `1.00` |
| caption | `0.82–0.92` |
| metadata | `0.70–0.82` |

For a `1000px` source displayed around `375px` wide, begin with:

| Level | Source size |
|---|---:|
| long-image title | `82–108px` |
| section title | `58–74px` |
| module title | `46–54px` |
| body | `38–43px` |
| caption | `32–36px` |
| metadata | `28–32px` |

Start near the middle of each range rather than automatically using the maximum.

Use these line-height ranges:

| Level | Line height |
|---|---:|
| long-image title | `0.95–1.10` |
| section title | `1.05–1.20` |
| module title | `1.15–1.30` |
| body | `1.50–1.70` |
| caption | `1.35–1.50` |
| metadata | `1.20–1.40` |

Let `L` equal the body line height. Coordinate local vertical spacing:

| Relationship | Spacing |
|---|---:|
| module title to body | `0.5–0.8L` |
| body paragraph to paragraph | `0.7–1.0L` |
| image to caption | `0.4–0.6L` |
| section title to first module | `1.2–2.0L` |
| previous section to new title | `3–5L` |
| main title group to first content module | `2–3L` |

Preserve the grid, module gaps, major-section gaps, and density waveform when applying this scale. Do not shrink the title while leaving poster-sized empty space around it.

Prefer weight, whitespace, alignment, color, or image relationships before increasing title size. Give each section only one highest-contrast element. If the image is the anchor, reduce the title's weight; if the title is the anchor, subordinate oversized numbers, English decoration, and accents.

Limit the long-image title to two lines in normal use. Do not let the long-image title exceed `2.6×` body or a section title exceed `1.85×` body without a clear, reference-supported compositional reason. Do not use oversized titles to open every section.

Adjust final sizes through actual-display mobile tests. Do not reduce body text to solve a height problem before revising copy, module width, spacing, or canvas height.

Font personality belongs to the skin; semantic hierarchy, spacing, and contrast belong to the DNA.

## 10. Container system

Use three to five functional container families:

- narrative text;
- visual evidence;
- data or structured record;
- quote or emphasis;
- metadata;
- action or product.

Translate containers by style:

| Function | Archival | Terminal | Minimal | Magazine |
|---|---|---|---|---|
| narrative | document page | reading pane | open text field | editorial column |
| evidence | numbered plate | data viewport | borderless figure | clipped image |
| record | form or ledger | system panel | ruled table | labeled block |
| quote | note or letter | log excerpt | oversized statement | pull quote |
| metadata | stamp or file code | status and timestamp | small label | sticker or barcode |

The container's function remains stable even when its appearance changes.

## 11. Repetition and variation

Repeat at least three unifying devices:

- numbering system;
- alignment axis;
- rule or border logic;
- metadata syntax;
- spacing cadence;
- caption treatment.

Create variation through module ratio, density, image scale, or background value. Do not invent an unrelated component language for every section.

## 12. Quality gate

Score the result before delivery:

| Dimension | Weight |
|---|---:|
| narrative structure | 20 |
| hierarchy and focal control | 20 |
| density and pacing | 20 |
| grid and module relationships | 15 |
| fidelity to reference layout DNA | 15 |
| readability and production safety | 10 |

Target at least `80/100`.

Hard failures requiring revision:

- the result copies only the reference's colors or texture;
- every section uses the same card template;
- all modules have equal visual weight;
- the page has no clear climax or breathing region;
- generated raster text replaces substantial real copy;
- style changes also destroy the layout skeleton;
- references were reduced to keywords without inspecting the images;
- an invented measurement is claimed as extracted from a reference;
- body text is made unreadably small to fit a fixed height;
- the main title exceeds `3×` body or a section title exceeds `2×` body without a clear reason;
- every section relies on oversized type for differentiation;
- title size and color both compete with the intended visual anchor.

## 13. Compact production brief

Use this block when directing another design or generation stage:

```text
Preserve the reference set's layout DNA rather than its subject matter or surface style.

Keep:
- strong opener and sectioned narrative;
- 12-column controlled asymmetric grid;
- high-medium-low density waveform;
- one dominant anchor per section;
- alternating full-width, 8+4, 7+5, 6+6, and centered modules;
- varied text, image, evidence, quote, and metadata containers;
- controlled overlap, bleed, crop, and offset;
- recurring numbering, caption, and metadata systems;
- a body-anchored type scale with coordinated vertical spacing;
- visible variation without forming a style collage.

Replace as required:
- palette, type personality, material, image style, iconography, decoration,
  brand elements, and world-building symbols.

Build the complete structural draft before refining image assets or filling all body copy.
```
