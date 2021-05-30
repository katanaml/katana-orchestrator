from pydantic import BaseModel
from pydantic import create_model
from enum import Enum
from typing import Optional


class TaskType(str, Enum):
    TRAINING = 'training'
    INFERENCE = 'inference'
    SERVING = 'serving'


class WorkflowTaskData(BaseModel):
    task_type: TaskType
    payload: str
    data: Optional[create_model('Data',
                                crim=(float, ...),
                                zn=(int, ...),
                                indus=(float, ...),
                                chas=(int, ...),
                                nox=(float, ...),
                                rm=(float, ...),
                                age=(float, ...),
                                dis=(float, ...),
                                rad=(int, ...),
                                tax=296,
                                b=(float, ...),
                                lstat=(float, ...))] = None
    description: Optional[str] = None


class WorkflowTask(BaseModel):
    task_id: str
    task_status: str


class WorkflowTaskResult(BaseModel):
    task_id: str
    task_status: str
    outcome: str


class WorkflowTaskCancelled(BaseModel):
    task_id: str
    task_status: str
