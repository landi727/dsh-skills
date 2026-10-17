# Implementation decision matrix

Use this matrix to avoid treating every feature as an undefined request for testing. It supplies a default planning status for the proposed mechanism. Current first-party evidence and same-route tests override these defaults.

## Route codes

- `EDITOR`: inserted with the native WeChat editor.
- `PASTE`: copied or imported from local HTML or a third-party editor.
- `API`: created through the account's current draft/article API route.
- `ASSET`: exported upstream and uploaded as a raster or media asset.

## Default decisions

| Mechanism | Relevant route | Default planning status | Permission dependency | Evidence required to upgrade | Base or fallback |
| --- | --- | --- | --- | --- | --- |
| Static PNG/JPEG with ordinary article flow | `EDITOR` / `API` / `ASSET` | `主版本可用` | Usually none beyond upload access | Editor save/reopen plus device preview for release | Preserve complete content in the image and nearby article text where needed |
| Text baked into a static image | `ASSET` | `主版本可用` | None specific | Post-upload readability and crop test | Upstream editable source; readable raster upload |
| Continuous-image join | `ASSET` | `条件可用` until joins pass | None specific | Saved-draft and dual-device seam test | Put transition artwork inside both neighboring assets |
| GIF used for decoration | `EDITOR` / `API` / `ASSET` | `条件可用` | Route may impose current limits | Final-file upload, first-load, loop, compression, and fallback tests | Complete first/static frame |
| GIF carrying critical meaning | Any | `应降级` unless base frame contains the full meaning | Route may impose current limits | E3 plus tested base state | Static ordered frames or adjacent summary |
| Native video or audio block | `EDITOR` / `API` | `条件可用` | Account/editor capability may vary | Permission, poster, playback, return-position, and device tests | Poster plus nearby summary and visible native control |
| Static inline SVG imported with HTML | `PASTE` / `API` | `条件可用` | Route dependent | Saved/reopened markup and device rendering | Raster equivalent |
| SVG or CSS animation | `PASTE` / `API` | `条件可用` for optional decoration; `应降级` for essential meaning | Route dependent | Exact saved draft passes every required gesture and client | GIF or static frame |
| CSS tap/reveal/state switch | `PASTE` / `API` | `条件可用` for optional enhancement; `应降级` for essential reading | Route dependent | Saved markup, tap target, repeated-open, and fallback tests | Ordered visible modules |
| JavaScript, iframe, custom player, form, or canvas runtime | `PASTE` / `API` | `应降级` as an article-body mechanism | Route and policy dependent | E3 is required even for an optional experiment | Native block, visible link, static module, or mini-program route |
| Scroll-triggered browser behavior, hover, or viewport script | `PASTE` / `API` | `应降级` | Route/client dependent | E3 for the exact implementation | Ordered static modules or GIF |
| Ordinary visible link or image link | `EDITOR` / `API` | `条件可用` | Account, destination, and route may matter | Permission, exact saved destination, open, and return-path tests | Another independently verified entry; do not assume an untested QR code is a working fallback |
| Mini-program card or entry | `EDITOR` / `API` | `条件可用` | Account binding and path permissions | Permission, target path, open, and return-path tests | Visible mini-program name and user-operable verified route |
| Invisible or transparent hot area | Any | `应降级` for every critical action | Route dependent | E3 does not remove discoverability risk | Visible label, button, card, or image-link affordance |
| External remote image, font, CSS, or script dependency | `PASTE` / `API` | `应降级` until transferred into the final route | Hosting and route dependent | Saved draft proves accepted resource ownership and loading | Upload accepted local assets; use system-safe text rendering |
| Negative-margin overlap used to hide image joins | `PASTE` / `API` | `应降级` | Sanitization/client dependent | Exact saved draft passes both clients and regression | Bake overlap artwork into exported assets |

## Route-specific interpretation

- `EDITOR`: native insertion can establish current availability, but device behavior still needs E3.
- `PASTE`: inspect the transformed saved draft. Local browser and third-party previews remain upstream evidence.
- `API`: verify current account authorization, payload acceptance, resource ownership, and the resulting saved draft. API success alone does not prove device rendering.
- `ASSET`: audit the final uploaded file. Upstream HTML, PSD, Canva, or Figma editability does not affect article compatibility.

## Conflict rule

When evidence conflicts, keep the lower status until the conflict is reproduced through the final route. Official eligibility rules govern whether a feature may be used; same-route editor errors govern the tested account; E3 governs the tested draft on the recorded clients.
