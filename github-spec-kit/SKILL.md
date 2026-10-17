---
name: github-spec-kit
description: Apply GitHub Spec Kit's specification-driven development workflow to a real software project. Use when the user explicitly asks for GitHub Spec Kit, Spec Kit, specification-driven development, or wants to create or advance project constitution, feature specification, clarification, technical plan, requirements checklist, implementation tasks, cross-artifact analysis, implementation, or post-implementation convergence. Operate on project files and code when available. Do not use for a standalone readiness audit; use assess-document-development-readiness for that.
---

# GitHub Spec Kit

Use a stage-gated specification-driven workflow adapted from
[`github/spec-kit`](https://github.com/github/spec-kit). Treat specifications as the source of
intent and code as evidence of implementation.

This personal skill combines the upstream command suite into one dispatcher. Preserve upstream
stage boundaries and artifact names. Do not claim that this skill installs or replaces the
upstream `specify-cli` inside a user's repository.

## Route the request

Map the request to exactly one stage unless the user explicitly names several stages and supplies
approval to run them together:

1. `constitution` — establish project-wide non-negotiable principles.
2. `specify` — define one feature in terms of user need and observable behavior.
3. `clarify` — resolve high-impact ambiguity in the current specification.
4. `plan` — translate an approved specification into technical decisions and design artifacts.
5. `checklist` — create reviewer-owned tests for requirement quality.
6. `tasks` — produce an ordered, traceable implementation task list.
7. `analyze` — perform read-only consistency analysis across artifacts.
8. `implement` — execute approved tasks and record fresh verification evidence.
9. `converge` — compare the current codebase with all approved artifacts and append remaining work.
10. `taskstoissues` — publish approved tasks to an issue tracker only when the user explicitly asks
    and the tracker is available.

Read [references/stages.md](references/stages.md) before executing any stage. Read
[references/artifact-contracts.md](references/artifact-contracts.md) whenever creating or editing
artifacts. For `analyze`, `implement`, or `converge`, also read
[references/verification.md](references/verification.md).

## Establish project context

1. Resolve the current project root from the user's named project or current working directory.
2. Read applicable project instructions and inspect existing `.specify/`, `specs/`, documentation,
   source, tests, and configuration. Use `rg --files` and targeted reads; do not assume the project
   is empty.
3. If multiple products or repositories are accessible, stay within the project named by the user.
   Do not import documents, decisions, or code from adjacent projects.
4. If the requested stage needs a missing prerequisite, stop and name the missing artifact and the
   exact preceding stage required. Do not synthesize upstream approval.
5. When there is no writable project workspace, produce the requested artifact in the user's
   requested destination and mark file-dependent checks as unverified.

## Enforce stage boundaries

- Complete only the selected stage, report its result, and stop. Suggest the next eligible stage
  without executing it.
- Do not let approval of an earlier artifact authorize later planning, coding, deployment, or
  release work.
- Do not move from UI structure to implementation by inference. A visible control is a requirement
  only when its trigger, states, outcome, failure behavior, persistence, permissions, and dependent
  service or data are specified.
- Never convert placeholders, disabled controls, mock data, or static routes into completion claims.
- Do not include estimated duration, schedule, or staffing effort unless the current user request
  explicitly asks for it.
- Preserve explicit user decisions. Mark missing decisions as assumptions or clarification needs;
  do not silently decide material product behavior.

## Maintain the artifact chain

Use these canonical locations when the repository already follows Spec Kit conventions:

```text
.specify/memory/constitution.md
.specify/feature.json
specs/<feature>/spec.md
specs/<feature>/checklists/requirements.md
specs/<feature>/plan.md
specs/<feature>/research.md
specs/<feature>/data-model.md
specs/<feature>/contracts/
specs/<feature>/quickstart.md
specs/<feature>/tasks.md
```

Do not create empty artifacts merely to satisfy the directory structure. For a project with an
established equivalent structure, preserve it and record the mapping instead of duplicating files.

Maintain traceability:

```text
user story / acceptance scenario
→ functional requirement
→ technical decision or contract
→ implementation task
→ code location
→ test or runtime evidence
```

Every mandatory capability must reach the end of the chain before `converged` can be reported.

## Apply approval and evidence rules

- Label artifacts as `draft`, `review-ready`, `approved`, or `blocked`. Only the user or designated
  reviewer can make an artifact `approved`.
- Treat generated checklists as reviewer-owned. Leave boxes unchecked unless the reviewer supplies
  a decision or direct evidence supports an objective check. Never self-approve the stage.
- Separate document completeness, implementation completion, test success, and production
  readiness. Report each independently.
- Require fresh command output, runtime observation, or directly inspected code for completion
  claims. Prior agent reports and checked task boxes are leads, not evidence.
- If evidence is unavailable, use `unverified`; do not substitute confidence language.

## Report the stage result

Return:

1. Stage executed and artifact paths affected.
2. Result: `blocked`, `review-ready`, `approved input processed`, `implemented with evidence`, or
   `converged`.
3. Blocking issues and unresolved decisions, each linked to its source artifact.
4. Verification performed and verification still missing.
5. The single next eligible Spec Kit stage. Do not launch it automatically.

## Source fidelity

This adaptation follows the upstream SDD stages and canonical artifacts from GitHub Spec Kit. It
adds local safeguards for project isolation, explicit approval, behavioral UI requirements, fresh
evidence, and omission of unsolicited time estimates. When upstream behavior and this skill differ,
state the difference instead of presenting the adaptation as an upstream feature.
