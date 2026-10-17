---
name: consolidate-decisions-to-document
description: "Extract explicitly confirmed facts, decisions, constraints, and final revisions from conversations or supplied notes; preserve their existing relationships, hierarchy, scope, and status; and convert them into a faithful, minimally edited document. Use when the user asks to consolidate what was decided, confirmed conclusions, or a frozen plan. Do not use for full-discussion summaries, critique, replanning, new product judgments, or polished creative writing."
---

# Consolidate Decisions to Document

Create a faithful record of settled content. Preserve meaning and structure; do not improve the underlying plan.

## Boundaries

- Do not make new product, design, strategy, or content judgments.
- Do not add explanations, rationale, risks, solutions, background, or principles absent from the confirmed source.
- Do not treat an assistant proposal as confirmed without user acceptance.
- Do not treat silence or continued conversation as acceptance.
- Do not rebuild the taxonomy to make the document look more complete.
- Exit this skill when the request is to critique, replan, expand, creatively rewrite, or summarize the entire discussion.

## Inputs

Use the available conversation, specified messages, transcript, or notes and the user's requested topic or range. When the range is already clear, proceed without asking. When the source or range is unavailable, ask only for the missing source or one scope decision.

Check source completeness before extraction. If the available record is known to be truncated, summarized, or missing key original passages, state the actual coverage. When the missing material affects a key confirmation or version judgment, request only the necessary passage; otherwise proceed within the stated coverage.

## Confirmation Rules

Include in the main document:

- Facts, requirements, and constraints directly stated by the user and not later revised.
- Items the user explicitly accepted, adopted, retained, approved, or froze.
- The latest explicit revision for the specific item and scope it clearly addresses.

Exclude from the main document:

- Unaccepted assistant suggestions.
- Possibilities, tentative suggestions, open questions, and items marked for later discussion.
- Rejected, abandoned, or superseded material.
- Content whose status remains ambiguous or conflicting.

Place unresolved ambiguity or conflict under `待确认项`; never resolve it for the user.

Treat a later revision as replacing only the item and range it explicitly addresses. Retain other confirmed content. When the replacement range is unclear, move only the disputed portion to `待确认项`.

## Workflow

### 1. Extract confirmed content

Internally record for each candidate item: the corresponding source wording, confirmation basis, confirmed scope, later revisions, and current status (`已确认`, `待确认`, or `已废弃`). Keep only `已确认` items in the main document. Do not expose this internal ledger unless requested.

### 2. Preserve relationships and hierarchy

- Reuse existing headings, grouping dimensions, and order when they are established.
- Preserve parent-child, parallel, causal, sequential, dependency, and priority relationships.
- Preserve qualifiers such as current/later, required/optional, adopted/deferred, and applicable scope.
- When no hierarchy exists, apply only the minimum grouping needed for readability using topic names already present in the source.

### 3. Document the content

Only complete fragments, remove speech fillers, merge exact repetition, normalize already-set terminology, and correct grammar or punctuation. Do not broaden conclusions, infer missing logic, rename concepts, add transitions that imply judgments, or invent a cleaner architecture.

## Output

Return:

1. A directly readable document containing only confirmed content.
2. `待确认项` only when unresolved ambiguity or conflict exists.
3. A brief coverage note only when the available source is known to be incomplete.

Do not append other process notes, a decision ledger, change log, or duplicate summary unless requested. When the user requests a document file, lock the consolidated content first, then use the appropriate file-creation capability without rewriting it.

## Failure Handling

- If later explicit revisions conflict with earlier content, replace only the explicitly affected item and scope; keep unaffected confirmed content.
- If a conflict remains unresolved, omit it from the main document and place it under `待确认项`.
- If the source contains no confirmed content, say so; do not turn proposals into a plan.
- If the user wants all information including discussion history, leave this skill and perform an ordinary information summary.

## Validation and Stop

Before delivery, perform a two-way check:

- Verify that every main-document statement has a confirmation basis and stays within its confirmed scope.
- Verify that every confirmed item within the stated source range appears in the main document.

After merging repetitions or removing duplicates, recheck conditions, hierarchy, dependencies, qualifiers, and scope. Confirm that no rejected or superseded item remains and no new judgment was introduced. Correct detected drift, deliver once, and stop. Do not continue polishing or replanning without a new request.
