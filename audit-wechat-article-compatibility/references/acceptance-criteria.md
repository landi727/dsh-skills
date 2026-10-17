# Observable acceptance criteria

Use these criteria for consistent pass/fail decisions. They are audit thresholds, not claims about permanent WeChat platform limits.

## Universal release criteria

| Check | Pass | Fail |
| --- | --- | --- |
| Critical meaning | 100% of required copy, dates, prices, instructions, attribution, brand marks, and actions remain understandable in the base state | Any required meaning depends on animation, playback, reveal, or a missing module |
| Asset completeness | Zero unresolved local references and zero required remote resources whose transfer into the final route is unverified | Any required image, font, style, poster, or media file is missing or inaccessible |
| Module order | Saved/reopened draft and both required clients preserve the approved order | Any module is removed, duplicated, or reordered |
| Horizontal layout | Zero unintended horizontal scrolling or clipped critical content | Any required content is clipped or forces horizontal scrolling |
| Critical actions | 100% of critical links, cards, media controls, and gestures reach the exact intended result on both required clients | Any critical action fails, opens the wrong destination, or has no usable fallback |
| Conditional fallback | Every `条件可用` item exposes its fallback before or when the enhancement fails | A failed enhancement leaves blank space, hidden meaning, or invisible navigation |

## Images and continuous joins

- Critical text must be readable at normal article scale without pinch zoom on each required device.
- The saved draft must preserve the intended aspect ratio; any crop that removes critical content fails.
- A continuous join passes only when no gap, hairline, duplicated strip, transparent edge, or abrupt scaling step is visible at normal reading scale on either required client.
- At high zoom, record a join defect when it occupies at least one rendered screen pixel. High-zoom-only defects are `中` or `低` severity unless visible during normal reading.
- Every boundary between separately uploaded continuous assets receives its own join result; ordinary non-continuous static images may be grouped.

## GIF and animation

- The first visible frame or persistent base layer contains all critical meaning assigned to that module.
- The final uploaded file starts, completes one intended cycle, and repeats or stops exactly as specified on both clients.
- Zero blank initial frames, missing final frames, reversed frame order, or compression damage that changes meaning.
- Record final bytes, dimensions, frame count, duration, and current editor acceptance. Mark any platform size or duration claim `证据不足` unless supported by current E2 evidence.
- Frame drops are release blockers only when they remove meaning or break an action; decorative unevenness receives severity according to visual impact.

## SVG, CSS, and tap effects

- Required elements and attributes remain present after save, close, and reopen.
- Every required gesture succeeds on first and repeated use on both clients.
- Tap geometry after import matches the visible control. Any critical invisible or displaced hit area fails.
- Hover-only behavior fails the mobile interaction criterion.
- When the effect is optional, disabling it must leave the article order, spacing, meaning, and action intact.

## Native media and destinations

- Poster, caption, nearby summary, control visibility, playback/open result, return position, and fallback each receive an explicit result.
- The saved destination must exactly match the approved URL, account, mini-program, and path.
- Permission validation uses the production account and route. Evidence from another account cannot pass this check.

## Source inspection thresholds

The source audit fails its completeness check when any of these remain unresolved:

- Missing local asset references: greater than `0`.
- Required remote dependencies not demonstrably transferred into the final route: greater than `0`.
- JavaScript, iframe, form, custom-player, canvas runtime, or event handlers used for essential article behavior: greater than `0`.
- Critical interactions without a visible base action or fallback: greater than `0`.

CSS risk findings are review triggers, not automatic platform-failure claims. Assign the final status from the implementation matrix and route evidence.

## Configurable platform limits

Do not hard-code file-size, pixel-dimension, duration, frame-count, link, or account limits from memory. Record the current verified value, source, check date, and scope in the evidence ledger. Test the actual final asset against that recorded value.
