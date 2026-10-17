# Audit report templates

Use the template for the selected review mode. Omit empty sections. Keep observations, verification, inference, and recommendations distinct.

## Plan audit

1. **Verdict:** always `仅完成策划审查`.
2. **Scope:** review date/version, intended delivery route, account facts supplied, and required clients.
3. **Blocking design dependencies:** only mechanisms that make critical meaning or action depend on a fragile route.
4. **Compact mechanism matrix:** group modules that share mechanism, route, status, and fallback.
5. **Minimal revisions:** preserve approved content, visual hierarchy, pacing, and campaign decisions. Include severity and repair cost.
6. **Assumptions and future proof:** list only the route, account permission, editor, or device tests that could change a major verdict.

| Module group | Intended effect | Route/mechanism | Essential? | Default status | Severity | Fallback | Decision |
| --- | --- | --- | --- | --- | --- | --- | --- |

Do not add a full evidence ledger or blank device-result table.

## Source audit

1. **Verdict:** `仅完成策划审查` or `暂缓发布`; source alone cannot establish release readiness.
2. **Scope:** review date/version, intended delivery route, account facts supplied, and required clients.
3. **Source summary:** inspected path/package, HTML count, asset manifest, missing files, remote dependencies, and scanner limitations.
4. **Blocking findings:** group identical causes; retain file and module references.
5. **Mechanism risks:** use the implementation matrix and distinguish detected source facts from predicted WeChat behavior.
6. **Minimal repairs:** include severity and estimated cost.
7. **Proof still needed:** saved/reopened draft and named device checks.

| Finding/module | Observed source fact | Status | Severity | Evidence | Minimal repair | Cost | Proof needed |
| --- | --- | --- | --- | --- | --- | --- | --- |

Do not include an empty release-test result table.

## Release audit

### 1. Verdict

- **Verdict:** `可发布` / `可发布，有已知降级` / `暂缓发布`
- **Review date and article version:**
- **Delivery route and production account scope:**
- **Required clients and versions:**
- **One-sentence reason:**

### 2. Blocking items

List only items that prevent the stated verdict. Give module ID, impact, minimal repair, cost, and proof needed to close each item.

### 3. Feature matrix

| Module/group | Intended effect | Implementation | Essential? | Status | Severity | Evidence | Failure mode | Fallback | Next action/cost |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Use `主版本可用`, `条件可用`, `应降级`, or `证据不足`. Use E0-E3 and an E2 subtype when applicable.

### 4. Release-gate results

| Gate/test | Platform/device | Expected result | Actual result | Evidence | Status |
| --- | --- | --- | --- | --- | --- |

Include editor save/reopen, required iOS and Android clients, every critical action, conditional media first state, continuous joins, and fallbacks.

### 5. Minimal revisions

List the smallest changes that preserve approved content, visual hierarchy, rhythm, and campaign concept. Include severity, cost, and tradeoff when material.

### 6. Evidence ledger

| Claim | Evidence level/subtype | Source or artifact | Account/route/client scope | Checked date | Limitation |
| --- | --- | --- | --- | --- | --- |

### 7. Remaining user-side verification

End with the exact previews, screenshots, recordings, permissions, or device results still needed. Do not ask for supplied evidence.

## Published regression addendum

Add only when the published URL was actually checked:

- **Status:** `已发布复验` / `发布后发现偏差`
- **Published URL and checked date:**
- **CDN/image/media differences:**
- **Final destination and sharing checks:**
