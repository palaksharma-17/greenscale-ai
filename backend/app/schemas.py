from datetime import datetime

from pydantic import BaseModel, ConfigDict


class WorkloadCreate(BaseModel):
    name: str
    cpu_required: float
    memory_required: float
    duration: float
    priority: str = "medium"


class WorkloadResponse(BaseModel):
    id: int
    name: str
    cpu_required: float
    memory_required: float
    duration: float
    priority: str
    status: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)