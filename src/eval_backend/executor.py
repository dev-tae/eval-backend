from eval_backend.models import Case

class MockExecutor:
    def execute(self, case: Case) -> str:
        if case.id == "case-1":
            return '{"name":"Mint","species":"Cat","weight":"14 lbs"}'
        if case.id == "case-2":
            return '{"name":"John Doe","date_of_birth":"01-01-1990","job":"Software Engineer"}'
        return "{}"
