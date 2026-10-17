# Report and regression contract

Contents: findings; run evidence; baseline; comparisons; final report.

## Findings and statuses

Record stable ID, title, route, category, impact(high/medium/polish), exact viewport/state/visible consequence, raw screenshot pointer, requirement/goal, concrete proposed fix and scope. Separate evidence from inference or preference. For fixes add files/hunks, own commit when applicable, before/after evidence and actual checks.

- verified: actual retest confirms the correction and applicable checks, with no new observed regression. State tested scope.
- best-effort: authorized fix applied, but required state/device/evidence is incomplete. Explain gap.
- reverted: attempt regressed or failed verification and only this review's change was undone.
- deferred: not fixed; state scope/dependency/evidence reason and next action.

An audit-only finding is pending/deferred action, not a verified fix. Unverified acceptance criteria remain visible independently of status.

## Run evidence

Record target, approved contract/version, date/run ID, revision/uncommitted state, actual pages/viewports/states, screenshots, flow observations, actual console checks, measured performance tool/conditions and independent-review status/result. Distinguish live evidence, supplied image, mockup and source inspection. Mockups/source lines cannot replace after screenshots. Different content/viewport/state/scroll/motion phase may prevent comparison.

## Baseline

Save immutable `design-baseline.<runId>.json`, preserving earlier copies. Update an optional `design-baseline.json` latest copy atomically only after the unique copy exists and within authorized scope. Preserve upstream fields; populate actual evidence, not example values:

```json
{
  "schemaVersion": 2,
  "date": "YYYY-MM-DD",
  "runId": "unique-run-id",
  "url": null,
  "designScore": "B (provisional)",
  "aiSlopScore": "B (provisional)",
  "categoryGrades": {},
  "findings": [{"id":"FINDING-001","title":"Observed issue","impact":"high","category":"hierarchy"}],
  "detector": {"mode":"none","engine":null,"base":null,"targetSet":null,"total":null,"byRule":{},"byPage":{}},
  "workEvidence": {"revision":null,"workingTree":null,"contractVersion":null,"coverage":[],"screenshots":[],"unverified":[],"independentReview":"not-run"}
}
```

workEvidence is a Work extension. The standalone installation has no detector: mode:none and null totals unless a separately available compatible detector actually ran. Manual findings are not detector totals. When one ran, record its actual version, mode(dom/source), source base where applicable, target-set hash, counts and scan limits. Confirm advisory scan findings in rendered evidence. Do not persist an authenticated DOM dump merely for this report.

## Regression

Use compatible earlier evidence, not the current/future baseline. Compare category changes and new/persistent/resolved/unverified findings. Recheck an earlier issue in matching conditions before declaring resolved. Missing/unreadable prior baseline means first usable baseline, not imagined improvement.

Detector deltas require matching mode and targetSet. Disclose changed engine/rule set. Qualify comparisons if coverage changed. Dynamic content/motion can alter pixels/counts without regression; explain the underlying observation.

## Final report

Lead with actual result and acceptance blockers. Include coverage/limits, evidence-backed findings, baseline → final grades, verified/best-effort/reverted/deferred totals, independent review status, changed files and next actions. Add genuine quick wins. Keep heuristic quality separate from satisfying approved requirements. Do not claim all checks passed, production-ready or external/cross-model-reviewed without evidence.
