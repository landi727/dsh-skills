# Audit report template

Keep the report concise enough to drive revision. Add detail only where evidence or a failure requires it.

## 1. Verdict

- **Verdict:** `可发布` / `可发布，有已知降级` / `暂缓发布` / `仅完成策划审查`
- **Review mode:** `plan-audit` / `source-audit` / `release-audit`
- **Review date and version:**
- **Delivery route:**
- **Required clients:**
- **One-sentence reason:**

## 2. Blocking items

List only issues that prevent the stated release verdict. For each item, give the module ID, impact, required repair, and proof needed to close it.

## 3. Feature matrix

| Module | Intended effect | Proposed implementation | Essential? | Status | Evidence | Failure mode | Fallback | Next action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

Use `主版本可用`, `条件可用`, `应降级`, or `证据不足`. Use E0–E3 evidence levels.

## 4. Minimal revisions

List the smallest changes that preserve the approved content, visual hierarchy, rhythm, and campaign concept. State production cost or tradeoff when material.

## 5. Release-test checklist

| Test | Platform/device | Expected result | Actual result | Evidence | Status |
| --- | --- | --- | --- | --- | --- |

Include editor save/reopen, iOS, Android, every interaction, media first state, long-page loading, image joins, and fallbacks relevant to the article.

## 6. Evidence ledger

| Claim | Evidence level | Source or artifact | Scope | Checked date | Limitation |
| --- | --- | --- | --- | --- | --- |

## 7. Remaining user-side verification

End with the exact previews, screenshots, recordings, permissions, or device results still needed. Do not ask for items already supplied.
