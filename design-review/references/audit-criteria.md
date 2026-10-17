# Audit criteria

Contents: surface modes; ten categories; pattern judgment; scores.

Calibrate all gstack criteria against approved project requirements. Separate breakage, requirement failures and preference. Use N/A or unverified for inapplicable or unsupported checks.

## Surface modes

- Persuade: visitor decides/acts; coherent first view, recognizable brand, headline, action and useful section roles.
- Operate: visitor finishes a task; scanability, visible states, efficient controls and familiar interactions.
- Read: visitor understands; structure, reading width, navigation and appropriate density.
- Experience: the artifact or art owns the first view; UI supports it.
- Hybrid: classify by section.

Check brand recognition, purposeful anchor, headline scanability, one job per section, justified cards and purposeful motion. Busy imagery behind text, repetition or generic grids are contextual warnings, not universal bans.

## Ten categories and upstream weights

### Hierarchy/composition — 15%

Focal point/action, eye path, competing weights, density, overlap/z-index, purpose above fold, squint-test hierarchy and intentional whitespace. Compare with approved composition.

### Typography — 15%

Font roles/count, scale, line height, reading width, heading semantics, weight, wrapping and legibility. Upstream defaults: no more than three families, roughly 45–75 characters per line, body around 16px+, caption around 12px+. Adapt to language/device/brief. Check numerical alignment, truncation and spacing. Approved fonts cannot fail by appearing on an overused/banned list.

### Color/contrast — 10%

Palette coherence, semantic states, non-color cues, dark elevation, readability and warm/cool consistency. Separate UI tokens from illustration colors. Upstream contrast targets: 4.5:1 ordinary text, 3:1 large text and essential UI boundaries. Precise conformance claims need actual measurements and applicable current standards; never infer ratios by eye.

### Spacing/layout — 15%

Grid, alignment, scale, grouping/rhythm, radii, reading width, safe areas, clipping/overflow, breakpoints and state changes. Deliberate full-bleed art is not a broken UI grid.

### Interaction states — 10%

Hover where applicable, keyboard focus, active/pressed, disabled, loading, empty, error/success, recovery and input clarity. Check touch affordances/size; upstream suggests about 44px targets. Cosmetic browser theming has lower priority than usability. Clear feedback need not always be animated.

### Responsive — 10%

Real composition/control ordering across actual devices, navigation, text, cropping/resolution, touch access, safe areas, overflow and in-scope orientation. Fitting columns can still lack hierarchy; one screenshot cannot prove another viewport.

### Content — 10%

Specific labels, real content, useful errors/empty states, wrapping, recovery and concise instructions. Flag fabricated metrics/testimonials, filler and placeholders within scope. Essential legal, narrative or instructional content does not fail merely for being long.

### Generic patterns — 5%, also separate headline grade

Check whether the result expresses product/art direction instead of an unrelated template: uniform icon-circle grids, identical cards for unequal content, interchangeable sections, vague hero copy, decorative halos, fake data or irrelevant stock images. Explain observed harm. Approved purple, gradients, waves, cards, mascots or generated art are not defects alone. Do not claim these cues prove AI authorship.

### Motion — 5%

Purpose, trigger, continuity, readable intermediate/final states, response, hierarchy and reduced motion. Inspect real frames for character joints, occlusion, layer coverage and deformation when required. Upstream 50–700ms, transform/opacity and limited authored moments are ordinary UI heuristics; approved scenes, springs, SVG deformation, WebGL/shaders and narratives need their own contract/device evidence. Specialized feasibility/implementation belongs to the relevant skill.

### Performance feel — 5%

Observed loading/interaction delay, layout shifts, image/font readiness, long tasks and rendering stability. Upstream targets roughly LCP below 2s for apps/1.5s for informational pages, CLS below 0.1. These are targets, not produced measurements. Record tool/device/conditions/samples; distinguish lab from field evidence. A still yields no exact performance score.

## Grades

Upstream A: intentional/polished; B: solid/minor inconsistencies; C: functional/generic; D: visibly unfinished; F: harms experience. Each category starts A; High lowers one grade, Medium half a grade, Polish is recorded without lowering. Do not duplicate one issue from manual and detector findings.

Use the weights above for a transparent reasoned Design Score. Upstream does not specify letter-number conversion or rounding; label any numeric mapping as this run's convention. Incomplete coverage produces provisional grades/excluded categories, not assumed A for unseen checks.

Show AI Slop/generic-pattern grade separately, calibrated to approved design. Keep project acceptance status separate: aesthetics cannot compensate for a failed critical requirement.
