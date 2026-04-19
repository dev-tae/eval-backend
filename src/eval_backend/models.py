from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum


class Status(Enum):
    QUEUED = 1
    PENDING = 2
    COMPLETED = 3


@dataclass
class Case:
    id: str
    input: str
    expected_rule: str

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
class Run:
    id: str
    dataset_id: str
    status: Status
    results: list[Result] = field(default_factory=list)
    created_at: datetime | None = None
    finished_at: datetime | None = None


