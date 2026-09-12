# Production Intake and Legibility Gate

## Contents

1. Classify the task
2. Confirm the output form
3. Branch by production context
4. Request and qualify references
5. Confirm content and assets
6. Establish legibility constraints
7. Return a constraint confirmation sheet
8. Follow the required production order
9. Stop on hard failures

## Purpose

Confirm the real use context before designing. Do not generate a final visual while the medium, placement, dimensions, viewing conditions, references, or legibility constraints remain materially unknown.

Ask in the user's language. Ask only for missing information.

## 1. Classify the task

Identify whether the user wants:

1. reference analysis or layout rules;
2. a structural wireframe;
3. generated visual assets;
4. a finished composition.

Proceed directly for analysis-only work, while labeling missing evidence. Enforce the full gate for items 2–4.

## 2. Confirm the output form

If absent, ask:

> Is the intended output a webpage, long image, poster, or another material?

Do not assume that every visual-design request is a long image.

## 3. Branch by production context

### Webpage

Confirm:

- page type: homepage, landing page, campaign page, feature page, dashboard, or other;
- primary device: mobile, desktop, or responsive;
- publishing platform or technical environment;
- viewport, first-screen, or content-width constraints;
- need for real HTML text, interaction, motion, and responsive behavior;
- whether the design is standalone or embedded in an existing site;
- existing design system, brand rules, or development constraints.

Keep body copy, buttons, navigation, and important labels as real page elements. Never flatten a substantive webpage into one raster image.

### Online long image

Confirm:

- exact platform, such as WeChat, Xiaohongshu, Weibo, Zhihu, Douyin, or a website;
- placement: article body, cover, feed, detail page, or campaign page;
- source canvas width and target or flexible height;
- actual display width, cropping, and compression;
- primary reading device;
- whether segmented publishing is allowed;
- required PNG, JPG, PDF, SVG, or editable source.

Do not reuse one type scale across platforms without recalculating display scale.

### Online poster

Confirm:

- exact platform;
- placement: cover, feed, splash, banner, campaign visual, or share card;
- required aspect ratio and safe zones;
- likely platform crop;
- primary viewing device;
- required alternative ratios.

### Offline material

Confirm:

- material: poster, display board, roll-up banner, lightbox, brochure, booklet, packaging, or other;
- final physical dimensions;
- orientation;
- typical viewing distance;
- installation or handling environment;
- print material and process;
- printer requirements for color mode, resolution, and bleed;
- editable production-file requirement.

Judge typography at physical size and viewing distance, not from an enlarged screen preview.

## 4. Request and qualify references

Ask the user to upload images, a ZIP archive, or accessible links. Confirm:

- which references have the highest priority;
- whether all references are deep references;
- what to borrow: layout, density, hierarchy, palette, material, image style, components, or overall mood;
- what must not be used;
- whether multiple references may be synthesized.

Inspect every available reference. Do not reduce a reference set to style keywords before examining the actual compositions.

If the user has no references:

1. record `no reference images`;
2. offer two or three proposed directions;
3. ask the user to choose or authorize a recommendation;
4. never claim the result was extracted from references.

## 5. Confirm content and assets

Confirm:

- final copy or estimated copy volume;
- title, subtitle, body, data, and call to action;
- required images, logos, and brand assets;
- number and purpose of newly generated images;
- font, color, brand, and prohibited-use rules;
- delivery formats;
- future editing requirements.

If final copy is unavailable, use a structural draft with clearly labeled body and image placeholders.

## 6. Establish legibility constraints

### Webpage

- Start mobile body text at no less than `16 CSS px` unless the context justifies a larger minimum.
- Start body line height around `1.45–1.75`.
- Limit readable text-column length rather than allowing unrestricted full-width paragraphs.
- Test required mobile and desktop breakpoints.
- Resolve overflow through copy, width, hierarchy, or page length before reducing body text.

### Online raster long image or poster

Calculate source-file type size from the expected display scale:

`source font px >= target displayed px × source canvas width / actual display width`

Example:

- source width: `1000px`;
- actual phone display width: `375px`;
- target displayed body size: `16px`;
- source body size: `16 × 1000 / 375 ≈ 43px`.

Do not describe `28px` text on a `1000px` source as `28px` to the viewer when the platform scales the entire image down.

Check:

- displayed body size;
- title-to-body ratio;
- line and paragraph spacing;
- labels inside images;
- density;
- phone-scale thumbnail;
- clarity after platform compression.

### Offline material

- Base hierarchy on physical size and typical viewing distance.
- Preserve continuous body readability for handheld materials.
- Make supporting information readable at the intended distance for near-view posters.
- Reduce paragraph volume and increase scale and contrast as viewing distance grows.
- Test through actual-size print, tiled proof, or a scale simulation.
- Never solve overflow by proportionally shrinking the entire composition.

Confirm resolution, bleed, color mode, and production tolerances with the printer when those values are not supplied. Treat generic print settings as recommendations, not confirmed vendor requirements.

## 7. Return a constraint confirmation sheet

Before creating a wireframe or generating images, return:

```text
Output form:
Online or offline:
Platform or material:
Placement:
Canvas or physical dimensions:
Primary device or viewing distance:
Estimated copy volume:
Minimum readable body size:
References and priority:
Invariant layout DNA:
Replaceable visual skin:
Recommended and alternative palette:
Required assets:
Forbidden elements:
Delivery formats:
Unresolved items:
```

Then ask the user to confirm the constraints.

Do not generate the final visual before confirmation. If the user explicitly requests defaults and immediate execution, list every default first and proceed only within those disclosed assumptions.

## 8. Required production order

1. confirm output form;
2. confirm platform or offline material;
3. confirm dimensions, device, or viewing distance;
4. obtain and inspect references;
5. analyze copy and assets;
6. establish grid, typography, palette, and legibility constraints;
7. return the confirmation sheet;
8. obtain confirmation or explicit authorization for stated defaults;
9. design the complete structural draft;
10. confirm the macro layout;
11. generate independent visual assets;
12. compose with real text;
13. test at actual display scale or viewing distance;
14. export the final deliverables.

Do not reverse this into “generate the whole visual first, then fit the copy.”

## 9. Hard failures

Stop before final delivery if:

- the output form is unknown;
- the exact online placement or offline context is unknown;
- final dimensions or display scale are unknown;
- references were not requested;
- layout DNA and visual skin were not separated;
- typography was not checked against device scale or viewing distance;
- body copy was repeatedly reduced to solve overflow;
- final generation began before constraint confirmation;
- a raster model generated substantial non-editable body text;
- the work was checked only at enlarged source size, not in its real use context.
