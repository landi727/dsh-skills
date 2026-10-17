#!/usr/bin/env python3
"""Aggregate Agent Skill evaluation results stored as JSON."""

from __future__ import annotations

import argparse
import json
import statistics
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any


def _mean(values: list[float]) -> float | None:
    return statistics.fmean(values) if values else None


def _stdev(values: list[float]) -> float | None:
    return statistics.stdev(values) if len(values) > 1 else (0.0 if values else None)


def _rounded(value: float | None) -> float | None:
    return round(value, 3) if value is not None else None


def _criterion_score(item: dict[str, Any]) -> float | None:
    kind = item.get("type")
    if kind == "binary" and isinstance(item.get("passed"), bool):
        return 1.0 if item["passed"] else 0.0
    if kind == "scale":
        score = item.get("score")
        maximum = item.get("max_score")
        if (
            isinstance(score, (int, float))
            and not isinstance(score, bool)
            and isinstance(maximum, (int, float))
            and not isinstance(maximum, bool)
            and maximum > 0
            and 0 <= score <= maximum
        ):
            return float(score) / float(maximum)
    return None


def aggregate(data: Any) -> tuple[dict[str, Any] | None, list[str]]:
    errors: list[str] = []
    if not isinstance(data, dict):
        return None, ["Root must be a JSON object."]
    runs = data.get("runs")
    if not isinstance(runs, list) or not runs:
        return None, ["runs must be a non-empty array."]

    by_configuration: dict[str, dict[str, list[float]]] = defaultdict(
        lambda: {
            "scores": [],
            "durations": [],
            "tokens": [],
            "run_records": [],
            "binary_passes": [],
        }
    )
    cases_by_configuration: dict[str, set[str]] = defaultdict(set)

    for index, run in enumerate(runs):
        prefix = f"runs[{index}]"
        if not isinstance(run, dict):
            errors.append(f"{prefix} must be an object.")
            continue
        configuration = run.get("configuration")
        case_id = run.get("case_id")
        if not isinstance(configuration, str) or not configuration.strip():
            errors.append(f"{prefix}.configuration must be a non-empty string.")
            continue
        if not isinstance(case_id, str) or not case_id.strip():
            errors.append(f"{prefix}.case_id must be a non-empty string.")
            continue
        criteria = run.get("criteria")
        if not isinstance(criteria, list):
            errors.append(f"{prefix}.criteria must be an array.")
            continue

        configuration_values = by_configuration[configuration]
        configuration_values["run_records"].append(1.0)
        weighted_scores: list[tuple[float, float]] = []
        for item in criteria:
            if not isinstance(item, dict):
                continue
            score = _criterion_score(item)
            weight = item.get("weight", 1)
            if score is not None and isinstance(weight, (int, float)) and not isinstance(weight, bool) and weight > 0:
                weighted_scores.append((score, float(weight)))
            if item.get("type") == "binary" and isinstance(item.get("passed"), bool):
                configuration_values["binary_passes"].append(1.0 if item["passed"] else 0.0)
        if weighted_scores:
            numerator = sum(score * weight for score, weight in weighted_scores)
            denominator = sum(weight for _, weight in weighted_scores)
            configuration_values["scores"].append((numerator / denominator) * 100)
        cases_by_configuration[configuration].add(case_id)

        duration = run.get("duration_seconds")
        if isinstance(duration, (int, float)) and not isinstance(duration, bool) and duration >= 0:
            by_configuration[configuration]["durations"].append(float(duration))
        tokens = run.get("tokens")
        if isinstance(tokens, int) and not isinstance(tokens, bool) and tokens >= 0:
            by_configuration[configuration]["tokens"].append(float(tokens))

    if errors:
        return None, errors

    summary: dict[str, Any] = {
        "skill_name": data.get("skill_name"),
        "configurations": {},
    }
    for configuration, values in sorted(by_configuration.items()):
        summary["configurations"][configuration] = {
            "cases": len(cases_by_configuration[configuration]),
            "runs": len(values["run_records"]),
            "scored_runs": len(values["scores"]),
            "quality_mean": _rounded(_mean(values["scores"])),
            "quality_stdev": _rounded(_stdev(values["scores"])),
            "binary_pass_rate": _rounded(_mean(values["binary_passes"])),
            "duration_mean_seconds": _rounded(_mean(values["durations"])),
            "tokens_mean": _rounded(_mean(values["tokens"])),
        }

    pairwise = data.get("pairwise", [])
    if pairwise is not None and not isinstance(pairwise, list):
        return None, ["pairwise must be an array when provided."]
    counts = {"candidate": 0, "baseline": 0, "tie": 0}
    for index, judgment in enumerate(pairwise or []):
        if not isinstance(judgment, dict) or judgment.get("winner") not in counts:
            return None, [f"pairwise[{index}].winner must be candidate, baseline, or tie."]
        counts[judgment["winner"]] += 1
    if pairwise:
        total = len(pairwise)
        summary["pairwise"] = {
            **counts,
            "candidate_win_rate": round(counts["candidate"] / total, 3),
            "non_loss_rate": round((counts["candidate"] + counts["tie"]) / total, 3),
        }

    candidate = summary["configurations"].get("candidate")
    baseline = summary["configurations"].get("baseline")
    if candidate and baseline:
        c_score = candidate.get("quality_mean")
        b_score = baseline.get("quality_mean")
        if c_score is not None and b_score is not None:
            summary["candidate_quality_delta"] = round(c_score - b_score, 3)

    return summary, []


def _self_test() -> int:
    fixture = {
        "skill_name": "example",
        "runs": [
            {
                "case_id": "a",
                "configuration": "candidate",
                "run": 1,
                "criteria": [{"id": "x", "type": "binary", "passed": True}],
                "duration_seconds": 2,
                "tokens": 100,
            },
            {
                "case_id": "a",
                "configuration": "baseline",
                "run": 1,
                "criteria": [{"id": "x", "type": "binary", "passed": False}],
                "duration_seconds": 1,
                "tokens": 80,
            },
        ],
        "pairwise": [{"case_id": "a", "run": 1, "winner": "candidate"}],
    }
    summary, errors = aggregate(fixture)
    if errors or summary is None or summary.get("candidate_quality_delta") != 100.0:
        print(f"Self-test failed: {errors or summary}")
        return 1
    print("Self-test passed.")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("results", nargs="?", type=Path)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()

    if args.self_test:
        return _self_test()
    if args.results is None:
        parser.error("results is required unless --self-test is used")

    try:
        data = json.loads(args.results.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"Invalid results file: {exc}")
        return 1

    summary, errors = aggregate(data)
    if errors:
        print("Results are invalid:")
        for error in errors:
            print(f"- {error}")
        return 1

    rendered = json.dumps(summary, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        args.output.write_text(rendered, encoding="utf-8")
        print(f"Wrote {args.output}")
    else:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    sys.exit(main())
