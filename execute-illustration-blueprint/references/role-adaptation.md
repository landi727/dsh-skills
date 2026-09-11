# Role Adaptation

Read this reference whenever a target contains people, animals, creatures, vehicles, mechanical subjects, important discrete objects, important environment roles, material-rich subjects, or embedded scenes.

## Why this step is mandatory

Style references often transfer palette and texture more readily than they transfer the construction of a new semantic category. A newly introduced botanist, diver, child, dog, or vehicle may revert to a generic visual convention unless its modeling rules are translated explicitly.

## Universal role card

Create this common core for every important role, regardless of subject category:

1. **Narrative function**: the single action or identity cue this role must communicate.
2. **Frame share**: large, medium, small, or micro; include a measured value when the blueprint supports it.
3. **Visibility protection**: the silhouette and few identity cues that must remain readable.
4. **Shape translation**: major masses, proportion, deformation, and symmetry policy.
5. **Line translation**: contour weight, internal line density, closure, wobble, and color.
6. **Fill and volume translation**: flat, cut-plane, continuous volume, or painterly; state value-plane and highlight limits.
7. **Color adhesion**: assign palette roles and separation from adjacent fields.
8. **Texture adhesion**: state whether texture belongs to the paper, fill, contour, surface, or atmosphere.
9. **Detail budget**: name the few features that carry recognition; protect clean areas.
10. **Drift exclusions**: name likely defaults that conflict with the blueprint.

Do not place category-specific fields in this core. Build an internal module manifest and append only the applicable module below. Omit every inactive module and its headings from the final prompt. A hybrid subject may activate multiple modules only when their fields govern different visible features.

Keep the full card internal. Compile one compact prompt sentence per important role from the few active fields that control recognition, style adhesion, scale, and interaction. Do not enumerate the schema in the prompt.

## Person module

Activate only for human or humanoid people. Specify framing, head-to-body proportion, face construction, gaze, gesture, hand visibility, clothing-mass treatment, and prop interaction only when those fields carry identity or action. Convert character nouns into observable construction.

For a small figure whose facial detail will not survive thumbnail viewing, default to these ceilings unless the blueprint supports more:

- 3–5 major silhouette masses;
- 1–2 interior value planes or fill roles;
- sparse facial marks rather than modeled facial volume;
- one dominant gesture;
- one action prop;
- no independent lighting scheme inside the figure.

Use the source's proportion logic. Slightly enlarge the head or hands only when doing so preserves action readability and remains compatible with the reference. Avoid generic “cute,” “anime,” “cinematic,” or “realistic” character language unless visibly established.

## Animal module

Activate only for animals or animal-like creatures. Protect species or breed identity through body silhouette, head and muzzle construction, ear and tail geometry, coat or face pattern, posture, and limb readability before adding fur or facial detail. Apply the reference's material ceiling to fur. Use gaze or prop interaction only when the requested action depends on it.

## Mechanical module

Activate for robots, machines, engines, or articulated mechanical systems that are not primarily vehicles. Define functional silhouette, articulation points, shell-to-exposed-part ratio, required hardware, seam vocabulary, and the permitted number and scale of exposed components. Keep unsupported panels, lights, reflections, and engineering microdetail out of the prompt.

## Vehicle module

Activate for land, air, sea, or space vehicles. Define travel orientation, body or hull silhouette, propulsion or ground-contact cues, cabin or cockpit visibility, required identifiers, clean-body minimum, and motion cue. Treat glass, metal, wheels, tracks, wings, or exhaust only through source-supported modeling rules.

## Object module

Activate for tools, products, food, furniture, vessels, clothing, or other discrete objects. Define use orientation, gripping or support relation, opening and part structure, one or two recognition features, and material cues that survive at the object's effective scale. Do not add material vocabulary when material is neither visible nor identity-bearing.

## Environment module

Activate for a location or environmental structure that carries narrative or compositional weight. Define horizon or ground organization, foreground/midground/background allocation, landmark hierarchy, navigable open space, atmospheric depth ceiling, and which region supplies the protected quiet field. Treat minor scenery as cluster assignments rather than separate equal-salience roles.

## Embedded scenes

Activate this module only when a subject is visibly nested inside a window, visor, helmet, screen, cockpit, cutaway, body compartment, or other bounded container. It supplements the nested subject's universal card and category module; it does not replace them.

For a window, visor, helmet, screen, cockpit, cutaway, or body compartment, create an inset-scene card with:

- container geometry and screen location;
- frame or shell as the contour owner;
- strict clipping or supported boundary breaking;
- one primary character or object;
- one primary action;
- one action prop;
- zero or one environmental depth cue unless the blueprint supports more;
- internal color and contrast budget;
- minimum breathing gap between the character and container edge.

Also record:

- container share of the full frame;
- primary nested subject share of the container;
- effective full-frame share across all nesting levels;
- the recognition cues and detail ceiling supported at that effective scale.

Do not import person, animal, mechanical, vehicle, object, or environment fields into the inset unless the nested role activates that category. Keep each inset's contents, lighting, palette allowance, and exclusions scoped to its container.

Prioritize the inset in this order:

1. container silhouette;
2. primary figure or object silhouette;
3. action relationship;
4. one environment cue;
5. decorative or technical information.

Move excess technical information into an existing panel, badge, or diagram when the blueprint supports one. Otherwise omit candidate content.

Redraw the container frame above the inset when the reference uses an opaque shell or outline closure. Prevent hands, faces, drones, vehicles, or scenery from leaking across the boundary unless deliberate boundary breaking is an established source mechanism.

## Cross-category mechanical discipline

For activated mechanical and vehicle modules, protect the identity silhouette and required hardware first. Translate mechanical nouns through the blueprint's shape and modeling system:

- rounded or geometric masses;
- allowed side planes;
- line-based seams and hardware;
- permitted glass or metal cues;
- clean-shell minimum;
- controlled number of exposed components.

Do not let “retro,” “mechanical,” “transparent,” or “metal” authorize extra panels, reflections, microhardware, or realistic engineering detail.

## Material module

Activate only when a material cue carries role identity, action readability, or a frozen user requirement. It may supplement any category module, and remains scoped to that role.

State one permitted recognition cue and one prohibited expansion for each material. Examples:

- transparent window: use a bounded translucent color field; prohibit mirror reflections when unsupported;
- metal shell: use contour and one side plane; prohibit glossy highlights when unsupported;
- water: use a flat path and sparse ripple marks; prohibit photoreal refraction when unsupported;
- paper: use visible fibers or ink irregularity at the reference's scale; prohibit a uniform noise filter when unsupported.

## Demonstrated mappings

These cases illustrate the rule; do not copy their content into unrelated tasks.

### Mail carrier inside an airship window

Keep one carrier, one letter, and one outward hand gesture inside the oval window. Lock the carrier to a palette role and reduce the face to the reference's line and fill system. The window frame closes above the figure. Route maps and floating-island information belong in a separate cargo inset.

### Botanist inside a robot chest compartment

Keep the botanist and seed drone as the one action relationship. Move controls, seed diagrams, and environmental story cues to existing panels or the visor. Prevent the scientist from acquiring a separate realistic or generic science-fiction character style.

### Listener inside a deep-sea helmet or station window

Choose the listener as the primary inset figure. Treat the submarine or signal tower as one subordinate depth cue or move it to a second inset. Match the person, helmet frame, water, and technical symbols to one modeling and line system.
