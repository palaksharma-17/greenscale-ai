from fastapi import APIRouter

router = APIRouter(
    prefix="/api",
    tags=["System"]
)


@router.get("/health")
def health_check():
    return {
        "status": "healthy"
    }


@router.get("/status")
def system_status():
    return {
        "system": "GreenScale AI",
        "backend": "FastAPI",
        "cloud_simulator": "not connected",
        "workload_simulator": "not connected",
        "optimizer": "not connected"
    }