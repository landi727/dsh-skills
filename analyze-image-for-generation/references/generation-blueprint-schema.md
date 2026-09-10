# Blueprint Output and Prompt Compilation

## Contents

1. Authoritative priority policy
2. Output depth
3. Full-blueprint field inventory
4. One prompt-compilation policy
5. Machine-readable output

## 1. Authoritative priority policy

This file owns priority, prose output depth, and final prompt order for both task modes. Dimension and subtype references supply evidence questions and drawing rules; their local analysis sequences do not prescribe another final prompt order.

Separate two kinds of obligation:

- **Explicit user requirements:** requested identity, story/action, exact content, frozen colors/layout, and delivery constraints. Preserve them; do not silently demote them to fit inferred style rules.
- **Source-derived mechanisms:** the visual relationships that carry the requested reconstruction or style identity. Rank by the perceptual change caused by losing each mechanism, its effect on the task, and its interaction with other mechanisms.

Usually 3–5 defining mechanisms summarize the image; use fewer or more when warranted. This is a focus aid, not a quota or a limit on explicit requirements. Prefer a coupled mechanism when components rely on one another, such as large silhouette + color-field separation, or lost edges + directional brushwork. Keep the underlying evidence distinguishable.

Assign hard/medium/soft priority and rank within each tier:

- **hard:** loss breaks an explicit requirement or a defining visual relationship;
- **medium:** supports identity with bounded variation;
- **soft:** incidental variations with little effect on recognition or style;
- **unresolved:** importance or evidence cannot support an established rule; high impact does not make uncertain evidence factual.

For a decisive mechanism, retain evidence, scope, priority reason, fixed behavior, allowed variation, and visible failure sign. In compact output, show the rule and the information that changes a user's decision; keep the rest internal. Merge duplicate constraints rather than promoting a whole checklist to hard.

No visual dimension has a permanent rank. Consider whole-image mass/focal relationships and source-specific drawing language together. Promote color, deformation, edge/brushwork, texture, gesture, layering, or density whenever the actual reference depends on them. Preserve required complexity and modeling as actively as upper limits.

Resolve conflicts by explicit user priority first, then supported defining mechanisms in rank order, then supporting and incidental detail. Try a compatible target mapping before relaxing a mechanism. Report any material tradeoff. Ask when explicit requirements conflict or the requested identity remains blocked; do not ask about every routine choice. A lower-ranked hard requirement is still required for an unqualified pass.

Keep importance, confidence, inspection sequence, report order, and model execution separate. Front-loading communicates intent; it is not a known model-weight parameter or a guarantee.

## 2. Output depth

Choose depth from the requested deliverable, not image complexity alone.

**Compact analysis (default):**

1. One sentence for task mode and overall visual identity, plus material source limits.
2. A short ranked list of defining mechanisms, each phrased as a visible drawing/organization rule.
3. Useful fixed/variable distinctions and target mapping/overflow decisions, when supplied.
4. A short acceptance list aligned to the ranking and actual validation status.

Keep classification metadata, loaded-file lists, audit ledgers, empty fields, and repeated evidence internal unless requested. A simple image does not require an exhaustive system report.

**Full blueprint:** begin with the same ranked summary, then expand the field inventory below. Give visual layering, object modeling, color relationships, density rhythm, and visual organization distinct labeled blocks ordered by their importance for this reference. Briefly summarize a simple system; expand its supported subfields only when they affect control or the user requests them. State material unknowns once. Report each rule once and refer to it from dependent sections.

**Prompt-only or generation request:** analyze internally, then deliver the executable prompt or requested image with only essential context. Do not prepend the full report. For both modes, compile separate prompts. A request to analyze alone does not authorize generation.

**JSON:** use the existing formal schemas. Required JSON fields remain present, with empty lists/null/unresolved where supported by their field types. Schema completeness does not require displaying those fields in prose or copying them into a prompt.

## 3. Full-blueprint field inventory

This inventory is a reference for applicable fields, not a mandatory ordering of importance.

| System | Fields to preserve when applicable |
| --- | --- |
| Task and source | Mode, exactness, reference roles, type, conflicts, meaningful source limitations |
| Composition/geometry | Frame/crop, projection, main/secondary axes, dominant mass, anchors, proportions, margins and crossings |
| Reconstruction occupancy | Primary and major objects' centers, bounding-box limits, width/height spans, box area, visible silhouette area, edge margins, measurement status; separate inferred hidden envelope |
| Direction/depth | Endpoint roles and screen positions, projected path, near/far roles, visible faces, convergence and foreshortening; preserve mixed projection |
| Visual organization | Focal hierarchy/path, weight/counterweights, motif cadence, graphic devices, semantic groups and story action |
| Visual layering | Spatial-order status, role families, decisive local overlaps/interlocks, contour ownership, visibility protections, masks/windows, recoverability of production order, target mapping and failure signs |
| Object modeling | Recognition strategy, shape grammar, masses, modeling mode, value structure, light/material response, line-based volume, detail progression, exceptions, required effects and ceilings |
| Color | Palette mode, frozen colors, roles/area relations, hue distances, temperature, values, saturation, adjacency/separation or supported blending |
| Drawing surface | Silhouette/frame/internal-line hierarchy, edge behavior, fill, brush/texture scale, scope and local exceptions |
| Density/capacity | Observed quiet/dense topology, peaks/gaps, subject cleanliness when present, relevant bounds and tolerances; required/candidate/incidental content, allocation and actual overflow decisions |
| Target application | Recomputed anatomy, proportions, composition, semantic/layer/color roles; fixed rules, supported variables, source-specific content and hypotheses kept separate |
| Validation | Priorities, concrete drift exclusions, acceptance criteria, source-audit status, generation status, actual tested scope and consequential uncertainties |

Use object cards for source-specific reconstruction or decisive target exceptions. Do not repeat global rules on every object. Style-only tasks do not require a source object census or coordinate registry.

## 4. One prompt-compilation policy

Use the following shared structure for reconstruction and style transfer. The ranked mechanisms inside it are dynamic.

1. **Task anchor:** briefly name mode, target or source identity, and actual reference roles. Include consequential explicit requirements; keep required text in a clearly identified exact-content block when substantial.
2. **Ranked visual core:** state the defining mechanisms in priority order as positive drawing actions and visible relationships. Integrate necessary exclusions with the rule they qualify. Any dimension can lead this block.
3. **Target application:** map recognition cues, action, main masses, composition and supporting content through those rules. Place capacity limits, layer/visibility relations, modeling bounds, color or mark behavior next to the objects/groups they govern. Include only content that fits the assessed capacity; all candidates may fit.
4. **Remaining controls:** add only nonredundant supporting rules, local exceptions, exact content, and concrete exclusions that materially affect the task. Omit audit bookkeeping and speculative production history.

If a material noun may invite unsupported rendering, qualify that noun locally (for example, a flat opaque window with a graphic inset). Target identity may appear before these qualifications. Do not impose a universal density/clean-area/lighting contract before all target nouns.

Compile after target capacity and rule conflicts have been assessed. Keep the reusable style block independent from source identities and target-specific content; the task anchor and target mapping surround it. For a reusable prompt without a supplied target, provide a separate target-content slot. In reconstruction preserve the actual source geometry; in transfer recompute geometry from the new identity and organization grammar.

Compress by merging repeated rules, retaining only decisive local exceptions, and dropping unneeded fields. Do not enforce a universal word cap or lose exact user requirements for brevity. Match the supplied output format and tool capabilities; never invent reference-strength parameters or numeric model weights.

## 5. Machine-readable output

Read `task-blueprint.schema.json` and the schemas referenced by the selected mode. Keep reconstruction and style-transfer payloads separate. The reconstruction `verification` field concerns source audit only.

Order the `mechanisms` array by requested importance, including within priority tiers; explain obligation source and conflicts in existing `reason`, `fixed`, `variable`, and uncertainty fields. This order is semantic and does not depend on JSON object-key order.

Use measured or explicitly estimated normalized positions and area fractions. Preserve measurement status; never substitute bounding-box area for visible silhouette area. Record numerical tolerances and qualitative acceptance conditions in the existing criterion/budget strings. Use null for unsupported numerical claims and unrun prompts/results. Empty density/layer lists are legitimate when there is no supported structure or no target to allocate; explain material limitations in the appropriate text field.

Record actual source bindings and source-audit status separately from generated-output status. Without inspected output, use `not_run` and a null run context. JSON validity establishes the field contract, not effective prompting or successful generation.
