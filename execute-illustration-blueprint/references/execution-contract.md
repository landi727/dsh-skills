# Execution Contract

Use this reference to convert a visual blueprint and target story into a bounded image-generation specification.

## Contract fields

### Perceptual order

State the intended reading sequence as ranked roles, not as a list of nouns. Protect the first-read subject from competing text, accent colors, microdetail, and background contrast.

### Spatial and density budget

Define:

- primary subject occupancy and crop;
- largest continuous quiet field and its protected minimum when supported by the blueprint;
- allowed interruptions inside quiet fields;
- dense-cluster count and location;
- breathing gaps between clusters;
- primary-subject clean-area floor;
- text-module count and hierarchy.

Use blueprint measurements when available. When any of the four execution fields below is missing and a usable reference is attached, perform a targeted fallback extraction from the reference:

1. View the reference at full size, thumbnail scale, and mildly blurred scale.
2. Map each continuous quiet field by normalized location, approximate extent range, allowed interruptions, and the boundary that must stay open.
3. Count dense clusters; record each cluster's location, approximate footprint, dominant contents, and the breathing gap separating it from the next cluster.
4. Estimate the primary subject's largest uninterrupted clean mass as a bounded share of that subject, excluding inset windows, labels, and crossing props.
5. Count the independently readable secondary elements inside each source cluster and record that count as the capacity ceiling for the corresponding target cluster.

Label these values `source-derived fallback`. Use ranges when edges are ambiguous, protect the larger quiet-field bound and clean-area bound, and use the lower cluster-count or capacity bound. Once derived, these values are hard execution constraints. Do not substitute generic percentages, leave the field unresolved, or repeat the full style analysis.

### Content-capacity gate

Create a compact table internally:

| Cluster | Capacity | Required assignments | Candidate assignments | Protected gap |
|---|---|---|---|---|

Apply these rules:

- Required items receive capacity first.
- Candidate items are a selection pool; inclusion is optional.
- Incidental items enter only after all protected gaps remain intact.
- One visual module may combine closely related cues when the reference supports inset panels, diagrams, badges, or symbolic compression.
- Each secondary item belongs to exactly one cluster or permitted interruption.

Resolve overflow in this order:

1. remove incidental items;
2. reduce candidate items;
3. combine related cues into one symbol or inset;
4. reuse an existing panel or container;
5. report a conflict between required items and supported capacity.

Do not increase capacity by shrinking every element. Preserve the source-derived scale tier and remove lower-priority content first.

### Module activation and isolation

Maintain an internal activation manifest before prompt compilation:

- `core`: always active for the execution contract and universal role fields;
- `person`, `animal`, `mechanical`, `vehicle`, `object`, `environment`: active only for roles in that category;
- `inset`: active only when content is visibly nested inside a bounded container;
- `text`: active only for exact requested text or source-supported mandatory labels;
- `material`: active only when a material cue carries identity or a frozen requirement.

A prompt field enters the final prompt only when its module is active and the field contains target or source evidence. Omit inactive headings, empty slots, inherited defaults, and exclusions for modules that are not present. Bind each secondary module to one named cluster or container so its contents and rules cannot leak into another module or a quiet field.

### Layer and visibility contract

State the role-based stack and decisive local relations. For each major object or inset scene, define:

- what it covers and what covers it;
- clipping or mask boundary;
- contour ownership and redraw order;
- minimum visible identity cues;
- areas that must remain unobstructed.

For every nested role, record three linked scales:

- container share of the full frame;
- nested subject share of its immediate container;
- effective full-frame share, calculated from the two values above and every additional nesting level.

Set recognition features and detail tier from the effective full-frame share. If the effective share falls below the reference-supported readability floor, enlarge the container or nested subject, simplify to fewer recognition cues, or omit candidate content. Do not compensate with microdetail, boundary leakage, or a separate lighting system. Rules inside a container apply only inside that container unless the blueprint explicitly supports boundary breaking.

### Modeling contract

Carry forward the blueprint's:

- modeling mode;
- shape grammar and deformation;
- value-plane count and edge behavior;
- lighting and gradient ceiling;
- material response;
- line-based depth cues;
- object-tier detail progression;
- protected clean masses.

For every material-rich noun, state the permitted visual cue and prohibited expansion. “Glass,” “metal,” “water,” “fur,” or “fabric” must not silently introduce unsupported highlights, reflections, gradients, shadows, or microtexture.

### Palette contract

Map target roles onto the blueprint's color relationships:

- background or paper role;
- primary subject role;
- separator and outline role;
- accent roles and area limits;
- adjacency rules;
- opacity and texture behavior.

Explicitly frozen colors override the default mapping. Keep the number of active color roles within the blueprint's supported range.

### Avoid and deletion rules

List only concrete risks supported by the task or known failure history, such as:

- generic anime facial construction;
- smooth 3D or glossy mechanical rendering;
- realistic portrait shading inside a flat illustration;
- random decorative scatter through a quiet field;
- repeated icons or extra unrequested labels;
- inset content bleeding outside its container;
- all environment cues rendered at equal salience.

Avoid vague phrases such as “bad composition” or “wrong style.”

## Compact prompt header

Start the final prompt with a short contract in this pattern, retaining only clauses whose modules are active:

```text
Execution contract: First read [...]. Protect [...]. Limit the image to [...] density clusters and [...] text modules. Keep at least [...] of the primary subject visually clean when supported by the blueprint. Render all target roles through [... modeling system ...]. Clip inset scenes inside [...]. Treat environment cues as a candidate pool; omit overflow in this order: [...].
```

Then provide the target scene and object details. Omit the inset, text, material, or environment clause when its module is inactive. Do not repeat the same contract throughout the prompt.

After compilation, run a deletion pass: remove every field whose module is inactive, every empty placeholder, and every secondary item without a cluster or container assignment.
