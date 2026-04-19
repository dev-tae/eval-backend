# Public Artifact Cadence

## Purpose

This note defines how the eval-backend flagship should create public proof without turning social posting into a separate obligation.

The default public-signal stack is:
- visible project structure
- concise README
- short milestone notes
- short design or tradeoff notes

## What Counts As A Milestone

A milestone is any small project step that makes the system more concrete or more explainable.

Good milestone examples:
- define dataset/case/run/result shape clearly
- add mock executor flow
- add first evaluator rule
- add result persistence
- add run summary
- add basic run states
- add retry or traceability support

A milestone does not need to be large.
It needs to be real, understandable, and worth pointing at.

## What Note To Write After Each Milestone

Each meaningful weekend block should end with one short note.

Default structure:
- what changed
- what concept clicked
- what is still confusing
- what the next slice is

Keep these notes short.
The point is visible, compounding artifacts, not polished essays.

## Good Enough To Publish

Use this threshold:
- the slice is real
- the writeup is clear
- the note teaches something specific

It does not need:
- perfect architecture
- broad external usefulness
- a finished product
- social-media polish

## Repo Visibility Guidance

Near-term output should look like:
- one visible flagship repo or subdirectory
- a clean README that explains the project in plain English
- milestone notes that show progression over time

This is enough for now.
Do not turn X into a required weekly lane.
