# Stage procedures

## Contents

1. Constitution
2. Specify
3. Clarify
4. Plan
5. Checklist
6. Tasks
7. Analyze
8. Implement
9. Converge
10. Tasks to issues

## 1. Constitution

Purpose: establish project-wide governance that later artifacts must obey.

Inputs:

- Existing `.specify/memory/constitution.md`, if present
- Project instructions, architecture constraints, quality requirements, and user-provided principles

Procedure:

1. Separate governance statements from feature requests and implementation requests.
2. Preserve still-valid existing principles and identify additions, changes, and removals.
3. Express each principle as a testable `MUST`, `SHOULD` with rationale, or explicit prohibition.
4. Include amendment rules, compliance review, ratification date, amendment date, and semantic
   version.
5. Change only the constitution. Defer feature or code work to the appropriate later stage.
6. Validate that no unexplained placeholder remains.

Output: `.specify/memory/constitution.md` and a concise change-impact report.

## 2. Specify

Purpose: describe one feature's observable product behavior without choosing implementation.

Inputs:

- A non-empty feature description
- Constitution, relevant product documents, and existing behavior

Procedure:

1. Create one feature directory with a stable short name. Reuse the active directory when updating
   an existing feature.
2. Identify actors, goals, primary journeys, data concepts, constraints, boundaries, and exclusions.
3. Write independently testable user stories in priority order. Each story must deliver observable
   value on its own.
4. Give acceptance scenarios explicit Given/When/Then behavior.
5. Assign stable IDs to functional requirements (`FR-001`) and success criteria (`SC-001`).
6. Keep success criteria measurable and technology-agnostic.
7. Document assumptions. Use at most three `[NEEDS CLARIFICATION: ...]` markers for choices that
   materially change scope, security/privacy, or user experience and lack a safe default.
8. For every interactive UI element, specify trigger, enabled/disabled conditions, loading,
   success, empty, error and permission states, persisted result, and downstream dependency.
9. Create a requirements-quality checklist but leave reviewer decisions unchecked.

Output: `spec.md`, `checklists/requirements.md`, and `.specify/feature.json` when using the canonical
layout. Stop before technical planning.

## 3. Clarify

Purpose: eliminate material ambiguity before technical planning.

Procedure:

1. Scan scope, actors, workflows, states, data, permissions, failures, integrations, non-functional
   constraints, and acceptance coverage.
2. Rank ambiguity by impact. Ask no more than five focused questions in a clarification pass.
3. Ask one decision at a time when answers are dependent. Offer mutually exclusive options when
   useful and allow free-form input.
4. Write confirmed answers back into the most relevant specification section immediately.
5. Preserve unresolved items as explicit markers. Never infer approval from silence.
6. Revalidate requirements and acceptance scenarios after edits.

Output: updated `spec.md` with a clarification log. Stop when no high-impact ambiguity remains or
the question limit is reached.

## 4. Plan

Purpose: translate an approved specification into implementable technical design.

Prerequisite: approved `spec.md`; unresolved material clarifications block planning.

Procedure:

1. Inspect the current codebase, dependencies, schemas, APIs, build/test tooling, and deployment
   constraints before choosing architecture.
2. Check every decision against the constitution.
3. Resolve technical unknowns through primary documentation or direct repository evidence. Record
   decisions and rejected alternatives in `research.md`.
4. Define components, boundaries, interfaces, data models, state transitions, error handling,
   permission enforcement, migration needs, observability, and test strategy.
5. Map each functional requirement and acceptance scenario to one or more technical touchpoints.
6. For UI capabilities, identify the owning component, state source, event handler, service/API,
   persistence behavior, and verification route. A layout-only component cannot satisfy a
   behavioral requirement.
7. Record setup and validation scenarios in `quickstart.md` when useful.

Outputs: `plan.md` plus only the supporting artifacts the feature needs: `research.md`,
`data-model.md`, `contracts/`, and `quickstart.md`.

## 5. Checklist

Purpose: create tests for the quality of requirements, not tests for application behavior.

Procedure:

1. Choose a checklist focus such as UX, API, security, data, AI behavior, release, or operations.
2. Phrase each item so a reviewer can decide it from the requirements and plan.
3. Test completeness, clarity, consistency, measurability, boundary coverage, failure coverage, and
   traceability.
4. Include concrete source references (`FR-003`, `US2/AC1`, plan section name).
5. Exclude implementation verification such as “click the button and confirm it works.” That
   belongs to tests and convergence.
6. Leave every subjective or approval-dependent item unchecked.

Output: a focused checklist under `checklists/`.

## 6. Tasks

Purpose: convert the approved plan into an executable implementation sequence.

Prerequisites: approved `spec.md`, complete `plan.md`, and required supporting artifacts.

Procedure:

1. Organize tasks by user story or independently testable increment, with setup and shared
   foundations preceding dependent work.
2. Give every task a stable ID (`T001`), exact action, target file or artifact, source requirement,
   dependency, and verification method.
3. Mark a task parallel only when it changes different files and has no unresolved dependency.
4. Include tests before corresponding implementation when the plan adopts test-first development.
5. Include data migrations, permissions, failure states, observability, integration wiring, and
   release configuration when required by the specification.
6. Reject tasks such as “build the page” when the feature also requires services, persistence,
   role behavior, or error handling. Split by verifiable capability.
7. Define the completion evidence expected for each task or phase.

Output: `tasks.md`. Stop before writing application code.

## 7. Analyze

Purpose: read-only consistency and coverage analysis before implementation.

Procedure:

1. Load the constitution, `spec.md`, `plan.md`, `tasks.md`, and required supporting artifacts.
2. Detect duplication, ambiguity, underspecification, contradictions, constitution violations,
   orphan requirements, unmapped plan decisions, missing tasks, and untestable completion claims.
3. Build a requirement-to-task coverage map.
4. Grade findings as CRITICAL, HIGH, MEDIUM, or LOW using `verification.md`.
5. Report recommended remediation and affected artifacts. Do not edit any artifact during analyze.

Output: an analysis report and a gate result. Any CRITICAL issue blocks implementation.

## 8. Implement

Purpose: execute approved tasks while preserving traceability and producing fresh evidence.

Procedure:

1. Verify all mandatory pre-implementation checklists and approvals.
2. Execute tasks in dependency order. Complete setup and shared foundations before story work.
3. Run relevant tests and validation at each checkpoint. Halt on failure that invalidates dependent
   work.
4. Mark a task complete only after inspecting the changed files and obtaining its required evidence.
5. Record deviations from the plan. Material changes require returning to the affected artifact and
   obtaining approval; do not hide them in code.
6. At phase end, compare delivered behavior with acceptance scenarios, including loading, empty,
   error, permission, persistence, and recovery states.

Output: code and tests, updated task checkboxes, and a completion report containing commands and
results. “Tests passed” alone does not prove all requirements were met.

## 9. Converge

Purpose: find the gap between approved intent and current implementation after an implement pass.

Procedure:

1. Load the constitution, specification, plan, tasks, code, tests, and current runtime evidence.
2. Recheck every requirement, acceptance scenario, technical decision, and task regardless of its
   checkbox state.
3. Classify each gap as `missing`, `partial`, `contradicts`, or `unrequested`.
4. Present severity-graded findings before writing.
5. If actionable gaps exist, append one new `## Phase N: Convergence` section to `tasks.md`. Add
   traceable tasks with new IDs. Never rewrite, renumber, delete, or reorder existing tasks.
6. Do not modify application code, `spec.md`, or `plan.md` during convergence.
7. If no gap exists, leave `tasks.md` byte-for-byte unchanged and report `converged` with the
   evidence checked.

Output: convergence report and, only when needed, an append-only convergence phase in `tasks.md`.

## 10. Tasks to issues

Purpose: publish an approved task list to the user's issue tracker.

Rules:

- Run only on explicit request and only after resolving the repository and destination tracker.
- Preserve task IDs, requirement references, dependencies, acceptance evidence, and grouping.
- Preview the issue set before creating external records when recipients, repository, or scope are
  ambiguous.
- Do not expose credentials or place secrets in issue content.
