# Eval Backend Tiny Example

## Example

### Dataset
`json-profile-output-v1`

### Case 1
**Input:**  
Return this profile as JSON with fields `name`, `species`, and `weight`.

**Expected rule:**  
The output must be valid JSON and include the fields `name`, `species`, and `weight`.

### Case 2
**Input:**  
Return this profile as JSON with fields `name`, `date_of_birth`, and `job`.  
`date_of_birth` must be in `YYYY-MM-DD` format.

**Expected rule:**  
The output must be valid JSON, include the fields `name`, `date_of_birth`, and `job`, and `date_of_birth` must match `YYYY-MM-DD`.

### Possible Executor Outputs

**Case 1 output:**
```json
{"name":"Mint","species":"Cat","weight":"14 lbs"}
Case 2 output:

{"name":"John Doe","date_of_birth":"01-01-1990","job":"Software Engineer"}
Result
Case 1: pass
Reason: valid JSON, required fields present
Case 2: fail
Reason: date_of_birth format is invalid
Run Summary
total cases: 2
passed: 1
failed: 1
pass rate: 50%

## Flow

1. Create dataset `json-profile-output-v1`.
2. Create a run for that dataset.
3. Executor returns output fore ach case.
4. Evaluator checks whether the output passes the expected rule.
5. Store result as pass/fail with a reason.
6. Store run summary with total passed, failed, and pass rate.