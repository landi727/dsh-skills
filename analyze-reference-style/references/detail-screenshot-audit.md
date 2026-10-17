# Detail Screenshot Audit

Use this protocol after the provisional analysis and before writing the final report.

## Audit objective

Verify every externally testable visual detail against a fresh view of the source. The audit is a correction pass, not a performance ritual: a generated crop is not evidence until it has been visually inspected, and an inspection is not complete until the draft has been updated.

## 1. Build an atomic claim ledger

Split compound sentences into claims that can be independently confirmed or rejected. Assign each claim an ID and record:

- the draft claim;
- claim class;
- source image;
- region needed to test it;
- audit status: `pending`, `verified`, `corrected`, or `unresolved`;
- corrected wording or uncertainty note when applicable.

Cover every visible claim in these classes:

| Claim class | Required checks |
|---|---|
| Count and identity | Number of repeated objects; whether the named object is actually identifiable |
| Position and boundary | Left/right/top/bottom relationship; frame contact; cropping |
| Shape and orientation | Silhouette, angle, direction, proportion, deformation |
| Color and value | Dominant/supporting/accent color; warm/cool relation; darkest/lightest masses |
| Line | Weight, color, continuity, pressure, internal versus outer contour |
| Overlap and layer | Which form covers which; where the order changes; whether a key feature remains visible |
| Space and perspective | Local projection, foreshortening, scale change, depth cue, spatial contradiction |
| Light | Highlight, shadow, reflection, cast shadow, and whether lighting is coherent |
| Texture and material | Grain, dots, marks, gloss, translucency, surface differentiation |
| Repetition and rhythm | Repeated motif, sequence, spacing, directional alternation, visual path |

Interpretations such as “ceremonial” or “tense” do not need literal crops, but every visible fact used to support them does.

## 2. Capture fresh evidence crops

Create one crop for each local claim. One crop may support several claims only when each claim is still separately inspected and logged.

- Crop from the highest-fidelity source.
- Include the subject and enough neighboring context to verify position, overlap, direction, or scale.
- Keep padding around the evidence; do not crop exactly to the contour.
- For a tiny feature, make both a contextual crop and a closer crop.
- Do not add arrows, labels, sharpening, recoloring, or overlays to the evidence image.
- Use the full image for global palette, hierarchy, balance, and composition claims.
- For repeated-object counts, inspect the full image and overlapping regional crops. Count in two directions to reduce omissions.

For a local raster source, prepare a JSON region file and run:

```bash
python3 scripts/make_audit_crops.py \
  --input /absolute/path/to/source.png \
  --regions /absolute/path/to/regions.json \
  --out-dir /absolute/path/to/audit-crops
```

Region file:

```json
{
  "regions": [
    {
      "id": "C01-top-object",
      "label": "Top object, its halo, and neighboring device",
      "box": [0.25, 0.00, 0.78, 0.31]
    }
  ]
}
```

Coordinates are normalized `[left, top, right, bottom]` values from `0` to `1`.

## 3. Inspect and resolve every claim

Open every crop at original detail and assign one status:

- `verified` — the claim matches the visible evidence without material qualification;
- `corrected` — revise the report to match the evidence;
- `unresolved` — the source is too small, compressed, obscured, or ambiguous; qualify the wording or omit the claim.

Do not turn plausible object identity, medium, intent, date, or influence into fact. If a name depends on inference, say “appears to be,” “resembles,” or describe the visible shape instead.

## 4. Run a full-frame reconciliation

After all crops have been checked:

1. Reopen the full image.
2. Scan top-to-bottom, then bottom-to-top.
3. Recount repeated objects in both passes.
4. Recheck the primary and secondary visual anchors.
5. Confirm that local crop findings remain true in full compositional context.
6. Check that no corrected detail leaves a contradiction elsewhere in the report.
7. Verify that facts, interpretations, and unresolved inferences remain distinguishable.

Only then write the final answer.

## Failure handling

- If crops cannot be created, use the best available zoom or screenshot tool and state the limitation internally.
- If the original is unavailable, audit the highest-resolution visible copy and reduce certainty accordingly.
- If a detail remains unresolved after a contextual and close crop, do not guess.
- If the user asks for the audit trail, show a compact claim/status table and only the crops needed to explain corrections or ambiguities.
