# Eval Backend V1 Framing Draft

## Purpose

The purpose of Eval Backend V1 is to run evaluation cases against an executor and store the results in a structured way.

At first, the executor can be a mock function.
Later, the executor can be replaced with a real LLM API call such as OpenAI, Anthropic, or Gemini.

The main goal of the backend is not to "judge intelligence" in a broad sense.
The goal is to:
- run a dataset of evaluation cases
- capture outputs and metadata
- apply evaluation rules
- store pass/fail or score results
- make failures visible and inspectable

This project is meant to train backend thinking around:
- run orchestration
- persistence
- retries
- error handling
- observability
- AI-adjacent workflow evaluation

## Core Entities

- `Dataset`
  - a named collection of evaluation cases
- `Case`
  - one input item, expected behavior, and evaluation rule
- `Run`
  - one execution of a dataset against an executor
- `Attempt`
  - one execution attempt for a case or run, including retries
- `Result`
  - stored output, pass/fail or score, and evaluation details
- `Trace`
  - metadata that explains what happened during execution, such as timestamps, errors, and retry history

`User` is intentionally not a core v1 entity.
This version is about backend run management first, not multi-user product design.

## Run Lifecycle

1. Create or select a dataset.
2. Start a run against that dataset.
3. For each case in the dataset, call the executor.
4. Capture the raw output, timing, and execution metadata.
5. Apply evaluation logic to determine pass/fail or a simple score.
6. Store results and trace information.
7. Mark the run as succeeded or failed with a summary.

Suggested v1 run states:
- `queued`
- `running`
- `succeeded`
- `failed`

## Failure Cases

- executor call fails
- executor returns invalid output format
- evaluation logic cannot score the output
- retry succeeds after an earlier failure
- retry limit is reached
- result storage fails
- trace data is missing or incomplete

Model-behavior failures should also be visible, for example:
- the model does not follow the required format
- the model misses a required field
- the model gives the wrong label or answer shape

## V1 Scope

V1 should stay narrow.

Build:
- dataset and case definition
- run creation and status tracking
- mock executor
- simple evaluator
- result persistence
- trace or audit metadata
- run summary

For v1, the evaluator should not try to produce a vague "confidence" score.
Start with clearer evaluation outputs such as:
- `passed`
- `failed`
- `score`
- `reason`

Examples of simple v1 evaluation logic:
- exact match
- valid JSON
- required field presence
- keyword or label check

## V1 Mock Shape

The mock is not the final project.
It is a temporary executor so the backend can be built before using a real API.

Example flow:
- dataset contains cases with expected output rules
- mock executor returns deterministic fake output
- evaluator checks whether that output passes the rule
- backend stores results and summaries

Later, the executor can be swapped for a real LLM API call while keeping most of the backend structure the same.

## Current Open Questions

- should the first real evaluator be `exact match`, `JSON validity`, or `required field presence`?
- should retries be tracked per case, per run, or both?
- what is the smallest useful result summary for v1?
- when should the real LLM API executor be added after the mock version is working?
