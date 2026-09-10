# Object Modeling System

## Contents

1. Purpose and modeling modes
2. Shape and mass construction
3. Value, light, and material response
4. Line-based volume and object detail density
5. Object tiers, transfer, prompt compilation, and acceptance

## Purpose

Turn object rendering from scattered adjectives into an executable construction system. Record both the required mechanism and its upper limit so generation does not add plausible volume, gloss, reflection, perspective structure, or microdetail that the source does not use.

Keep these axes independent. A reference may combine flat volume with rich print texture, strong volume with sparse detail, or transparent objects represented by opaque color blocks. Do not compress volume, lighting, material response, line-based depth, and detail density into one intensity score.

## 1. Select the modeling mode

Choose the dominant mode from visible evidence, then record important local exceptions:

- **`none_flat`**: recognition comes from silhouette, outline, and local color; no modeled light or turning planes.
- **`symbolic_flat`**: one or a few hard-edged side, light, or dark shapes imply volume without continuous modeling.
- **`discrete_faceted`**: several explicit value or color planes construct form through hard or controlled boundaries.
- **`soft_modeled`**: restrained gradients or soft value transitions model selected forms while clean planes remain.
- **`continuous_volumetric`**: continuous light, shadow, reflection, and material response construct most forms.
- **`mixed`**: two or more modes are comparably decisive and assigned to named regions or object categories.
- **`unresolved`**: the source cannot support a stable classification.

Illustration type informs the questions to ask; it does not select the mode automatically. Record global mode, evidence, scope, confidence, fixed behavior, allowed variation, and both over-modeling and under-modeling signs.

## 2. Build the shape grammar

For representative objects, record:

- recognition strategy: silhouette, internal structure, value planes, material cues, text, or symbols;
- primary primitives and contour families;
- primary mass, secondary masses, attachments, cutouts, and joints;
- supported mass count or complexity range;
- connection behavior: fused, overlapping, inset, hinged, stacked, outlined, or separated;
- curve, corner, taper, inflation, compression, skew, and asymmetry behavior;
- whether internal divisions follow physical construction, graphic partition, decoration, or narrative framing;
- clean mass areas that must remain free of added structure.

In reconstruction, retain source-specific geometry. In style transfer, preserve the grammar and recompute masses from the target's identity cues. Do not reproduce the source's object anatomy on an unrelated target.

## 3. Extract the value structure

Record:

- visible value-plane count, or unresolved when continuous modeling prevents a stable count;
- light-to-dark order of the planes;
- total object value span and adjacent-plane contrast: minimal, low, medium, or high;
- approximate area share of principal light, local-color, and dark planes when supportable;
- edge behavior: hard, soft, lost, broken, gradient, or mixed;
- gradient policy: absent, local only, broad, continuous, mixed, or unresolved;
- whether side planes, cavities, highlights, and shadows are structural, symbolic, or illumination-driven.

Use measured color or value differences only when a repeatable method supports them. Otherwise preserve ordered qualitative bands and label estimates.

## 4. Extract the lighting ceiling

Record the source's lighting logic and the maximum allowed intensity for:

- highlights;
- attached dark planes;
- cast shadows;
- ambient-occlusion darkening;
- specular highlights;
- reflections and reflected-light accents;
- transparency, refraction, and glow.

For each allowed effect, state its shape, edge, area, placement, and object scope. An absent effect becomes a prohibition when adding it would change the source's modeling identity. A material noun such as glass, metal, chrome, water, helmet, cockpit, or building does not authorize extra optical effects.

Distinguish physically coherent light from graphic separation. Preserve symbolic light as graphic planes even when the target object could support realistic shading.

## 5. Extract material response

For each materially distinct object class, record:

- how the material is recognized: color, outline, symbol, edge, texture, transparency, reflection, or value modeling;
- response class: flat symbolic, matte, semi-matte, glossy, optically transparent, textural, mixed, or unresolved;
- allowed highlight, reflection, transparency, gradient, and texture behavior;
- forbidden material expansions;
- whether the material treatment changes with focal importance or object size.

Keep visible evidence separate from inferred real-world material. A blue window may function as a flat blue panel; describe optical transparency only when the image visibly constructs it.

## 6. Extract line-based volume

Separate:

- silhouette contours;
- structural seams and divisions;
- turning or cross-contour lines;
- thickness and side-edge lines;
- perspective-construction lines;
- decorative or symbolic lines.

For each system, record its volume function, density, hierarchy, and allowed scope. State whether target generation may add lines to clarify physical form. When the source uses lines only for boundaries and symbols, prohibit extra contour wrapping, perspective subdivision, panel seams, and architectural depth lines.

## 7. Build the object-detail density profile

Keep this separate from canvas-level density rhythm. For the global system and each important object tier, record:

- clean interior area share, measured, estimated, or unresolved;
- identity-bearing detail density;
- structural detail density;
- decorative detail density;
- surface microdetail density;
- mark scale relative to the object;
- concentration pattern and protected clean regions;
- whether detail increases or decreases from primary subject to supporting and background objects.

Do not infer density from object count alone. A single object can be over-modeled through extra plane boundaries, reflections, seams, texture, and small hardware.

## 8. Apply global rules and scoped exceptions

Build one global modeling profile, then define only evidence-supported overrides for:

- primary subject;
- major objects;
- supporting objects;
- background elements;
- special materials or nested scenes.

Every override must name the affected field and evidence. Do not let one glossy, textured, or highly modeled local region raise the rendering intensity of the whole image.

## 9. Transfer and prompt compilation

Compile using generation-blueprint-schema.md. Preserve shape grammar, recognition cues, and required modeling behavior along with supported upper bounds. State positive rendering actions before concrete exclusions; a dense or volumetric source must retain its defining complexity.

Place decisive shape/modeling mechanisms in the ranked visual core and attach other controls to the affected object tier or material noun. A local qualification such as an opaque flat window is sufficient when that is the only material risk. No universal lighting/detail contract or material-before-identity sequence is required.

Use quantitative bounds only when they help control an important visual relationship. Distinguish observed source values from chosen target bounds and record measurement status. For uncertain estimates, use ranges/tolerances or named qualitative limits; do not fail a result for a marginal numerical difference unsupported by measurement. Protect clean masses only when the source uses them.

## 10. Failure and acceptance

Treat these as over-modeling failures when unsupported by the source:

- added glossy highlights, reflections, refraction, glow, or ambient occlusion;
- extra gradients or rounded shading that increase apparent volume;
- perspective, turning, seam, or panel lines that construct new depth;
- every object receiving equally complete material and volume modeling;
- loss of large clean planes through hardware, texture, or tonal subdivisions.

Treat missing decisive planes, value masses, shadows, edge transitions, or material responses as under-modeling failures in references that depend on them.

Inspect the full frame and representative objects. Select thumbnail, grayscale, or mild blur only when they clarify a consequential modeling claim. Compare modeling mode, mass hierarchy, value-plane count, value span, highlight/shadow footprint, line-based depth, material response, clean-area share, and detail progression across object tiers. Record `pass`, `partial`, `fail`, or `not_run` separately from source-analysis confidence.
