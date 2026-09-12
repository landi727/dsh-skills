# Evidence and status rules

## Evidence levels

Assign one evidence level to every material compatibility claim.

| Level | Evidence | What it can support |
| --- | --- | --- |
| `E3 真实链路` | The same draft, account permissions, import route, and feature passed after save/reopen and on required iOS and Android previews | Release decision for the tested combination |
| `E2 当前一手` | Current official documentation, current WeChat editor UI, or a native error/validation message | Current capability or stated constraint; device behavior still needs testing |
| `E1 公开实证` | A published article/source or a repeatable test from a different account, route, or time | Feasibility precedent only |
| `E0 未证实` | Memory, assumption, third-party claim, inaccessible source, or no evidence | Question or test requirement only |

Prefer E3 over all lower levels. Record source, date checked, account/route scope, and relevant version. Never cite a third-party editor's preview as WeChat evidence.

When current official documentation is unavailable, state that limitation and rely on same-route editor and device tests. Do not silently promote E1 to E2.

## Feature statuses

| Status | Meaning | Required action |
| --- | --- | --- |
| `主版本可用` | Stable base content or E3-proven behavior with no critical failure | Keep; still run the final regression test after edits |
| `条件可用` | Feasible, but account, editor route, client, asset size, or version can change the result | Provide fallback and complete named tests |
| `应降级` | Current mechanism creates unnecessary failure risk or lacks proof for an essential function | Replace the mechanism while preserving the communication goal |
| `证据不足` | Artifact, permission, version, or real preview is missing | Do not claim compatibility; list the missing evidence |

Status describes the proposed implementation in its stated route. It is not a permanent property of a format such as SVG or GIF.

## Claim discipline

For every conclusion, distinguish:

- **Observed:** Present in the supplied source, saved draft, screenshot, or recording.
- **Verified:** Reproduced through the stated WeChat route and required clients.
- **Inferred:** Likely result based on lower-level evidence.
- **Recommended:** A change intended to reduce risk or cost.

Use exact wording:

- `已验证`: only for E3.
- `参考案例可实现`: for E1 published precedents.
- `需真机验证`: when the device gate is incomplete.
- `需账号权限验证`: when availability varies by account.

## Change invalidation

Re-test affected rows when any of these changes:

- WeChat editor or API route.
- Account type, verification, or permissions.
- SVG markup, CSS, image, GIF, video, audio, URL, or mini-program target.
- Asset dimensions, compression, hosting, or module order.
- WeChat or OS version for a required client.

Do not re-test unrelated rows unless the change can affect adjacent modules, page height, or shared CSS.
