---
name: design-longform-layouts
description: Extract, formalize, transfer, and apply layout DNA across different visual styles and production contexts. Use when a user asks to analyze references, reproduce their composition or editorial feeling, create a reusable layout specification, turn references into a wireframe or production brief, or design a webpage, long image, online poster, or offline visual material without copying the reference's original colors, subject matter, materials, or brand skin.
---

# Design Longform Layouts

## Purpose

Turn reference long images into a transferable editorial layout system. Preserve composition, hierarchy, rhythm, density, and module relationships while allowing color, typography style, texture, imagery, brand, and world-building motifs to change.

Treat this skill as a composition director. Pair it with the appropriate image, document, presentation, SVG, frontend, or design tool when producing an artifact.

## Non-negotiable principles

- Analyze the reference images themselves, not only keywords derived from them.
- Separate invariant layout DNA from replaceable visual skin before designing.
- Preserve editorial relationships; do not copy proprietary logos, characters, symbols, or a reference's complete composition.
- Use real, editable text for titles and body copy. Do not ask a raster image model to render substantial body text.
- Build the page structure before generating illustrations or decorative assets.
- Run the production-intake gate before creating a wireframe, image asset, or finished design.
- Do not generate the final visual until the user confirms the production constraints, unless the user explicitly authorizes stated defaults.
- When references do not define a clear palette, derive color from content and use context, then use one compatible current trend signal only as a calibration.
- Distinguish rules observed in references from new recommendations. Never present invented measurements as observed facts.
- Maintain controlled variation. Repetition creates a system; contrast creates rhythm.

## Workflow

### 1. Run the production-intake gate

First classify the request:

- reference analysis or layout specification only;
- structural wireframe;
- image-asset generation;
- finished design production.

For analysis-only requests, proceed with the available references and identify missing evidence. For a wireframe, generated asset, or finished design, read and enforce `references/intake-and-legibility.md`.

Ask only for missing information. Do not repeat questions the user has already answered.

Confirm, as applicable:

- webpage, long image, poster, or other material;
- exact online platform and placement, or offline material and installation context;
- canvas or physical dimensions;
- main device or viewing distance;
- reference images and reference priorities;
- copy volume and required assets;
- editable-source and export requirements.

If references are unavailable, record that explicitly and offer two or three proposed directions. Never imply that an unreferenced recommendation was extracted from source images.

Before production, return a constraint confirmation sheet. Wait for confirmation unless the user explicitly asks to use disclosed defaults and proceed.

### 2. Audit the full reference set

Inspect every available reference. For each one, record:

- opening-screen composition;
- section boundaries;
- dominant and secondary module widths;
- text-to-image ratio;
- density changes;
- alignment axes;
- overlaps, bleeds, crops, and offsets;
- recurring metadata and navigation devices;
- container types;
- closing-screen behavior.

For multiple references, identify:

1. common rules present across the set;
2. useful variants;
3. isolated stylistic outliers.

Do not average incompatible references into a style collage. Use the common rules as the layout system and variants as optional section patterns.

### 3. Split DNA from skin

Create two explicit lists.

**Layout DNA — preserve**

- narrative sequence;
- grid and alignment logic;
- hierarchy;
- density waveform;
- dominant-image behavior;
- module width families;
- asymmetry and overlap rules;
- recurring metadata;
- repetition and variation cadence.

**Visual skin — replace**

- palette;
- font personality;
- surface material;
- illustration or photography style;
- icons and decorative motifs;
- brand and world-building symbols;
- border, corner, and shadow treatment.

If an item cannot be cleanly assigned, explain whether changing it would alter the composition or only its appearance.

### 4. Build the long-image skeleton

For a long-form composition, define the page as roles, not topic-specific scenes:

1. strong opener;
2. orientation or abstract;
3. content development;
4. evidence or detail modules;
5. visual climax;
6. breathing section;
7. conclusion, product, or action section;
8. restrained closing mark.

Assign each section:

- one dominant anchor;
- one primary information module;
- one to three supporting modules;
- one metadata family;
- a density level;
- a transition behavior.

Use the ratios and constraints in `references/layout-dna.md` as reference-derived measurements when measurable, otherwise as disclosed recommendations.

### 5. Map content to modules

Choose a container according to information function:

- exposition → text block or editorial column;
- evidence → image plate, record, table, diagram, or comparison;
- emphasis → quote, oversized statement, or isolated fact;
- sequence → timeline, numbered steps, or repeated records;
- metadata → label, code, date, coordinate, status, or caption;
- action → product, registration, download, or publishing block.

Use three to five container families across one long image. Do not make every section the same card with different content.

### 6. Apply the selected visual skin

Translate each functional container into the chosen style without changing its role. For example, the same evidence module may become:

- a paper plate in an archival style;
- a system panel in a terminal style;
- a borderless figure in a minimalist style;
- a clipped collage in a magazine style.

Keep the layout skeleton stable while replacing the surface language.

If neither the user nor the references define a clear palette, read `references/color-palette.md`. Return one recommended palette and one alternative, explain their fit briefly, and obtain confirmation before final generation.

### 7. Produce the requested deliverable

Depending on the request, return one or more of:

- reference audit;
- layout DNA specification;
- fixed-versus-variable table;
- long-image structural outline;
- wireframe with module dimensions;
- section-by-section production brief;
- image-asset briefs with aspect ratio and text-safe zones;
- editable design artifact;
- QA report.

For webpages, keep meaningful copy, controls, and calls to action as real page elements. Do not flatten the page into a single raster image.

For long images and posters, calculate source-file type sizes from the actual display scale. For long-form editorial images, use body text—not the title—as the type-scale anchor. For offline materials, derive hierarchy from physical dimensions and viewing distance.

When creating a complete artifact, first render a structural draft with real headings and body placeholders. Confirm macro composition before refining images and filling all copy.

### 8. Validate

Use the gates in `references/layout-dna.md`, `references/intake-and-legibility.md`, and `references/color-palette.md`. Revise if any hard failure occurs.

## Output format for a reusable specification

Use this order:

1. one-sentence layout thesis;
2. production frame;
3. invariant layout DNA;
4. replaceable visual skin;
5. grid and spacing;
6. narrative and density waveform;
7. section anatomy;
8. module and image rules;
9. typography hierarchy;
10. palette logic;
11. style translation examples;
12. hard failures;
13. unresolved decisions.

Keep topic description out of the invariant rules. Mention it only in the visual-skin or content-mapping sections.

## Resource

Read [references/layout-dna.md](references/layout-dna.md) whenever defining, applying, or validating a long-form layout system.

Read [references/intake-and-legibility.md](references/intake-and-legibility.md) before producing any wireframe, generated image asset, webpage, long image, poster, or offline material.

Read [references/color-palette.md](references/color-palette.md) whenever the user and references do not provide a clear palette.
