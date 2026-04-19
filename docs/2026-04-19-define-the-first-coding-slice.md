## First Coding Slice

### What are we building first?
We are building the core data models for `Dataset`, `Case`, `Run`, and `Result`.

Then we will build a minimal evaluator flow that runs each case through a mock executor and checks whether the output passes the expected rule.

### What input does it use?
It uses one hardcoded dataset with 2 mock cases.

### What happens step by step?
1. Define `Dataset`, `Case`, `Run`, and `Result`.
2. Create one dataset, `json-profile-v1`, with mock cases.
3. Create one run for that dataset.
4. For each case in the dataset, the mock executor returns an output.
5. The evaluator checks whether the output passes the expected rule.
6. Store the result as pass/fail with a reason.
7. Produce a run summary with total passed, failed, and pass rate.

### What output/result should exist at the end?
For each case:
- case id
- run id
- raw output
- passed/failed
- reason

For the run:
- total cases
- total passed
- total failed
- pass rate
