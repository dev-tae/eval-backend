from datetime import datetime
from uuid import uuid4

from eval_backend.executor import MockExecutor
from eval_backend.evaluator import SimpleEvaluator
from eval_backend.models import Dataset, Result, Run, Status, RunSummary


class Runner:
    def __init__(
        self,
        executor: MockExecutor | None = None,
        evaluator: SimpleEvaluator | None = None,
    ):
        self.executor = executor or MockExecutor()
        self.evaluator = evaluator or SimpleEvaluator()
    
    def run(self, dataset: Dataset) -> Run:
        run_id = f"run-{uuid4()}"
        created_at = datetime.now()
        results: list[Result] = []

        for case in dataset.cases:
            raw_output = self.executor.execute(case)
            result = self.evaluator.evaluate(run_id, case, raw_output)
            results.append(result)

        total_cases = len(results)
        total_passed = sum(1 for result in results if result.passed)
        total_failed = total_cases - total_passed
        pass_rate = total_passed / total_cases if total_cases else 0.0
        
        return Run(
            id=run_id,
            dataset_id=dataset.id,
            status=Status.COMPLETED,
            results=results,
            created_at=created_at,
            finished_at=datetime.now(),
            run_summary=RunSummary(
                total_cases=total_cases,
                total_passed=total_passed,
                total_failed=total_failed,
                pass_rate=pass_rate,
            ),
        )
