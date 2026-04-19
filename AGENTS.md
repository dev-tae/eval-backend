# AGENTS.md

## Purpose

This project is a focused backend flagship for long-term frontier-lab signal.

It is not a startup product and not a generic agent framework.

The goal is to create visible engineering signal in:
- backend system design
- evaluation workflow thinking
- retries and failure handling
- observability and traceability
- AI-adjacent systems literacy
- clear technical writing

This project should help demonstrate the kind of engineering judgment that is relevant to frontier labs over the long term, while still being understandable and buildable by Tae Hyun.

## Build Philosophy

- Use Python unless there is a strong reason not to.
- Keep the system narrow and explainable.
- Prefer small, incremental slices over large scaffolds.
- Mock executor first, real API executor later.
- Do not overengineer early versions.
- Favor code that can be clearly explained in an interview.
- Each meaningful milestone should produce a short written note.

## Current V1 Shape

The system should support:
- `Dataset`
- `Case`
- `Run`
- `Result`

Initial flow:
1. Create a dataset with cases.
2. Create a run for that dataset.
3. Use a mock executor to return outputs.
4. Evaluate outputs with simple rules.
5. Store or print pass/fail plus reason.
6. Produce a run summary.

## Early Evaluator Rules

Start simple:
- valid JSON
- required field presence
- simple format checks
- optional exact match or label checks

Do not start with complex model-graded evaluation.

## Guardrails

Do not:
- turn this into a broad agent platform
- add auth/multi-user/product features early
- optimize for social-media polish over technical clarity
- add complexity that Tae Hyun cannot explain

Do:
- keep architecture readable
- keep implementation testable
- document what changed and why
- treat this repo as a public-facing technical artifact over time

## Signal Goal

This repo exists partly to create credible public signal for frontier-lab-adjacent engineering ability.

That means the project should eventually show:
- a clean README
- coherent design notes
- milestone history
- real backend implementation slices
- thoughtful tradeoff decisions

The signal target is not hype.
It is visible technical clarity and real engineering progression.
