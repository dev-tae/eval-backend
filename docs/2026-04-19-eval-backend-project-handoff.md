# Eval Backend Project Handoff

## What Should Move To The New Project

Move project-specific notes that are directly about the eval-backend build:

- `2026-04-02-eval-backend-flagship-v1.md`
- `2026-04-02-eval-backend-framing-draft.md`
- `2026-04-05-eval-backend-tiny-example.md`
- `2026-04-14-public-artifact-cadence.md`
- `2026-04-14-flagship-milestone-note-stub.md`

These are the notes that belong closest to the code because they define:
- project purpose
- system shape
- tiny example
- milestone expectations
- public-artifact rhythm

## What Should Stay In This Repo

Keep broader operating-system notes here:

- weekly plans
- career-pipeline notes
- remote-role strategy
- long-term frontier-lab direction
- public-signal strategy above the project level
- transformer-study direction

This repo should remain the planning and reflection workspace.

## Recommended Merge For The New Project

Instead of moving all five notes as-is, merge them into `2-3` cleaner docs in the new repo.

### 1. `README.md`

Use this for:
- what the project is
- why it exists
- core concepts:
  - dataset
  - case
  - run
  - result
  - attempt
  - trace
- current status
- current milestone

### 2. `docs/design.md`

Merge into this:
- project framing
- flagship purpose
- tiny example
- mock flow
- first coding slice

Good sections:
- purpose
- core objects
- tiny example
- run lifecycle
- mock flow
- first coding slice
- open questions

### 3. `docs/milestones.md`

Merge into this:
- milestone-note stub
- public-artifact cadence
- short milestone entries over time

Good sections:
- what counts as a milestone
- what note to write after each milestone
- good enough to publish
- milestone log

## Minimal Move Plan

If you want the leanest version, move and merge like this:

- `README.md`
  - from `2026-04-02-eval-backend-flagship-v1.md`
- `docs/design.md`
  - from `2026-04-02-eval-backend-framing-draft.md`
  - plus `2026-04-05-eval-backend-tiny-example.md`
- `docs/milestones.md`
  - from `2026-04-14-public-artifact-cadence.md`
  - plus `2026-04-14-flagship-milestone-note-stub.md`

## Recommendation

Do not physically delete the originals from this repo yet.

Use this handoff as the guide for what to recreate in the new project first.
Once the new project repo is stable, these notes can either stay here as historical context or be reduced to short pointers.
