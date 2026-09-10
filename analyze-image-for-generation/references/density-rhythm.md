# Density Rhythm and Negative Space

## Purpose

Treat density rhythm as an independent visual mechanism. Determine where visual activity concentrates, where the eye rests, how density changes between regions, and whether the primary subject contains clean areas. Do not substitute object count, generic “negative space,” or overall detail level for this analysis.

Keep canvas-level density separate from object-detail density. Use `object-modeling.md` for the internal frequency of value planes, seams, highlights, material cues, hardware, decoration, and microtexture within an object.
Keep overlap-driven density separate from layer order. Use `layering-hidden-shapes.md` to decide which object covers another, how much remains visible, and whether clusters interlock.

## Density drivers

Judge visual activity from the combined effect of:

- edge and contour frequency;
- local contrast and color alternation;
- object overlap and fragmentation;
- text, symbols, hardware, and small marks;
- texture or repeated pattern;
- directional lines and frame crossings.

A large flat shape may be quiet. A region containing only a few objects may still be dense when their outlines, text, contrast, or overlap are strong.

## Build a density-zone map

Divide the canvas into meaningful visual zones rather than forcing an equal grid. Use an equal grid only as an internal cross-check.

For each zone, record:

- region or normalized bounds;
- quiet, transition, medium, or dense level;
- approximate canvas-area share when measured or estimated;
- dominant density drivers;
- hard, soft, or interrupted boundary;
- relation to the focal subject and neighboring zones;
- measured, estimated, or unresolved status.

Then record:

- largest continuous quiet field and the marks allowed inside it;
- number and placement of major density peaks;
- breathing gaps separating clusters;
- direction of density change across the frame;
- whether transitions are abrupt, stepped, alternating, or gradual;
- clean versus decorated portions of the primary subject;
- frame edges that accumulate or release detail.

Use normalized density scores only when a repeatable method produced them. Otherwise use ordered qualitative levels and label area estimates.

## Describe the rhythm grammar

Classify the organization through visible relations such as:

- one dominant cluster against a continuous quiet field;
- several separated density islands;
- center-dense with quiet margins;
- edge-dense with a clean center;
- banded, alternating, diagonal, or graded density;
- broadly uniform density.

State the cadence: where the eye rests, where activity rises, how many peaks occur, and what prevents those peaks from merging. Keep density topology separate from exact source coordinates.

## Transfer to new content

Preserve these as fixed rules when supported and style-defining:

- relative dominance of quiet and dense areas;
- continuity of the largest quiet field;
- number or bounded range of major density peaks;
- separation between clusters;
- distribution of clean and decorated subject areas;
- direction and abruptness of density transitions.

Allow target-dependent positions, shapes, and contents to vary while recomputing the same rhythm grammar. Treat exact source coordinates, literal objects, and incidental gaps as source-specific unless the user freezes the composition.

Translate the map into a density budget for generation:

- identify one or more protected quiet zones and state which content must stay out;
- assign secondary objects, labels, texture, and symbols to named dense clusters;
- state where only low-contrast or isolated accents are allowed;
- set a supported count or range for major clusters and information modules;
- preserve breathing gaps between clusters and clean areas inside the main subject;
- remove or consolidate requested elements that exceed the reference's density budget.

Avoid vague prompt language such as “use negative space” or “keep a balanced composition.” State visible allocation and relevant exclusions. Assess capacity before compiling supporting content; final prompt order follows generation-blueprint-schema.md. Put decisive density rules in the ranked core and remaining controls near the affected cluster.

## Make the budget executable

When several target items compete for space or density is decisive, build the applicable fields below internally; full blueprints expose useful conclusions and compact output only consequential allocation decisions:

- `protected quiet zones`: named regions, minimum area share when estimable, continuity requirement, allowed low-activity interruptions, prohibited element classes, and measurement status;
- `cluster budget`: supported cluster-count range, each cluster's role and region, maximum element or module range, maximum text-group range, and required breathing gap;
- `primary-subject cleanliness`: minimum clean-area share when estimable, protected clean masses, and the maximum supported level of seams, value breaks, hardware, texture, and annotation;
- `candidate inventory`: required, candidate, and incidental items as inferred from the user's wording;
- `allocation ledger`: one cluster or permitted interruption for every included secondary element;
- `overflow policy`: remove incidental items → select among candidates → merge related cues → embed them in an existing device → surface a conflict among required items.

Use ranges or qualitative floors when exact measurement is unsupported. Do not invent percentages solely to make a prompt appear precise. Separate source observations from chosen target constraints. Use ranges or tolerances for estimated area/complexity and state which criteria are critical. A marginal difference from an uncertain estimate is not an automatic failure. A reference with uniform high activity can require high density and no protected quiet field.

User labels control default capacity semantics:

- “must preserve,” “required,” “exact,” and “frozen” are required;
- “available,” “optional,” “may use,” and “environment cues” are candidate pools unless the user explicitly requests all of them;
- unlabeled decorative suggestions are incidental when they do not carry identity, story, or required information.

Do not paste an unassessed candidate pool into the final prompt. Select items by story role and combined visual load. All candidates may be included when each has a supported allocation and the complete composition fits; deletion is not a prerequisite for passing.

## Acceptance check

Compare reference and output at full-frame, thumbnail, and mildly blurred views. Check:

- location, continuity, and approximate share of quiet fields;
- count, strength, and separation of density peaks;
- direction of density transitions;
- intrusion of text, icons, texture, clouds, or props into protected quiet zones;
- primary-subject cleanliness;
- whether a loss of clean subject area comes from object over-modeling rather than added scene elements;
- whether independent information clusters remain separated by breathing gaps.

Mark density rhythm as failed when the output spreads activity broadly across the frame even when the requested objects, palette, and drawing style are present. Diagnose the largest spillover region and revise only its element count, contrast, scale, or placement before changing unrelated style rules.

Treat any of these as a critical density failure when the source depends on quiet/dense contrast:

- a critical protected quiet zone loses its defining continuity or falls meaningfully outside the agreed bound and tolerance;
- the cluster or text-group maximum is exceeded;
- an unallocated candidate appears as an independent object;
- primary-subject clean masses are subdivided enough to violate their critical bound after accounting for estimation uncertainty;
- dense clusters merge because their breathing gaps disappear.

Content completeness does not compensate for a critical density failure. Missing candidate items are acceptable when the capacity gate intentionally omitted them.
