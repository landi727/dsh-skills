---
name: build-modular-longform-templates
description: Create modular long-image visual previews, then convert an approved preview or reference into reusable HTML and CSS modules with content-driven height and local assets. Use for fixed-style template extension, visual template confirmation, or editable longform production. Exclude standalone style critique, general websites, and Canva-only reconstruction.
whenToUse: Generate and confirm modular long-image previews, or convert an approved reference into editable, composable HTML and CSS modules with extensible body frames. Exclude general websites, critique-only requests, and Canva-only reconstruction.
---

# Build Modular Longform Templates

## Repository Contract

**Type**: Workflow (Creative / Visual Production).
**Responsibility**: Generate modular visual previews for approval, then turn an approved visual reference into reusable, editable HTML + CSS long-image modules and local assets.
**Boundary**: Exclude editor applications, backends, deployment, brand-database integration and Canva-only reconstruction.
**Input Contract**: Use the primary reference, established style, available brand assets and requested module scope. Accept source references at any dimensions. User-specified output dimensions take precedence; otherwise use the defaults below.
**Output Contract**: In visual-preview mode, deliver review images and a measured module map without HTML. In html-production mode, deliver standalone modules, shared CSS, local assets, a composed example and a module manifest.
**Failure Handling**: Ask for missing references; identify inaccessible assets or fonts and unrun tests; preserve completed work and report blocked delivery without claiming verification.
**Validation**: Follow the visual comparison and local-file/content-length checks in references/html-delivery.md.
**Stop Condition**: Finish when requested files are saved and scoped checks pass; stop with a precise blocker when required inputs, tools or delivery access remain unavailable. Do not expand the task to compensate.
**Reuse Scope**: Visual/editorial template production across brands and styles.
**Maturity**: Level 0 Draft. Structural validation and one planning-only usage check were completed; a full failure-mode eval suite, actual template production and a targeted visual revision cycle remain unverified.

## Outcome and scope

Support two modes and do not collapse them into one production pass:

| Mode | Use when | Deliver |
| --- | --- | --- |
| `visual-preview` | The visual template has not been approved | Module preview images plus a measured module map; do not build HTML or CSS yet |
| `html-production` | A preview or reference has been approved for implementation | Locally runnable HTML + CSS modules, composed example, manifest and local assets |

For an end-to-end request, finish `visual-preview`, obtain visual approval, then run `html-production` from the approved image. This approval gate prevents repeated code reconstruction while the visual direction is still changing.

Preserve the approved reference's visual character and editorial relationships while making text, images and section order replaceable. Use representative sample copy and image slots; a complete article is not a prerequisite.

Keep the skill style-neutral. Derive each template family's palette, typography, materials, shapes, density and illustration treatment from that task's references. Do not carry archival paper, orange accents, anime characters, or other sample-specific features into unrelated brands.

Do not expand this task into an editor application, backend, CMS, deployment or database integration. Treat a request for analysis or a module plan only as that scope.

## Dimension system

Keep source recognition and output production as separate coordinate systems.

- **Source reference**: accept any pixel width, height or aspect ratio. Read exact file dimensions from metadata before segmentation. Never use output defaults as slicing boundaries for the source.
- **Preview canvas**: default each review image to `1000 × 1600 px`. A user-specified preview size overrides this default.
- **Production width**: default all HTML modules to a `1000 px` source width. A user-specified production width overrides it.
- **Opening cover**: default to `1000 × 1600 px` and keep its protected brand geometry fixed.
- **Intro section**: `1000 px` wide and content-height; `800–1200 px` is a review guideline, not a clipping boundary.
- **Body section**: `1000 px` wide and content-height. Treat `700–1400 px` as the preferred visual range for one body block and split unusually long copy at a meaningful editorial boundary.
- **Image or collage section**: `1000 px` wide and content-height, determined by approved image ratios, crops, captions and overlap space.
- **Ending section**: `1000 px` wide and content-height; `700–1000 px` is a review guideline while its logo, QR code and protection zones remain fixed internally.

Explicit user dimensions take priority over all defaults. Visual fidelity may justify a different content-height inside the flexible module classes; record that choice rather than stretching or cropping the source composition to fit a guideline.

## Establish the production frame

Read the available references, approved style decisions and supplied brand assets. Use current context before asking questions. Resolve only missing information that materially changes production:

- The primary reference and any secondary references, with their roles.
- The target source width, intended reading scale and any fixed cover dimensions.
- Requested module families, frozen brand placements, and output location.

In `visual-preview` mode, read [references/visual-preview.md](references/visual-preview.md) before generating or validating previews. In `html-production` mode, default to plain HTML + CSS with local relative assets and keep body sections content-height rather than fixed-screen-height. A viewport's first or second screen describes a reading role; it need not be a hard slice boundary.

When the visual reference is missing, ask for it before claiming style fidelity or generating a replacement visual direction. When supplied rules conflict with the reference, follow explicit frozen rules and flag the specific conflict. Do not silently recompose frozen logo zones.

Give a short module plan and disclosed defaults before editing. Proceed on explicit production requests without redundant approvals; obtain a decision when the visual direction or a frozen-rule conflict is unresolved.

## Inspect and decompose the reference

Inspect the actual full image and relevant local details. Preserve the original reference throughout production; keywords alone are insufficient. Read its exact pixel dimensions, then identify semantic module boundaries independently of the target output size. Separate observed evidence from estimates and new implementation choices.

Record three layers, briefly:

1. Style: palette roles, type personality, material, image treatment and decoration.
2. Editorial relationships: hierarchy, whitespace, alignment axes, text/image proportions, density changes, repetition and transitions.
3. Reusable behavior: fixed geometry, replaceable fields, height growth, anchoring and adjacency.

Choose the smallest useful module set supported by the reference and request. Treat this catalog as roles, not a mandatory six-part article:

| Role | Extract |
| --- | --- |
| Opening cover | Logo zone, main/subtitle, dominant image, whitespace, bottom transition |
| Intro or second-screen section | Opening text, section identifier, orienting image |
| Basic body | Heading, body text, dividers, padding, open or framed layout |
| Featured body | Distinct frame/material, image-text layout, local decorations |
| Image or collage | Image count, proportions, overlap, crop and captions |
| Transition and ending | Section joins, closing copy and brand marks |

Combine or omit roles that add no useful capability. Make variants only where the reference shows a meaningful layout difference. Avoid equal-card repetition and arbitrary slicing through a composition.

For each chosen module record: stable ID; reference pixel interval; normalized vertical interval; function; layout; editable fields; fixed parts; flexible parts; extension behavior; top/bottom joins; text capacity or recommended splitting point. Generate a labeled boundary overlay when segmentation is part of the request or any boundary is uncertain. Use measured regions or clear visual landmarks, never invented exact measurements presented as observations.

## Build the template files

Enter this section only in `html-production` mode, using an approved preview or approved reference as the visual source. Read [references/html-delivery.md](references/html-delivery.md) before implementation and verification. It defines the file contract, extension mechanics and tests.

Keep real editable headings and body text in the DOM. Separate background, texture, structural edges, imagery, decoration, text and brand assets into appropriate CSS layers or elements. Keep existing logo artwork and its integral lettering as an image when fidelity depends on it.

Use supplied assets where suitable. Generate or edit raster assets with an available image-generation tool when the reference calls for them, including the actual primary reference in generation requests. Preserve subject relevance and text-safe areas. Do not substitute gradients or generic icons for inspectable reference imagery. Do not reproduce source characters or logos as the target brand's assets without a user request.

Preserve the visual style while adapting the composition for reuse. Do not flatten an entire module and place editable text over baked-in text. Do not claim exact source layer recovery from a flattened reference. Disclose unavailable fonts, approximate materials or inaccessible assets specifically.

Keep textures and illustrations at natural scale. Design repeatable or extendable body surfaces; keep top/bottom edge artwork separate. Treat indefinite height as a layout capability, not a guarantee that every length remains aesthetically balanced. Record a practical split rule for unusually long text.

## Verify and deliver

For `visual-preview`, verify exact exported dimensions, labeled segmentation, composition completeness and reference fidelity; deliver the preview for approval without creating HTML or CSS.

For `html-production`, compare the rendered result with the approved image at whole-page and module scales. Check style fidelity, primary focus, readability, breathing space and the rhythm of the composed example.

Run the structural, local-asset and short/normal/long-content tests in the delivery reference. Correct failures before delivery. Report tests that could not run and any unresolved visual substitutions; do not call an unrendered package verified.

Persist produced template artifacts using the environment's file-saving workflow, except externally git-backed projects. In ChatGPT Work, use the Library workflow for template deliverables; keep skill installation separate from artifact saving. Provide links to the actual files and entry HTML after saving, with a brief note on which files contain text, style and assets. Package template folders for convenient transfer when requested or required by the delivery surface. Do not publish, import or upload into a brand system without authorization.

Conclude concisely in the user's language: delivered modules, edit locations and verification status. Deliver files rather than stopping at analysis, prompts, screenshots or code snippets.
