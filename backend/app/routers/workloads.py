from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.app.database import get_db
from backend.app.models import Workload
from backend.app.schemas import WorkloadCreate, WorkloadResponse


router = APIRouter(
    prefix="/workloads",
    tags=["Workloads"]
)


@router.post(
    "/",
    response_model=WorkloadResponse
)
def create_workload(
    workload_data: WorkloadCreate,
    db: Session = Depends(get_db)
):
    workload = Workload(
        name=workload_data.name,
        cpu_required=workload_data.cpu_required,
        memory_required=workload_data.memory_required,
        duration=workload_data.duration,
        priority=workload_data.priority
    )

    db.add(workload)
    db.commit()
    db.refresh(workload)

    return workload


@router.get(
    "/",
    response_model=list[WorkloadResponse]
)
def get_workloads(
    db: Session = Depends(get_db)
):
    workloads = (
        db.query(Workload)
        .order_by(Workload.id.desc())
        .all()
    )

    return workloads