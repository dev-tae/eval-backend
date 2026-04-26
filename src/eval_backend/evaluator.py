import json
import re

from eval_backend.models import Case, Result


class SimpleEvaluator:
    def evaluate(self, run_id: str, case: Case, raw_output: str) -> Result:
        rule = case.expected_rule

        if rule.require_valid_json:
            try:
                parsed_output = json.loads(raw_output)
            except json.JSONDecodeError:
                return Result(
                    run_id=run_id,
                    case_id=case.id,
                    raw_output=raw_output,
                    passed=False,
                    reason="output is not valid JSON",
                )
        else:
            parsed_output = raw_output

        if not isinstance(parsed_output, dict):
            return Result(
                run_id=run_id,
                case_id=case.id,
                raw_output=raw_output,
                passed=False,
                reason="output JSON must be an object",
            )

        missing_fields = [
            field for field in rule.required_fields if field not in parsed_output
        ]

        if missing_fields:
            return Result(
                run_id=run_id,
                case_id=case.id,
                raw_output=raw_output,
                passed=False,
                reason=f"missing required fields: {', '.join(missing_fields)}",
            )

        for field in rule.date_fields:
            value = parsed_output.get(field)
            if not isinstance(value, str) or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", value):
                return Result(
                    run_id=run_id,
                    case_id=case.id,
                    raw_output=raw_output,
                    passed=False,
                    reason=f"{field} must match YYYY-MM-DD",
                )

        return Result(
            run_id=run_id,
            case_id=case.id,
            raw_output=raw_output,
            passed=True,
            reason="output passed all checks",
        )
