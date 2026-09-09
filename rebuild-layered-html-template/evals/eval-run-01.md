# Eval Run 01 — Conclusion-page back-test

## Scenario

Convert one 992 × 1586 flattened editorial page into a 1000 × 1600 locally runnable layered HTML + CSS package. The page contains paper grain, map collages, stacked documents, torn paper, tape, a paper clip, contour graphics, title text, UI marks, and a footer.

## Observed production path

1. Preserved the exact selected image as the source reference.
2. Generated a clean paper texture with the exact source attached to the image-edit call.
3. Cropped complex map regions from the source.
4. Found that cyan and orange accents remained baked into those crops while CSS versions also existed.
5. Re-edited the exact source to remove only those accents, then re-cropped clean map assets.
6. Rebuilt base, texture, imagery, papers, decoration, vectors, editable title, footer, guides, and source overlay as explicit HTML/CSS layers.
7. Packaged local files with no iframe or remote resource.

## Checks

| Check | Result |
| --- | --- |
| Skill frontmatter validation | PASS |
| Valid package structural check | PASS |
| Missing-package failure | PASS |
| Missing-asset failure | PASS |
| Exact browser screenshot comparison | UNVERIFIED — browser binary download was blocked by the environment |

## Outcome

**PARTIAL.** The process and deterministic package checks are grounded in a real production run. Browser-verified visual revision remains required before raising maturity above Level 0.

## Process correction retained by the skill

An element recreated as CSS or SVG must first be removed from the raster beneath it. This prevents duplicated accents and is now an explicit workflow invariant.
