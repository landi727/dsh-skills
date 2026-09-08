---
name: build-modular-longform-templates
description: Build reusable HTML and CSS long-image modules from supplied references and an established visual style, including opening, body, image and closing sections with content-driven height and local assets. Use for fixed-style template extension, modular longform templates, or stretchable editorial text frames intended for Cursor or direct HTML editing. Exclude standalone style critique, general websites, and Canva-only reconstruction.
whenToUse: Build modular long-image HTML and CSS templates from supplied references and a fixed visual style, with editable content and extensible body frames. Exclude general websites, critique-only requests, and Canva-only reconstruction.
---

# Build Modular Longform Templates

## Repository Contract

**Type**: Workflow (Creative / Visual Production).
**Responsibility**: Turn approved visual references into reusable, editable HTML + CSS long-image modules and local assets.
**Boundary**: Exclude editor applications, backends, deployment, brand-database integration and Canva-only reconstruction.
**Input Contract**: Use the primary reference, established style, available brand assets and requested module scope; resolve missing references and frozen-rule conflicts before production. Disclose provisional dimensions.
**Output Contract**: Deliver standalone modules, shared CSS, local assets, a composed example and a module manifest as specified in references/html-delivery.md.
**Failure Handling**: Ask for missing references; identify inaccessible assets or fonts and unrun tests; preserve completed work and report blocked delivery without claiming verification.
**Validation**: Follow the visual comparison and local-file/content-length checks in references/html-delivery.md.
**Stop Condition**: Finish when requested files are saved and scoped checks pass; stop with a precise blocker when required inputs, tools or delivery access remain unavailable. Do not expand the task to compensate.
**Reuse Scope**: Visual/editorial template production across brands and styles.
**Maturity**: Level 0 Draft. Structural validation and one planning-only usage check were completed; a full failure-mode eval suite, actual template production and a targeted visual revision cycle remain unverified.

## Outcome and scope

Deliver actual, locally runnable HTML + CSS module files, a composed long-image example, and local assets. Preserve the approved reference's visual character and editorial relationships while making text, images and section order replaceable. Use representative sample copy and image slots; a complete article is not a prerequisite.

Keep the skill style-neutral. Derive each template family's palette, typography, materials, shapes, density and illustration treatment from that task's references. Do not carry archival paper, orange accents, anime characters, or other sample-specific features into unrelated brands.

Do not expand this task into an editor application, backend, CMS, deployment or database integration. Treat a request for analysis or a module plan only as that scope; generate files when production is requested.

## Establish the production frame

Read the available references, approved style decisions and supplied brand assets. Use current context before asking questions. Resolve only missing information that materially changes production:

- The primary reference and any secondary references, with their roles.
- The target source width, intended reading scale and any fixed cover dimensions.
- Requested module families, frozen brand placements, and output location.

Default to plain HTML + CSS with local relative assets. State a provisional source width when none is supplied, and keep body sections content-height rather than fixed-screen-height. A viewport's first or second screen describes a reading role; it need not be a hard slice boundary.

When the visual reference is missing, ask for it before claiming style fidelity or generating a replacement visual direction. When supplied rules conflict with the reference, follow explicit frozen rules and flag the specific conflict. Do not silently recompose frozen logo zones.

Give a short module plan and disclosed defaults before editing. Proceed on explicit production requests without redundant approvals; obtain a decision when the visual direction or a frozen-rule conflict is unresolved.

## Inspect and decompose the reference

Inspect the actual full image and relevant local details. Preserve the original reference throughout production; keywords alone are insufficient. Separate observed evidence from estimates and new implementation choices.

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

For each chosen module record: stable ID; reference location; function; layout; editable fields; fixed parts; flexible parts; extension behavior; top/bottom joins; text capacity or recommended splitting point. Use normalized regions or clear visual landmarks, never invented exact measurements presented as observations.

## Build the template files

Read [references/html-delivery.md](references/html-delivery.md) before implementation and verification. It defines the file contract, extension mechanics and tests.

Keep real editable headings and body text in the DOM. Separate background, texture, structural edges, imagery, decoration, text and brand assets into appropriate CSS layers or elements. Keep existing logo artwork and its integral lettering as an image when fidelity depends on it.

Use supplied assets where suitable. Generate or edit raster assets with an available image-generation tool when the reference calls for them, including the actual primary reference in generation requests. Preserve subject relevance and text-safe areas. Do not substitute gradients or generic icons for inspectable reference imagery. Do not reproduce source characters or logos as the target brand's assets without a user request.

Preserve the visual style while adapting the composition for reuse. Do not flatten an entire module and place editable text over baked-in text. Do not claim exact source layer recovery from a flattened reference. Disclose unavailable fonts, approximate materials or inaccessible assets specifically.

Keep textures and illustrations at natural scale. Design repeatable or extendable body surfaces; keep top/bottom edge artwork separate. Treat indefinite height as a layout capability, not a guarantee that every length remains aesthetically balanced. Record a practical split rule for unusually long text.

## Verify and deliver

Compare the rendered result with the original reference at whole-page and module scales. Check style fidelity, primary focus, readability, breathing space and the rhythm of the composed example.

Run the structural, local-asset and short/normal/long-content tests in the delivery reference. Correct failures before delivery. Report tests that could not run and any unresolved visual substitutions; do not call an unrendered package verified.

Persist produced template artifacts using the environment's file-saving workflow, except externally git-backed projects. In ChatGPT Work, use the Library workflow for template deliverables; keep skill installation separate from artifact saving. Provide links to the actual files and entry HTML after saving, with a brief note on which files contain text, style and assets. Package template folders for convenient transfer when requested or required by the delivery surface. Do not publish, import or upload into a brand system without authorization.

Conclude concisely in the user's language: delivered modules, edit locations and verification status. Deliver files rather than stopping at analysis, prompts, screenshots or code snippets.
