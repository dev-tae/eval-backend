## Core Objects

### Dataset
A dataset is a collection of test cases for one evaluation purpose.

Fields:
- id
- name
- description
- list of cases

### Case
A case is one test input and its expected evaluation rule.

Fields:
- id
- input
- expected rule

### Run
A run is one execution of the full dataset.

Fields:
- id
- dataset_id
- status
- created_at
- finished_at

### Result
A result is the evaluation outcome for one case in one run.

Fields:
- run_id
- case_id
- raw_output
- passed
- reason


## Mock Flow

1. Create dataset `json-profile-v1`.
2. Create a run for that dataset.
3. For each case in the dataset, the mock executor returns an output.
4. The evaluator checks whether the output passes the expected rule.
5. Store the result as pass/fail with a reason.
6. Store the run summary with total passed, failed and pass rate.