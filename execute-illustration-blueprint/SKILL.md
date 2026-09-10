---
name: execute-illustration-blueprint
description: Compile an existing reference-image generation blueprint and new target content into executable illustration constraints, then generate, inspect, and selectively repair the raster image. Use after analyze-image-for-generation or when the user supplies a complete visual blueprint, especially for style transfer, small people or animals, embedded scenes inside windows, helmets, screens, cockpits, or body compartments, complex environment-cue lists, protected negative space, density control, and style-consistent revisions. Do not use for reference analysis alone.
---

# Execute Illustration Blueprint

## Mission

Turn an approved visual blueprint into a compact production contract that an image model can execute consistently. Preserve the user's subject and story while translating every included visual role—especially small characters and inset scenes—through the reference's shape, line, fill, modeling, color, texture, and density systems.

Do not redo the source analysis. Do not add new story content. Treat this skill as the execution stage between analysis and image generation.

## Required inputs

Collect from the current request and prior context:

- the approved reconstruction or style-transfer blueprint;
- each reference image and its declared role;
- target subject, required identity cues, inset scenes, candidate text or symbols, environment cues, and frozen composition or colors;
- any previous generated image and the user's concrete feedback;
- whether the user requests a prompt, a new image, or an edit.

If a reference exists but no usable blueprint has been produced, use `analyze-image-for-generation` first. If the user supplied a complete blueprint in the request, use it directly. Ask only when a missing choice changes a hard requirement or required content exceeds the supported capacity.

Before calling an image-generation tool, read and follow the available `imagegen` skill for tool selection, image roles, prompt handling, iteration, and output policy.

## Non-negotiable separation

Maintain three distinct layers:

1. **Blueprint evidence**: established style and organization rules derived from the reference.
2. **Target content**: the new subject, action, story, text, and frozen requirements supplied by the user.
3. **Execution decisions**: target-specific placement, capacity, role adaptation, and overflow handling required to make the first two compatible.

Never present an execution decision as observed source evidence. Never carry source-specific characters, props, text, or motifs into the target unless the user requests them.

## Workflow

### 1. Build the execution contract

Read `references/execution-contract.md` completely. Convert the blueprint and target into:

- hard, medium, and soft constraints;
- a first-read order;
- protected quiet fields and no-content zones;
- named density clusters with element and text budgets;
- a primary-subject clean-area floor;
- visual-layering and clipping rules;
- object-modeling ceilings and floors;
- a palette-role map;
- an overflow deletion order.

Classify target items as:

- **required**: explicitly mandatory or frozen;
- **candidate**: listed as available, optional, symbolic, or environmental cues;
- **incidental**: helpful only when capacity remains.

Every included secondary item must belong to one named cluster or one explicitly permitted quiet-field interruption. Omit unassigned candidate and incidental items. Never solve overflow by shrinking all content or scattering it through protected space.

### 2. Adapt every important visual role

Read `references/role-adaptation.md` whenever the target contains people, animals, creatures, vehicles, mechanical subjects, material-rich objects, or embedded scenes.

Create a compact role card for:

- the primary subject;
- every major object;
- every person, animal, or creature;
- every inset scene inside a window, visor, helmet, screen, cockpit, cutaway, or body compartment.

Each role card must define:

- frame share and visibility priority;
- silhouette and shape grammar;
- pose, gaze, gesture, and prop interaction when applicable;
- line treatment and contour hierarchy;
- fill mode and value-plane ceiling;
- color role and adjacency protection;
- permitted texture and material cues;
- detail budget and protected clean masses;
- concrete style-drift exclusions.

Treat role adaptation as mandatory even when the user only names the character. A role noun such as botanist, diver, pilot, mail carrier, child, dog, or robot does not define how that role belongs to the reference style.

When the source lacks the target category, label the mapping as a cross-category hypothesis and derive it from the closest supported shape, line, fill, modeling, and density mechanisms. Do not let the model fall back to generic anime, glossy 3D, cinematic concept art, editorial vector, or realistic portrait conventions unless the blueprint supports them.

### 3. Compile the generation prompt

Write the prompt in this order:

1. **Execution contract**: first-read order, quiet-space protection, cluster limits, subject clean-area floor, modeling ceiling, inset-scene rule, and overflow behavior.
2. **Reference roles**: identify each attached image as style, composition, subject, or edit reference.
3. **Scene and primary subject**: state the requested story and required identity cues.
4. **Role adaptation cards**: convert important subjects and all people or animals into the reference language.
5. **Inset scenes and layer relations**: state clipping, contour ownership, visibility, and one-action hierarchy.
6. **Background allocation**: name allowed zones and cluster assignments; distinguish required cues from candidate pools.
7. **Color, line, fill, light, and texture**: preserve the blueprint's relationships and scoped exceptions.
8. **Exact text**: quote only requested text and limit its placement and hierarchy.
9. **Avoid**: list concrete drift risks and prohibited overflow.

Front-load the execution contract. Use relationships and limits rather than a pile of style adjectives. Keep the prompt concise enough that hard rules remain legible.

### 4. Generate or edit

- For a new image, attach the supplied references in their declared roles and generate from the compiled contract.
- For a local correction, use the previous output as the edit target, name one defect, and repeat all frozen invariants.
- Do not silently regenerate the whole composition to repair one face, hand, prop, label, or inset scene.
- Do not claim exact control over stochastic output.

### 5. Validate and repair

Read `references/validation-repair.md` completely. Inspect the full frame and a thumbnail-scale view.

Check, in order:

1. first-read subject and silhouette;
2. quiet-field continuity and cluster separation;
3. role-style consistency for every person or animal;
4. inset clipping, action readability, and contour ownership;
5. object-modeling, line, fill, light, color, and texture ceilings;
6. required identity cues and exact text;
7. source-content leakage and unassigned decoration.

For one local failure, make one targeted edit while freezing the rest. For a global rhythm or style failure, reduce candidate content and regenerate once with the execution contract repeated at the beginning. Stop after the bounded correction and report any remaining drift.

## Output behavior

- When the user asks only for a prompt, return the compiled prompt and stop.
- When the user asks for an image, generate it, validate it, and apply the bounded correction when warranted.
- Keep the user-facing completion concise: state what was generated, which invariants were protected, and any remaining visible deviation.
- Do not expose internal scoring, long role cards, or the full audit unless requested.

## Acceptance condition

The result passes only when the new content reads in the reference's visual language at both full size and thumbnail size. Overall palette or texture similarity cannot compensate for a character, animal, inset scene, or major object that uses a conflicting modeling system.
