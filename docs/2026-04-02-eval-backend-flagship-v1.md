# Eval Backend Flagship V1

## Purpose

This project is the long-term flagship for the current cycle.

It is not a startup product and not a generic agent platform.

It exists to create real signal in:
- backend ownership
- async workflow design
- retries and idempotency
- observability and auditability
- AI-adjacent systems literacy
- technical writing and tradeoff explanation

## Product Shape

Build a backend service for running and reviewing evaluation jobs.

Core concepts:
- `dataset`
  - a named case set or evaluation set
- `run`
  - an execution attempt against a dataset with status, timing, and metadata
- `attempt`
  - a retry or execution record for a run
- `result`
  - persisted output and summary metrics
- `trace`
  - audit or observability metadata that explains what happened

The goal is to train production-like backend thinking:
- jobs do not always succeed
- retries need guardrails
- statuses need to be explicit
- result persistence matters
- operators need visibility into what happened

## V1 Scope

V1 must include:
- run creation
- run status tracking
- dataset or case-set management
- retry-safe execution model
- trace or audit metadata per run
- result persistence
- simple analysis or summary path
- explicit failure handling

V1 does not need:
- advanced auth
- multi-user collaboration
- a polished frontend product
- agent frameworks
- large-model orchestration complexity

## Suggested Slice Order

### Slice 0: framing

Write down:
- what the service does
- who the operator is
- what a run lifecycle looks like
- what can fail
- what must be visible after failure

This should be a short design note, not a giant spec.

### Slice 1: core run lifecycle

Implement:
- create a dataset
- create a run against a dataset
- track run status across basic states
- persist minimal run metadata

Target states:
- `queued`
- `running`
- `succeeded`
- `failed`

### Slice 2: retry-safe execution

Implement:
- retry recording
- attempt history
- retry guardrails
- clear handling for terminal failure

This is where idempotency and failure semantics start to matter.

### Slice 3: traceability

Implement:
- per-run event log, trace metadata, or audit trail
- timing fields
- error payload capture
- simple operator-readable run history

### Slice 4: result persistence and summary

Implement:
- store results by case or summary aggregate
- expose a simple analysis view or summary payload
- make failure versus success visible without raw log hunting

## Guardrails

- Prefer small explainable increments over large scaffolds.
- If generated code feels alien, stop and explain it before building more.
- Keep the backend simple enough that it can be defended in an interview.
- Every meaningful slice should produce one short note:
  - what changed
  - why it matters
  - what tradeoff was chosen

## Weekly Use

Default cadence:
- `2` weekday night sessions
- `1` weekend deep block

Use low-energy nights for practical coding drills instead of forcing flagship work.
The flagship should stay active without displacing the main remote-role search.

Each meaningful weekend block should usually produce:
- one small implementation slice
- one short milestone note

## Output Expectations

By the end of the first cycle, this project should generate:
- a resume-usable project blurb
- at least one design or tradeoff note
- concrete talking points on retries, failure handling, observability, and AI-adjacent workflow design
- a visible artifact trail that can later support public proof

If it is not producing those outputs, the project is drifting.
