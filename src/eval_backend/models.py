from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum


class Status(Enum):
    QUEUED = 1
    PENDING = 2
    COMPLETED = 3


@dataclass
class ExpectedRule:
    required_fields: list[str] = field(default_factory=list)
    date_fields: list[str] = field(default_factory=list)
    require_valid_json: bool = True

@dataclass
class Case:
    id: str
    input: str
    expected_rule: ExpectedRule

@dataclass
class Dataset:
    id: str
    name: str
    description: str
    cases: list[Case] = field(default_factory=list)

@dataclass
class Result:
    run_id: str
    case_id: str
    raw_output: str
    passed: bool
    reason: str

@dataclass
class RunSummary:
    total_cases: int
    total_passed: int
    total_failed: int
    pass_rate: float

@dataclass
class Run:
    id: str
    dataset_id: str
    status: Status
    run_summary: RunSummary
    results: list[Result] = field(default_factory=list)
    created_at: datetime | None = None
    finished_at: datetime | None = None

