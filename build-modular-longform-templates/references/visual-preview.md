# Visual Preview Contract

Use this reference only in `visual-preview` mode or when measuring an arbitrary source image before HTML production.

## Source measurement and segmentation

1. Read the source image's exact pixel width and height from file metadata.
2. Detect semantic boundaries from changes in hierarchy, background surface, whitespace, image group, dividers, section labels and connection artwork. Do not divide the source into equal-height screens.
3. Record each boundary in source pixels and as a normalized vertical ratio from `0` to `1`.
4. Produce a labeled overlay when the user asks to inspect the split or when a boundary is uncertain. Keep the untouched source available beside it.
5. Mark uncertain or overlapping transitions explicitly. Do not present estimated boundaries as recovered source layers.

The file dimensions are exact metadata. Semantic boundaries are visual judgments and become accepted only after the labeled split matches the visible composition or the user confirms it.

## Preview generation

- Default each generated preview canvas to `1000 × 1600 px`; explicit user dimensions override it.
- Generate only the requested representative roles: opening cover, intro, body, image or collage, transition, and ending. Combine roles when one preview communicates the system more clearly.
- Include the actual primary reference in image-generation requests. Preserve its palette, material, type personality, density, image treatment and alignment logic.
- Use representative placeholder copy and clear image-safe zones. Keep logo and QR protection zones intact.
- Treat the preview as a visual approval artifact. Do not generate HTML, CSS or a runtime while the preview remains unapproved.

## Mapping an approved preview to production

After approval, keep `1000 px` as the default HTML source width. The cover defaults to `1000 × 1600 px`; intro, body, image and ending modules use the content-height rules in `SKILL.md`.

Recompose flexible modules when the approved source ratio differs from their production guidance. Preserve hierarchy, whitespace relationships, focal scale, image crop and protected brand zones. Do not uniformly stretch a bitmap or force semantic content into a predetermined slice.

## Acceptance checks

- Confirm exported preview dimensions from the actual file, not the generation prompt.
- Inspect that no headline, subject, logo, QR code or boundary artwork is unintentionally cropped.
- Compare the reference and preview at the whole-frame scale for hierarchy and rhythm.
- Confirm that the labeled source split follows visual transitions rather than equal intervals.
- Record the approved preview filename or identifier as the visual source for `html-production`.
