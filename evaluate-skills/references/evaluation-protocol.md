# Evaluation protocol

Use this reference when preparing or running behavioral evaluations. Keep the test artifact separate from the target skill so the skill cannot learn the expected answers.

## Case design

Build cases from real user language and actual task variation:

- representative: the central job the skill should perform;
- boundary: difficult inputs, missing information, or competing constraints;
- near-miss: similar wording where the skill should stay out or narrow its behavior;
- regression: a case that previously exposed a failure.

Avoid several prompts that test the same behavior with superficial wording changes. A small diverse set is stronger than a large repetitive set.

## Criteria design

Write criteria before seeing outputs. Each criterion should identify one observable property and its evidence source.

- `binary`: objectively pass or fail; prefer a deterministic check.
- `scale`: score from 0 to `max_score` using anchored descriptions.
- `human`: requires domain, taste, or acceptance judgment; record feedback without converting it into fake precision.

Use weights only when the decision genuinely values criteria differently. A requirement that both versions always pass is useful for regression protection, yet it does not support a superiority claim.

## Role isolation

### Executor

Provide only the target skill condition, task prompt, input files, allowed tools, and output location. Do not reveal the expected answer, rubric, competing condition, suspected defect, or intended change.

### Grader

Provide the task, criteria, output, and source evidence needed to verify it. Ask for a result per criterion with concise evidence. Do not reveal which version the output came from.

### Comparator

Label paired outputs `A` and `B` using a randomized order. Ask for `A`, `B`, or `tie`, confidence from 0 to 1, and the decisive evidence. Do not reveal candidate identity until the judgment is complete.

### Analyzer

Review case-level grades, pairwise judgments, timing, tokens, and user feedback. Identify non-discriminating criteria, flaky cases, regressions, and cost-quality tradeoffs. Do not use the average score as the sole conclusion.

## Evaluation plan schema

Store repeated plans as JSON:

```json
{
  "skill_name": "example-skill",
  "objective": "Determine whether the revision improves task quality without regressions.",
  "baseline": {"type": "snapshot", "label": "previous-version"},
  "runs_per_configuration": 1,
  "cases": [
    {
      "id": "representative-case",
      "prompt": "A realistic user request",
      "expected": "A concise description of acceptable behavior",
      "files": [],
      "criteria": [
        {
          "id": "required-coverage",
          "description": "Covers every required item from the supplied source.",
          "type": "binary",
          "weight": 1
        }
      ]
    }
  ]
}
```

`baseline.type` must be `without_skill`, `snapshot`, or `named`. Criterion type must be `binary`, `scale`, or `human`. A scale criterion also requires an integer `max_score` greater than 1.

## Results schema

Store machine-aggregated runs as JSON:

```json
{
  "skill_name": "example-skill",
  "runs": [
    {
      "case_id": "representative-case",
      "configuration": "candidate",
      "run": 1,
      "criteria": [
        {"id": "required-coverage", "type": "binary", "passed": true, "evidence": "All required items appear."}
      ],
      "duration_seconds": 12.4,
      "tokens": 4200
    }
  ],
  "pairwise": [
    {
      "case_id": "representative-case",
      "run": 1,
      "winner": "candidate",
      "confidence": 0.8,
      "evidence": "The candidate is more complete and equally concise."
    }
  ]
}
```

For scale results, use `score` and `max_score`. Omit unavailable timing or token fields instead of estimating them. Human-only criteria may remain outside the aggregate and appear in the report as qualitative evidence.

## Comparison discipline

- Keep model, tools, inputs, and output contract matched.
- Run both conditions close together to reduce environmental drift.
- Randomize pairwise presentation order.
- Preserve ties; forced winners exaggerate weak differences.
- Treat missing or contradictory evidence as uncertainty.
- Recheck earlier cases after every revision.

## Minimum report

Report the candidate and baseline, case coverage, run count, model and tools, objective results, pairwise results, regressions, measured costs, user feedback, supported claim, and remaining uncertainty.
