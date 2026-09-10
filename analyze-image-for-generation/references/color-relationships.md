# Color Relationship System

## Purpose

Turn color from a descriptive mood or swatch list into an executable relationship system. Separate literal hues from the roles and contrasts that make the image readable. Apply this module to reconstruction and style transfer; preserve uncertainty when the source does not support precise measurement.

## 1. Select a palette mode

Choose one mode before assigning target colors:

- **`preserve_source`**: default when the user gives no color instruction. Preserve the source's literal hue families, role assignments, approximate area shares, and relationships even when the target subject suggests another local color or environmental palette.
- **`relationship_transfer`**: use only when the user explicitly requests a new color direction, recoloring, environmental adaptation, or brand adaptation. Hues may change; preserve the source's role hierarchy, hue-distance pattern, temperature allocation, value ladder, saturation budget, and adjacency behavior unless the user explicitly changes one of those relations.
- **`custom_palette`**: use when the user supplies an overall palette, color set, or color-to-role mapping. Assign those colors to source-derived roles, then test the complete system for collisions rather than distributing every requested color uniformly.

Explicitly frozen colors override the selected mode. An isolated recognition color such as a red vehicle or green uniform becomes a frozen role within the current mode; it does not select `custom_palette` by itself. Keep inferred style colors, user-required object colors, and optional target colors in separate fields. Do not interpret a scene noun such as desert, night, forest, or ocean as permission to recolor the style.

Routing examples:

- “same style, new subject” with no color direction → `preserve_source`;
- “adapt the whole image to a desert color direction” → `relationship_transfer`;
- “use this five-color palette” or an explicit role-to-color table → `custom_palette`;
- “keep the vehicle red and white” → freeze those subject roles inside the otherwise selected mode.

## 2. Build a color-role map

For every large field and functionally important accent, record:

- role name and occupied regions;
- approximate area share, measured, estimated, or unresolved;
- hue family and relation to the other major roles;
- warm, cool, or neutral role and its spatial distribution;
- value band and order in the image's lightness hierarchy;
- saturation or chroma band;
- whether the color is fixed, transferable, target-driven, or unresolved;
- allowed neighboring roles and required separation mechanism.

Use functional roles such as background field, primary-subject base, counter-color, light neutral, dark structure, and concentrated accent. The source may support fewer or more roles; do not force a universal count.

## 3. Extract four relationship systems

### Hue-distance structure

Classify every important pair as near, moderate, or opposed in hue. Preserve which large areas are deliberately separated and which small elements form analogous families. Use numeric color-space distance only when the source and measurement method support it; otherwise record a stable qualitative category.

### Temperature allocation

Record the approximate canvas share and spatial role of warm, cool, and neutral colors. State which temperature forms the field, which forms the counterweight, and whether accents are concentrated or dispersed. Preserve the allocation pattern during recoloring instead of warming or cooling every object to match the scene noun.

### Value ladder

Order the principal roles from lightest to darkest and record which adjacent masses depend on value contrast. Include the functions of the lightest and darkest colors. A recolored palette must retain enough steps for the subject, background, nested scenes, text, and outlines to remain separable in grayscale.

### Adjacency matrix

For each pair that touches or nearly touches, specify one policy:

- direct contact is allowed because hue or value separation is sufficient;
- a dark or light outline is required;
- a neutral buffer or gap is required;
- adjacency should be avoided;
- relation is unresolved.

Record the actual separation device: hue distance, value contrast, temperature contrast, outline, neutral gap, texture break, or a combination. Do not rely on outlines to repair every weak color relationship.

## 4. Map the system to a new palette

Apply colors in this order:

1. palette mode and explicitly frozen colors;
2. functional roles and approximate area shares;
3. hue-distance relations among large roles;
4. warm/cool/neutral allocation and spatial distribution;
5. value ladder;
6. saturation budget and accent concentration;
7. adjacency policies and separation devices;
8. literal target hues.

When recoloring, change role colors as a coordinated set. Do not shift every source color toward one environmental hue family. A phrase such as “desert palette” is incomplete unless the prompt also assigns role separation, temperature counterweight, value order, and adjacency rules.

## 5. Detect color adhesion

Treat color adhesion as a critical failure when two or more large neighboring roles combine most of these conditions:

- near hue families;
- the same temperature role;
- similar value bands;
- similar saturation bands;
- no effective outline, neutral buffer, or contrasting field.

Also flag a system when its counter-color is fragmented into tiny accents and can no longer balance the dominant field, or when environmental recoloring collapses background, subject, and supporting scenery into one warm or cool mass.

## 6. Audit and acceptance

Inspect the source or generated result in four views:

- **full frame**: role locations, area balance, and spatial temperature allocation;
- **thumbnail**: immediate separation of the largest masses and bounded accents;
- **grayscale**: value ladder and subject/background separation;
- **adjacency or flat-color map**: pairwise contact rules and missing buffers.

For every decisive color rule, provide visible evidence and scope, generation constraint, failure sign, and acceptance check. Mark area shares and hue/value relations as measured, estimated, or unresolved. A source audit validates the extracted system; a generated-output audit validates whether the system survived generation.
