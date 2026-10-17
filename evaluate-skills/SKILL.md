---
name: evaluate-skills
description: Evaluate and improve existing Agent Skills with realistic cases, explicit criteria, matched baselines, blind comparison, and bounded benchmarks. Use when the user asks to test, assess, optimize, compare versions of, or benchmark a skill, or when skill-creator hands off a complex draft for evidence-based validation. Do not use for general questions about skills, initial drafting, or format-only validation.
---

# Evaluate Skills

Evaluate whether a skill improves real task performance, then make only evidence-backed revisions. Work as a companion to the system `skill-creator`: let `skill-creator` create, edit, validate, install, and remove skills; use this skill to test behavior and support improvement claims.

## Route the request

Choose the smallest evaluation that can support the user's claim:

1. **Inspection** — Review instructions, trigger scope, resources, and likely failure modes. Use when the user asks for an assessment without requesting task runs. Do not claim proven performance.
2. **Smoke test** — Run 2-3 varied cases once with the skill. Use after a simple skill or a narrow change to catch obvious failures. Add a baseline only when claiming that the skill improves results.
3. **Version comparison** — Run 3-5 cases against a matched baseline. Use by default for meaningful revisions or when the user asks whether a new version is better. Apply blind comparison to subjective outputs.
4. **Benchmark** — Run 5-10 cases multiple times per configuration and report variance. Use only when the user explicitly requests a benchmark or needs a stability claim. Explain the run count and likely cost before starting; obtain approval when the run is likely to be lengthy or expensive.

Treat structural validity, observed case performance, and demonstrated stability as different evidence levels. Never convert a successful format check into a performance claim.

## Establish the evaluation contract

Before seeing candidate outputs, record:

- the decision the evaluation must support;
- the candidate skill and exact baseline;
- representative, boundary, and near-miss cases;
- success criteria and their evidence type;
- allowed run count and stopping condition.

For a new skill, use no skill as the baseline. For an updated skill, snapshot the prior version before editing and use that snapshot. Use another named skill only when the comparison question specifically requires it.

Use `references/evaluation-protocol.md` for case design, role isolation, grading, and reporting. Store the plan as `evals/evals.json` when the evaluation will be repeated. Validate it with:

```bash
python3 scripts/validate_eval_plan.py evals/evals.json
```

## Run matched evaluations

1. Preserve the candidate and baseline exactly as tested.
2. Give each executor the same task prompt, files, tool access, model class, and output requirements. Change only the skill condition.
3. Run candidate and baseline cases in the same evaluation window. Parallelize independent runs when subagents are available.
4. Keep executors blind to expected answers, suspected defects, intended fixes, and competing outputs.
5. Capture the final output plus available duration and token usage. Do not infer missing telemetry.
6. Grade objective requirements with deterministic checks where practical. Use an independent grader for rubric judgments.
7. For subjective quality, anonymize and randomize the two outputs before pairwise comparison. Permit ties and require evidence.
8. Ask the user to review outputs when taste, voice, domain judgment, or acceptance depends on them. Human review outranks aggregate scores in these areas.

Do not spawn a full comparison merely because this skill triggered. Match the number of agents and runs to the selected tier. Follow the host's authorization rules for subagents and external effects.

## Analyze results

Check more than the overall score:

- which cases distinguish candidate from baseline;
- which criteria pass for both and add little evidence;
- repeated failure patterns across cases;
- regressions introduced by the candidate;
- score variance or inconsistent pairwise choices;
- quality gains relative to time and token cost;
- cases where the grader lacked enough evidence.

If run data follows `references/evaluation-protocol.md`, aggregate it with:

```bash
python3 scripts/aggregate_results.py results.json
```

Use cautious claim language:

- **Structurally valid** — format and required files pass validation.
- **Promising** — a small smoke test found no material failure.
- **Better on tested cases** — the candidate beat the matched baseline on the named set.
- **Stable within tested scope** — repeated runs show acceptable variance across the named set.

Do not generalize beyond the tested cases, model, tools, or environment.

## Improve without overfitting

Translate feedback into the smallest reusable change that explains several failures. Prefer clearer reasoning, routing, reusable scripts, or references over case-specific rules. Remove instructions that add cost without improving results.

After a revision:

1. rerun every earlier case as regression coverage;
2. add one materially different case when the change may be overfit;
3. compare against the same baseline unless the user's decision has changed;
4. stop when the acceptance threshold is met, progress stalls, or the next iteration would exceed the agreed budget.

Do not silently rewrite or install the target skill when the user requested evaluation only. Hand approved revisions back to `skill-creator` for validation and saving.

## Report the outcome

Lead with the decision supported by the evidence. Include:

1. scope: candidate, baseline, cases, runs, model/tools;
2. result: wins, ties, losses, requirement pass rate, and variance when available;
3. observed strengths and failures with case-level evidence;
4. cost or latency tradeoffs when measured;
5. claim strength and remaining uncertainty;
6. the smallest recommended revision or a clear no-change conclusion.

Keep raw evaluation files available when created, but do not overwhelm the user with internal bookkeeping.
