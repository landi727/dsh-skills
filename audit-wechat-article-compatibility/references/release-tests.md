# Release tests

## Required evidence package

Collect or ask the user to record:

- Review date and article version.
- Account type, verification state, and relevant permissions.
- Final editor/import/API route.
- Saved-draft preview link or equivalent screenshots/recording.
- Device model, OS version, and WeChat version for each required client.
- Final asset manifest with module IDs, formats, dimensions, and filenames.
- Interaction targets and expected fallbacks.

The user may execute this checklist manually. Do not request account credentials or publish on their behalf.

## Gate 1: content

- Disable or ignore optional motion and interaction.
- Confirm that title, narrative order, dates, prices, instructions, attribution, logo, and call to action remain understandable.
- Confirm that every essential module has a visible first/base state.
- Mark any missing meaning as a release blocker.

## Gate 2: editor survival

1. Insert the assets through the intended final route.
2. Save the draft, close it, and reopen it.
3. Compare the reopened result with the intended module order and behavior.
4. Check resource URLs, formatting, spacing, SVG state, links, media cards, and tap areas.
5. Record editor warnings, rejected assets, rewritten URLs, removed markup, and visual shifts.

A successful local or third-party preview cannot replace this gate.

## Gate 3: iOS and Android

On at least one required iOS device and one required Android device:

- Open from the real preview message or link produced by the final route.
- Scroll from beginning to end at normal speed and then quickly.
- Test every visible link, card, media control, SVG tap, and other gesture.
- Check first load, delayed loading, animation start/loop, return position, and repeated opening.
- Check image clarity, text size, crop, margins, seams, blank blocks, and horizontal overflow.
- Record deviations with module ID, device/version, screenshot or recording, severity, and fallback result.

Add a lower-performance or older target device when animated assets or long pages are important to the intended audience.

## Gate 4: fallback

For each `条件可用` row:

- Force or simulate the enhancement being unavailable where practical.
- Confirm that the initial/static frame contains the promised fallback.
- Confirm that navigation remains visible and understandable.
- Confirm that adjacent modules do not break when the enhancement is absent.

## Regression scope

After a change, re-test the changed module, shared styles/assets, and adjacent joins. Re-run the full article when module order, global width, shared CSS, or delivery route changes.

## Completion criteria

The release audit is complete only when:

- Every module has a recorded result.
- All critical rows are `主版本可用` with E3 evidence.
- Conditional optional rows have tested fallbacks.
- There are no unresolved critical failures on required clients.
- The report records known limitations and the exact tested versions.
