# Artifact contracts

## Contents

1. General rules
2. Constitution
3. Specification
4. Technical plan
5. Tasks
6. Traceability
7. Status and approvals

## 1. General rules

- Preserve stable IDs after publication. Deprecate or supersede an item instead of silently
  reusing its ID.
- Distinguish confirmed facts, user decisions, assumptions, open questions, and agent proposals.
- Record exclusions and deferred capabilities explicitly.
- Use exact source paths and named sections when referencing code or another artifact.
- Keep product behavior in `spec.md`; keep implementation choices in `plan.md`.
- Do not add schedules or effort estimates by default.

## 2. Constitution

Minimum structure:

```markdown
# Project Constitution

Version: X.Y.Z
Ratified: YYYY-MM-DD
Last amended: YYYY-MM-DD

## Principles
### I. <Name>
<Testable normative rule and rationale>

## Governance
<Amendment, versioning, approval, and compliance rules>
```

## 3. Specification

Minimum structure:

```markdown
# Feature: <Name>

Status: draft | review-ready | approved | blocked

## Scope
### Included
### Excluded

## Actors and permissions

## User stories
### US1 — <Outcome> (P1)
#### Acceptance scenarios
- Given ... When ... Then ...

## Edge and failure cases

## Functional requirements
- FR-001: The system MUST ...

## Key entities

## Success criteria
- SC-001: ...

## Assumptions

## Clarifications
```

For interactive interfaces, every relevant requirement must define:

- actor and permission;
- entry condition and trigger;
- enabled and disabled behavior;
- loading, empty, success, error, conflict, and recovery states as applicable;
- data read or written;
- persistence and refresh behavior;
- downstream service or integration;
- observable acceptance evidence.

## 4. Technical plan

Minimum structure:

```markdown
# Implementation Plan: <Feature>

## Context and constraints
## Constitution check
## Current-system findings
## Architecture and component boundaries
## Data model and lifecycle
## Interfaces and contracts
## UI state and event model
## Permissions and security
## Failure and recovery
## Observability
## Test strategy
## Migration and release constraints
## Requirement mapping
## Open decisions
```

Every material technical choice must identify its source requirement and rationale.

## 5. Tasks

Each task follows this contract:

```markdown
- [ ] T001 [P?] <imperative action> in `<path>`
  - Source: FR-001, US1/AC2, plan:<section>
  - Depends on: T000 or none
  - Done when: <observable evidence>
```

Task phases must reflect dependency order. User-story phases should remain independently testable
where the architecture permits.

## 6. Traceability

Maintain a compact mapping in `plan.md`, `tasks.md`, or the analysis report:

| Intent | Plan/contract | Tasks | Code | Evidence | Status |
|---|---|---|---|---|---|
| FR-001 | plan:Auth flow | T014–T018 | `src/...` | test/runtime | open/verified |

Use `unmapped` and `unverified` explicitly. Empty cells conceal gaps.

## 7. Status and approvals

- `draft`: still being authored; may contain material unknowns.
- `review-ready`: internally consistent enough for human review.
- `approved`: explicitly accepted by the user or designated reviewer.
- `blocked`: cannot advance because a decision, prerequisite, or critical inconsistency is missing.

An agent can produce `review-ready`. It cannot infer `approved` from its own checklist or analysis.
