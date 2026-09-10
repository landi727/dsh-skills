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

Use source-supported numbers when available. When the blueprint provides only qualitative evidence, use bounded language such as “one continuous upper quiet field comparable to the reference” and mark the figure unresolved. Do not invent percentages.

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

### Layer and visibility contract

State the role-based stack and decisive local relations. For each major object or inset scene, define:

- what it covers and what covers it;
- clipping or mask boundary;
- contour ownership and redraw order;
- minimum visible identity cues;
- areas that must remain unobstructed.

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

Start the final prompt with a short contract in this pattern:

```text
Execution contract: First read [...]. Protect [...]. Limit the image to [...] density clusters and [...] text modules. Keep at least [...] of the primary subject visually clean when supported by the blueprint. Render all target roles through [... modeling system ...]. Clip inset scenes inside [...]. Treat environment cues as a candidate pool; omit overflow in this order: [...].
```

Then provide the target scene and object details. Do not repeat the same contract throughout the prompt.
