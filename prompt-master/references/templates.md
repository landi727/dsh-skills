# Prompt Templates

Use only the smallest template that fits the task. Remove empty sections and replace placeholders with known information. Do not combine templates unless the task genuinely crosses capabilities.

## Contents

1. General task
2. Grounded research
3. Structured data
4. Coding change
5. Agentic execution
6. Image generation
7. Image editing
8. Video generation
9. Controlled prompt repair

## 1. General Task

    Task
    [Exact operation]

    Context
    [Only information needed to perform the task]

    Input
    [Runtime input or placeholder]

    Requirements
    - [Constraint]
    - [Constraint]

    Output
    [Format, length, structure, and completion criteria]

## 2. Grounded Research

    Research question
    [Question and decision it supports]

    Scope
    - Geography: [scope]
    - Time range: [range]
    - Sources: [preferred or required source types]

    Method
    Find current evidence, distinguish publication date from event date, and resolve conflicting claims where possible.

    Output
    [Requested deliverable]. Cite each material claim near the supporting source. Mark unresolved uncertainty explicitly.

## 3. Structured Data

Use the target tool's native schema feature when available. Put the schema in that feature and keep the prompt focused on semantics.

    Task
    Extract [entities or decisions] from the supplied input.

    Rules
    - Do not infer missing values.
    - Represent missing values as [null or specified sentinel].
    - Follow the supplied schema exactly.

    Input
    [Runtime input]

If native schema enforcement is unavailable, add a compact field contract and one valid example only when testing shows it is needed.

## 4. Coding Change

    Goal
    [Desired behavior]

    Scope
    - Language and version: [details]
    - File or function: [path and symbol]
    - Current behavior: [observed behavior]
    - Protected interfaces: [do-not-change boundaries]

    Requirements
    - [Functional requirement]
    - [Edge case]

    Done when
    - [Observable acceptance criterion]
    - [Relevant test passes]

## 5. Agentic Execution

    Objective
    [Final deliverable]

    Starting state
    [Known project or system state]

    Scope
    - Allowed: [paths, tools, or systems]
    - Protected: [paths, data, or systems]
    - Forbidden without approval: [irreversible or external actions]

    Process
    Inspect the relevant state, make the smallest necessary change, and verify the result with [tests or evidence].

    Stop conditions
    Stop and report when [success condition] is met or when [blocker requiring user input] occurs.

    Final report
    State what changed, how it was verified, and any remaining risk.

## 6. Image Generation

    Create [image type and intended use].

    Subject
    [Identity, appearance, action]

    Scene and composition
    [Environment, viewpoint, framing, foreground/background relationships]

    Visual treatment
    [Lighting, palette, materials, texture, style]

    Required details
    [Elements that must appear]

    Exclusions
    [Only exclusions that matter]

    Output
    [Aspect ratio, crop, resolution, transparency, or safe area]

## 7. Image Editing

    Edit the attached reference image.

    Change
    - [Requested delta]

    Preserve
    - [Identity, pose, geometry, layout, lighting, or other invariants]

    Output
    [Size, crop, format, transparency]

Do not redescribe the whole image when only a local change is required.

## 8. Video Generation

    Create a [duration] video showing [subject and action].

    Shot
    [Shot size, viewpoint, lens feeling, camera movement]

    Timeline
    - Beginning: [event]
    - Middle: [event]
    - End: [event]

    Visual continuity
    [Identity, wardrobe, environment, lighting, motion constraints]

    Audio
    [Dialogue, ambience, music, or no audio]

    Output
    [Aspect ratio, frame rate if supported, loop or endpoint behavior]

## 9. Controlled Prompt Repair

Use this structure when baseline outputs or failure cases are available.

    Observed failure
    [Specific repeatable failure]

    Hypothesis
    [One suspected cause]

    Variable changed
    [One conceptual variable]

    Revised prompt
    [Full prompt with all unrelated wording preserved where possible]

    Evaluation
    Run the original and revised prompts on the same cases with the same model and settings. Keep the revision only if the target failure improves without regressing passing cases.
