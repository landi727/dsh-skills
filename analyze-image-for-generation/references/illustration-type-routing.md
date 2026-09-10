# Illustration Type Routing

## Classification output

Classify visible construction after selecting reconstruction or style-transfer mode. Record:

- primary type;
- zero to two supporting types;
- visible evidence and counterevidence;
- confidence: high, medium, low, or unresolved;
- loaded subtype modules;
- conflicts that affect generation.

Choose the type from how the image is built. Subject matter alone does not determine it. A painted machine remains painterly; a flat character poster can be primarily flat graphic with character narrative as a supporting type.

## Routing table

| Type | Decisive visible evidence | Load |
| --- | --- | --- |
| `flat_graphic` | Opaque color blocks, crisp or deliberately controlled boundaries, simplified primitives, sparse continuous modeling | `subtype-flat-graphic.md` |
| `painterly` | Brush or mark behavior, mixed edges, layered opacity, color mixing, modeled value masses | `subtype-painterly.md` |
| `collage_print` | Assembled fragments, cut or torn edges, registration behavior, overprint, halftone, paper or reproduced-print structure | `subtype-collage-print.md` |
| `character_narrative` | Character proportion, pose, expression, gaze, interaction, or action carries the image's recognition and story | `subtype-character-narrative.md` |
| `technical_information` | Projection, cutaway, exploded structure, labels, arrows, legends, diagrams, or exact relationships carry meaning | `subtype-technical-information.md` |
| `mixed` | Two or more construction systems remain comparably decisive across the frame | Load only the listed supporting-type modules |

## Routing rules

- Select the primary type by the mechanism whose removal would most change the image's construction and generation requirements.
- Add a supporting type only when it introduces distinct analysis fields or validation criteria.
- Use `mixed` when a single primary choice would hide a genuine construction conflict. List at least two supporting types.
- Classify each source separately when references use different construction systems; then state which source controls each dimension.
- Reconsider classification after the full-frame audit when local crops suggested a misleading type.
- Keep photography, UI interaction design, page-layout systems, and 3D-render pipelines outside this skill's main scope. Analyze illustrated instances only through their visible illustration construction.

Load the shared analysis references for every task, then load only the selected subtype files. Do not merge all subtype prompts or acceptance criteria.

Always load `layering-hidden-shapes.md` and `object-modeling.md` as shared systems. Use the selected subtype module to refine their evidence questions and allowed mechanisms. Do not assign layer grammar or modeling mode from illustration type alone: a flat graphic may interlock several depth bands, a painterly image may use transparent overlays, and a technical illustration may derive volume primarily from lines.
