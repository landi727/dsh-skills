---
name: execute-illustration-blueprint
description: Compile an existing reference-image generation blueprint and new target content into executable illustration constraints, then generate, inspect, and selectively repair the raster image. Use after analyze-image-for-generation or when the user supplies a complete visual blueprint, especially for style transfer, small people or animals, embedded scenes inside windows, helmets, screens, cockpits, or body compartments, complex environment-cue lists, protected negative space, density control, and style-consistent revisions. Do not use for reference analysis alone.
---

# Execute Illustration Blueprint

## Mission

Turn an approved visual blueprint into a compact production contract that an image model can execute consistently. Preserve the user's subject and story while translating every included visual role—especially small characters and inset scenes—through the reference's shape, line, fill, modeling, color, texture, and density systems.

Do not redo the source analysis. Do not add new story content. Treat this skill as the execution stage between analysis and image generation.

When the approved blueprint omits a spatial or density field required for execution, perform only the targeted fallback extraction defined in `references/execution-contract.md`. This exception fills missing execution data from the attached reference; it does not reopen the full style analysis.

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

If the blueprint lacks any of the following, extract that field from the reference before compiling the contract: quiet-field location and protected extent, dense-cluster count and footprint, primary-subject clean-area floor, or secondary-element capacity. Mark it as source-derived fallback evidence and enforce the conservative bound as a hard constraint. Do not leave these four fields unresolved when a usable reference is present.

Classify target items as:

- **required**: explicitly mandatory or frozen;
- **candidate**: listed as available, optional, symbolic, or environmental cues;
- **incidental**: helpful only when capacity remains.

Every included secondary item must belong to one named cluster or one explicitly permitted quiet-field interruption. Omit unassigned candidate and incidental items. Never solve overflow by shrinking all content or scattering it through protected space.

### 2. Adapt every important visual role

Read `references/role-adaptation.md` whenever the target contains people, animals, creatures, vehicles, mechanical subjects, important discrete objects, important environment roles, material-rich subjects, or embedded scenes.

First create an internal role inventory and module manifest. The inventory must include:

- the primary subject;
- every major object;
- every required or narratively important person, animal, creature, mechanical subject, vehicle, object, or environment role;
- every important subject inside a window, visor, helmet, screen, cockpit, cutaway, or body compartment.

Give every inventoried role a compact universal role card. Then activate only the matching category module from `references/role-adaptation.md`: person, animal, mechanical, vehicle, object, or environment. Activate the inset module only for genuinely embedded content. A hybrid role may activate more than one category only when each module controls a distinct visible property.

The universal role card defines:

- frame share and visibility priority;
- silhouette and shape grammar;
- line treatment and contour hierarchy;
- fill mode and value-plane ceiling;
- color role and adjacency protection;
- permitted texture and material cues;
- detail budget and protected clean masses;
- concrete style-drift exclusions.

Category-specific fields such as gaze, fur, hardware, cabin, material response, or horizon structure belong only to their activated module. Empty, irrelevant, and inactive fields must not enter the generation prompt.

Treat role adaptation as mandatory even when the user only names the character. A role noun such as botanist, diver, pilot, mail carrier, child, dog, or robot does not define how that role belongs to the reference style.

When the source lacks the target category, label the mapping as a cross-category hypothesis and derive it from the closest supported shape, line, fill, modeling, and density mechanisms. Do not let the model fall back to generic anime, glossy 3D, cinematic concept art, editorial vector, or realistic portrait conventions unless the blueprint supports them.

### 3. Compile the generation prompt

Compile from the module manifest. Role cards remain internal planning artifacts. Emit at most one compact adaptation sentence per important role, using only decisive fields from its active modules. Remove inactive headings, placeholders, defaults, and warnings; do not let one role inherit another role's category fields.

Write the prompt in this order:

1. **Execution contract**: first-read order, quiet-space protection, cluster limits, subject clean-area floor, modeling ceiling, overflow behavior, and only the active module clauses.
2. **Reference roles**: identify each attached image as style, composition, subject, or edit reference.
3. **Scene and primary subject**: state the requested story and required identity cues.
4. **Role adaptations**: convert every important subject through its universal card and activated category module, using one compact sentence per role.
5. **Inset scenes and layer relations**: state clipping, contour ownership, visibility, one-action hierarchy, container share of frame, child share of container, and the child's effective share of the full frame.
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
3. role-style consistency, identity, visibility, and scale for every inventoried important subject;
4. inset clipping, action readability, and contour ownership;
5. object-modeling, line, fill, light, color, and texture ceilings;
6. required identity cues and exact text;
7. source-content leakage and unassigned decoration.

For one local failure, make one targeted edit while freezing the rest. After the edit, compare the full frame, thumbnail, every important-subject crop, and every frozen invariant with the pre-edit output. Reject the edit and retain the pre-edit output when the correction causes material collateral change. For a global rhythm or style failure, reduce candidate content and regenerate once with the execution contract repeated at the beginning. Stop after the bounded correction and report any remaining drift.

## Output behavior

- When the user asks only for a prompt, return the compiled prompt and stop.
- When the user asks for an image, generate it, validate it, and apply the bounded correction when warranted.
- Keep the user-facing completion concise: state what was generated, which invariants were protected, and any remaining visible deviation.
- Do not expose internal scoring, long role cards, or the full audit unless requested.

## Acceptance condition

The result passes only when the new content reads in the reference's visual language at both full size and thumbnail size, every inventoried important subject passes its own checks, and any accepted local repair preserves all frozen invariants. Overall palette or texture similarity cannot compensate for an important role that uses a conflicting modeling system.
