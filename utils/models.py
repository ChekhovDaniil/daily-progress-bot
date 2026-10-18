from dataclasses import dataclass
from enum import Enum

class TaskType(Enum):
    TASK = "task"
    HABIT = "habit"
    EVENT = "event"
    REMINDER = "reminder"

@dataclass
class Task:
    text: str
    type: TaskType = TaskType.TASK
    done: bool = False
