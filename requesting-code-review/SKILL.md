---
name: requesting-code-review
description: Use when completing tasks, implementing major features, or before merging to verify work meets requirements
---

## Work environment integration

This is a Work-compatible import of [Superpowers](https://github.com/obra/superpowers/tree/8ca22dba9a94f28898bbce59f2537ff4d87c747d/skills/requesting-code-review). Preserve the independent review method and read the bundled `code-reviewer.md` before dispatch.

- Map `Task`, `superpowers:code-reviewer`, and `Subagent` examples to the native collaboration tool. Dispatch a fresh read-only reviewer with `fork_turns="none"`, a project path, the exact request/spec, and the relevant base/head or patch. Reviewer labels name roles, not installed extra skills. Use available host model rules; never assume an external launcher.
- Capture the real base before implementation, or resolve the actual branch merge-base for a branch review. Use `HEAD~1` only for an explicitly single-commit scope. Review all changes within the requested scope, including relevant uncommitted changes when that is what the user asks to review; describe the committed and working-tree inputs separately.
- Give the reviewer raw requirements, relevant project constraints, code/diff paths, and existing test evidence. Do not give it the implementer's desired verdict or parent history. Ask it to inspect the actual changes and return findings with file/line, severity, impact, evidence, and correction.
- A request for review authorizes read-only inspection. Fixes, commit, merge, publish, and other external actions follow the user's actual session authorization. Protect pre-existing user work; do not commit or stash everything merely to create a clean review input.
- This review cannot certify rendered visual fidelity or animation from source alone. Record missing runtime/visual evidence as unverified; use the project's appropriate visual and motion checks when authorized.
- Do not install skills mentioned in upstream examples. For feedback, independently verify whether each finding is valid, fix Critical/Important issues in the authorized implementation scope, record deferred/minor issues, and challenge mistaken findings with evidence. Do not let a positive review replace required project checks.

Source version and original hashes are in `references/source.json`; preserve `LICENSE`.


# Requesting Code Review

Dispatch a code reviewer subagent to catch issues before they cascade. The reviewer gets precisely crafted context for evaluation — never your session's history.

**Core principle:** Review early, review often.

## When to Request Review

**Mandatory:**
- After each task in subagent-driven development
- After completing major feature
- Before merge to main

**Optional but valuable:**
- When stuck (fresh perspective)
- Before refactoring (baseline check)
- After fixing complex bug

## How to Request

**1. Get git SHAs:**
```bash
BASE_SHA=$(git rev-parse HEAD~1)  # or: git merge-base origin/main HEAD
HEAD_SHA=$(git rev-parse HEAD)
```

**2. Dispatch code reviewer subagent:**

Dispatch a `general-purpose` subagent, filling the template at [code-reviewer.md](code-reviewer.md)

**Placeholders:**
- `{DESCRIPTION}` - Brief summary of what you built
- `{PLAN_OR_REQUIREMENTS}` - What it should do
- `{BASE_SHA}` - Starting commit
- `{HEAD_SHA}` - Ending commit

**3. Act on feedback:**
- Fix Critical issues immediately
- Fix Important issues before proceeding
- Note Minor issues for later
- Push back if reviewer is wrong (with reasoning)

## Example

```
[Just completed Task 2: Add verification function]

You: Let me request code review before proceeding.

BASE_SHA=$(git log --oneline | grep "Task 1" | head -1 | awk '{print $1}')
HEAD_SHA=$(git rev-parse HEAD)

[Dispatch code reviewer subagent]
  DESCRIPTION: Added verifyIndex() and repairIndex() with 4 issue types
  PLAN_OR_REQUIREMENTS: Task 2 from docs/superpowers/plans/deployment-plan.md
  BASE_SHA: a7981ec
  HEAD_SHA: 3df7661

[Subagent returns]:
  Strengths: Clean architecture, real tests
  Issues:
    Important: Missing progress indicators
    Minor: Magic number (100) for reporting interval
  Assessment: Ready to proceed

You: [Fix progress indicators]
[Continue to Task 3]
```

## Common Rationalizations

| Excuse | Reality |
|--------|---------|
| "I'll just review the diff myself instead of dispatching a reviewer" | You're the coordinator — reviewing the diff inline burns the context window you need to keep driving the work. Dispatch a reviewer subagent: the diff and the evaluation live in its context, and only the findings come back to you. |
| "The reviewer needs my whole session history to understand the change" | Hand it precisely crafted context, never your session's history. That keeps the reviewer on the work product, not your thought process. |

## Red Flags

**Never:**
- Skip review because "it's simple"
- Ignore Critical issues
- Proceed with unfixed Important issues
- Argue with valid technical feedback

**If reviewer wrong:**
- Push back with technical reasoning
- Show code/tests that prove it works
- Request clarification

See template at: [code-reviewer.md](code-reviewer.md)
