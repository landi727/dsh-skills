#!/usr/bin/env python3
"""Validate an Agent Skill evaluation plan stored as JSON."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


BASELINE_TYPES = {"without_skill", "snapshot", "named"}
CRITERION_TYPES = {"binary", "scale", "human"}


def _nonempty_string(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def validate_plan(data: Any) -> list[str]:
    errors: list[str] = []
    if not isinstance(data, dict):
        return ["Root must be a JSON object."]

    for field in ("skill_name", "objective"):
        if not _nonempty_string(data.get(field)):
            errors.append(f"{field} must be a non-empty string.")

    baseline = data.get("baseline")
    if not isinstance(baseline, dict):
        errors.append("baseline must be an object.")
    else:
        if baseline.get("type") not in BASELINE_TYPES:
            errors.append("baseline.type must be without_skill, snapshot, or named.")
        if not _nonempty_string(baseline.get("label")):
            errors.append("baseline.label must be a non-empty string.")

    runs = data.get("runs_per_configuration")
    if not isinstance(runs, int) or isinstance(runs, bool) or runs < 1:
        errors.append("runs_per_configuration must be an integer greater than 0.")

    cases = data.get("cases")
    if not isinstance(cases, list) or not cases:
        errors.append("cases must be a non-empty array.")
        return errors

    seen_case_ids: set[str] = set()
    for case_index, case in enumerate(cases):
        prefix = f"cases[{case_index}]"
        if not isinstance(case, dict):
            errors.append(f"{prefix} must be an object.")
            continue

        case_id = case.get("id")
        if not _nonempty_string(case_id):
            errors.append(f"{prefix}.id must be a non-empty string.")
        elif case_id in seen_case_ids:
            errors.append(f"{prefix}.id duplicates '{case_id}'.")
        else:
            seen_case_ids.add(case_id)

        if not _nonempty_string(case.get("prompt")):
            errors.append(f"{prefix}.prompt must be a non-empty string.")
        if "expected" in case and not _nonempty_string(case.get("expected")):
            errors.append(f"{prefix}.expected must be a non-empty string when provided.")
        if "files" in case and not (
            isinstance(case.get("files"), list)
            and all(_nonempty_string(item) for item in case["files"])
        ):
            errors.append(f"{prefix}.files must be an array of non-empty strings.")

        criteria = case.get("criteria")
        if not isinstance(criteria, list) or not criteria:
            errors.append(f"{prefix}.criteria must be a non-empty array.")
            continue

        seen_criterion_ids: set[str] = set()
        for criterion_index, criterion in enumerate(criteria):
            cprefix = f"{prefix}.criteria[{criterion_index}]"
            if not isinstance(criterion, dict):
                errors.append(f"{cprefix} must be an object.")
                continue
            criterion_id = criterion.get("id")
            if not _nonempty_string(criterion_id):
                errors.append(f"{cprefix}.id must be a non-empty string.")
            elif criterion_id in seen_criterion_ids:
                errors.append(f"{cprefix}.id duplicates '{criterion_id}' within the case.")
            else:
                seen_criterion_ids.add(criterion_id)
            if not _nonempty_string(criterion.get("description")):
                errors.append(f"{cprefix}.description must be a non-empty string.")
            criterion_type = criterion.get("type")
            if criterion_type not in CRITERION_TYPES:
                errors.append(f"{cprefix}.type must be binary, scale, or human.")
            weight = criterion.get("weight", 1)
            if not isinstance(weight, (int, float)) or isinstance(weight, bool) or weight <= 0:
                errors.append(f"{cprefix}.weight must be a number greater than 0.")
            if criterion_type == "scale":
                max_score = criterion.get("max_score")
                if not isinstance(max_score, int) or isinstance(max_score, bool) or max_score <= 1:
                    errors.append(f"{cprefix}.max_score must be an integer greater than 1.")

    return errors


def _self_test() -> int:
    valid = {
        "skill_name": "example",
        "objective": "Compare revisions.",
        "baseline": {"type": "snapshot", "label": "old"},
        "runs_per_configuration": 1,
        "cases": [
            {
                "id": "case-1",
                "prompt": "Do the task.",
                "criteria": [
                    {
                        "id": "coverage",
                        "description": "Covers requirements.",
                        "type": "binary",
                    }
                ],
            }
        ],
    }
    invalid = {"skill_name": "", "cases": []}
    if validate_plan(valid):
        print("Self-test failed: valid fixture was rejected.")
        return 1
    if not validate_plan(invalid):
        print("Self-test failed: invalid fixture was accepted.")
        return 1
    print("Self-test passed.")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("plan", nargs="?", type=Path)
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()

    if args.self_test:
        return _self_test()
    if args.plan is None:
        parser.error("plan is required unless --self-test is used")

    try:
        data = json.loads(args.plan.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"Invalid evaluation plan: {exc}")
        return 1

    errors = validate_plan(data)
    if errors:
        print("Evaluation plan is invalid:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Evaluation plan is valid.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
