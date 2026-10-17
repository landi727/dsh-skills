---
name: design-review
description: Audit rendered website design, hierarchy, typography, spacing, responsive layouts, interaction states and consistency; triage findings, apply authorized minimal fixes and recheck with before/after evidence and regression baselines. Use for website visual QA, design polish or design regression review. Standalone Work adaptation of gstack design-review; reviews motion presentation but does not implement character animation, fluid simulation or shaders.
---

# Design Review

Use gstack's audit → triage → fix → verify method with current native tools. Read [audit-criteria.md](references/audit-criteria.md) before judging the design, and [report-contract.md](references/report-contract.md) before recording findings or baselines.

Source: [garrytan/gstack](https://github.com/garrytan/gstack/tree/4015c2870b064644131ed6f7cfcc1469cfe9808c/design-review), MIT. Provenance and original hashes are in `references/source.json`; preserve `LICENSE`. The exact original in `references/upstream-design-review.md` is archival reference: its host commands are not this installation's execution instructions.

## Host integration and project authority

- Use available native tools and follow their advertised documentation. For a requested site audit, prefer sufficient connected plugins when host policy requires them; otherwise use the permitted browser interface. For local apps, use existing preview/testing tools and the applicable frontend testing skill. Do not assume Aside, `$B`, `$D`, Claude paths, login sessions or unsupported browser capabilities.
- This installation contains the method, not gstack's browser engine, automated detector, designer, telemetry, external model reviewers or GBrain. Do not install that framework, other skills, CLIs, detectors or test frameworks as an audit side effect.
- Missing operations produce missing evidence, never a pass. A static supplied image supports a scoped static review; it cannot verify unseen viewports, live interaction, console, motion continuity or measured performance.
- Treat user scope, approved references, DESIGN.md/design-system.md and behavior/motion contracts as binding. Compare actual rendering against them. Separate an approved choice from accidental drift; do not redesign an approved concept to satisfy generic preferences.
- Preserve approved illustration, character motion, WebGL, fluid deformation, lighting, palettes, fonts and composition. Generic defaults such as transform/opacity only, 50–700ms, one motion per view, or overused-pattern lists cannot reject an approved artistic/technical choice. Check actual clarity, continuity, accessibility and rendering.
- An audit is read-only unless fixes are authorized. Dirty trees permit review. Protect pre-existing work during fixes; never commit/stash everything as a setup requirement. Commit, merge, publish, submit or change production only within actual session authorization.

## Setup

1. Establish target URL or supplied evidence, project directory, pages/routes, device priorities, approved contracts and whether fixes are authorized. Use session context before asking for missing inputs.
2. Select **standard** (5–8 representative pages), **quick** (homepage + two), **deep** (10–15 and critical flows), **diff-aware** (affected routes) or **regression** (compare prior baseline). Review actual pages available; do not manufacture coverage for a smaller site.
3. For diff-aware review, resolve the actual base/recorded revision and map changed files to routes. Do not assume main or probe unrelated ports/sessions. Use the project's known entry/start command.
4. Read approved design documents and previous baseline; record revision/working-tree state and capture conditions. Establish a supported way to preserve raw screenshots and flow observations.
5. Create a unique run ID and a project-scoped report/evidence location. Save completed standalone deliverables using the host's required artifact workflow. Never overwrite previous runs, source illustrations, approved references or generated images to reuse filenames.
6. For authorized fixes, inspect and use relevant existing tests. Do not bootstrap test frameworks or change CI for an audit.

## Phases 1–6: Audit baseline

### 1. First impression

Capture/read the actual initial desktop or priority-device view before implementation analysis. Check that the correct route loaded; a login wall, error page or loading state is not the requested page. Follow host authentication guidance if blocked.

Describe what it communicates, the first three visual anchors and whether that order supports the goal. Name concrete elements and positions. Apply the page-area test: can each major area be named by purpose in about two seconds? Classify the surface as Persuade, Operate, Read, Experience or Hybrid.

### 2. Actual design system

Extract rendered typography, heading hierarchy, UI palette, spacing rhythm, grid, radii and states through screenshots and permitted rendered-page inspection. Distinguish declared tokens from observed output. Do not count every illustration color as a UI token. Record discrepancies against approved design. Create/change a canonical design-system document only within authorized scope.

### 3. Pages and viewports

Apply all relevant categories in audit-criteria.md. Capture/read representative phone, tablet and desktop states, ordinarily 375×812, 768×1024 and 1440×900, plus contract-specific breakpoints. Report unsupported/unseen viewports rather than assuming results.

Check default, loading, empty, error, long-content and relevant expanded/selected states. Record clipping, overlap, legibility, affordance, hierarchy and inconsistent components. Collect console/loading evidence only through supported actual operations.

Apply the trunk test where relevant: site identity, page identity, major sections, available options, current location and search. Mark inapplicable features N/A; galleries need not have search. Every finding requires a screenshot or precise raw-image pointer, observed consequence, impact, affected requirement/goal and concrete correction.

During phases 1–6, assess rendered evidence rather than reading source to infer visual success. Approved documents and diff-to-route mapping are allowed inputs. Read implementation later for fixes or separate implementation review.

### 4. Interaction flows

Walk two or three representative flows, or every critical flow in a small product. Capture trigger, transitions and final state. Assess response, feedback, focus, validation and recovery. Respect host consent rules for submissions/external side effects.

For motion inspect actual intermediate continuity, final state and reduced-motion behavior. A still cannot verify fluid/character movement. Use installed reference-motion analysis or illustration-motion validation when required and available.

Optional upstream goodwill heuristic starts at 70/100: hidden needed information −15, format punishment −10, needless data requests −10, blocking tours −15, sloppy appearance −10, ambiguous choices −5; obvious tasks +10, clear costs +5, saved steps +5, graceful recovery +10, appropriate error acknowledgment +5. Report specific causes; this is not measured user research.

### 5. Cross-page consistency

Compare navigation, footer, shared component states, typography, layout, spacing, voice and brand. Distinguish intentional variation from accidental drift. Prefer a scoped shared-component correction when it resolves multiple observed instances.

### 6. Report and baseline

Record findings incrementally using report-contract.md. Include actual page/viewport/state coverage, missing evidence, ten category grades, separate generic-pattern grade and project acceptance status. Add three to five real quick wins where useful.

Save a unique immutable per-run baseline. Compare with compatible prior evidence for new/resolved/persistent findings and grades. Preserve old runs. Heuristic grades cannot override failed requirements.

## Independent review

When delegation is available, dispatch a fresh read-only reviewer with fork_turns="none", raw screenshots, approved contracts, flow records, coverage and project path. Give task-local context, no parent history or desired verdict. It may inspect relevant source as a separate implementation check. Wait for its result before claiming independent review.

Resolve disagreement against raw evidence. Label this independent-agent review; do not claim external/cross-model review unless it actually ran. If unavailable, record the limit and perform bounded self-review.

## Phases 7–11: Authorized fixes and verification

### 7. Triage

Sort high, medium and polish findings. Separate acceptance blockers from aesthetic preference. Defer out-of-scope, third-party or unavailable-content issues. An audit-only request finishes with report/evidence/suggested actions; it does not authorize edits.

### 8. Minimal fix loop

For each authorized finding:

1. Capture the before state. Read relevant source; use rg to locate the smallest responsible rule/component.
2. Apply the smallest correction. Prefer local styling when adequate; do not refactor unrelated code or simplify approved art to make review easy.
3. Keep each change independently reviewable/reversible. If committing is authorized, stage only its files/hunks and use an atomic descriptive commit; preserve unrelated work.
4. Reload in matching viewport/state/content/capture conditions. Capture/read after evidence; check related routes and new errors.
5. Classify verified/best-effort/reverted/deferred using the report contract. For a regression undo only this review's patch or its own commit, preserving user/subsequent work.
6. Run appropriate existing behavior checks. Add meaningful regression tests only for real behavior failures; CSS-only polish ordinarily uses visual evidence, without implementation-mirroring tests.

Mockups are optional targets, not rendered verification. Use host image workflows only when creation is in scope. Never claim the unavailable gstack designer/detector ran.

Reassess after five fixes or a regression. Upstream risk heuristic: +15 per revert, +5 per component file, +1 per fix after ten, +20 for unrelated files. Above 20, stop speculative expansion, assess evidence and narrow/defer; continue clear authorized corrections under host rules. Retain the upstream cap of 30 fixes per run, reporting remaining work.

### 9. Final audit

Retest affected pages/flows in comparable conditions and recompute grades. Confirm fixes and no regression against approved design/behavior. Unseen device/motion/console/performance checks remain unverified. Repeat detector comparison only if a compatible detector actually ran initially; otherwise detector.mode stays none.

### 10. Final report

Record each finding's actual status, evidence, changed files, own commit if applicable, checks/conditions and unresolved limits. Give verified/best-effort/reverted/deferred totals, baseline → final grades, acceptance blockers and next actions. A PR-ready sentence must not imply unobserved coverage.

### 11. Existing task records

Update existing authorized TODOS.md/project records for deferred/resolved findings. Do not introduce cross-project memory systems or change project rules as an audit side effect.
