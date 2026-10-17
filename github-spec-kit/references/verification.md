# Verification and convergence

## Contents

1. Evidence hierarchy
2. Analysis severity
3. Coverage checks
4. Completion claims
5. Convergence append contract

## 1. Evidence hierarchy

Prefer evidence in this order:

1. Fresh runtime observation of the required behavior.
2. Fresh automated test output that directly exercises the requirement.
3. Direct code and configuration inspection showing the complete path.
4. Static artifact mapping with no runtime verification.
5. Prior reports, task checkboxes, screenshots of appearance, or agent claims.

Levels 4 and 5 cannot independently prove behavioral completion.

For a user-facing capability, verify the full chain where applicable:

```text
visible control
→ event handler
→ state transition
→ service/API
→ data or external effect
→ success/failure feedback
→ persisted or recoverable result
```

## 2. Analysis severity

- `CRITICAL`: constitution MUST violation; missing prerequisite; security/data-loss risk; or absent
  baseline behavior for a P1 story.
- `HIGH`: missing or contradictory core functional requirement, acceptance scenario, permission,
  integration, or persistence path.
- `MEDIUM`: partial secondary behavior, weak failure handling, ambiguous task coverage, or
  unrequested work requiring review.
- `LOW`: limited polish, documentation mismatch, or low-risk cleanup that does not block the
  specified journey.

Critical findings block implementation. High findings block completion and convergence.

## 3. Coverage checks

For `analyze` and `converge`, check:

- Every user story has acceptance scenarios.
- Every functional requirement maps to a plan decision or contract.
- Every buildable requirement maps to one or more tasks.
- Every behavioral task maps to code and direct evidence after implementation.
- Permission enforcement exists at the authoritative layer, not only in UI visibility.
- Data creation, validation, persistence, update, deletion, and recovery are covered where relevant.
- Interactive UI controls have working handlers and all specified states.
- AI or external-service features define input constraints, output handling, failure, retry, and
  human fallback where required.
- Release and configuration requirements are represented in tasks and evidence when in scope.

## 4. Completion claims

Before marking a task or phase complete:

1. Identify the exact claim.
2. Select evidence that directly proves it.
3. Run or inspect the evidence now.
4. Read the full result and exit status.
5. Compare it with the source requirement and acceptance scenario.
6. Report what is proven and what remains unverified.

Do not use broad statements such as “all functionality works” when only build or unit tests were
run. Report separate verdicts for:

- artifact completeness;
- implementation completeness;
- automated test status;
- observed interaction status;
- production readiness.

## 5. Convergence append contract

Convergence may write only one new section at the end of `tasks.md`:

```markdown
## Phase N: Convergence

- [ ] T042 <imperative remediation> per FR-003 (missing)
```

Rules:

- Assign IDs after the current maximum.
- Order CRITICAL and HIGH findings first.
- Include source reference and gap type: `missing`, `partial`, `contradicts`, or `unrequested`.
- Preserve all existing text and task states.
- When there are no actionable findings, make no file change.
- Convergence identifies remaining work; implementation performs it in a later, separately approved
  stage.
