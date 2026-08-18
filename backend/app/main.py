from fastapi import FastAPI

from app.api.routes import router


app = FastAPI(
    title="GreenScale AI",
    description="Carbon-aware dynamic multi-cloud workload orchestrator",
    version="0.1.0"
)


app.include_router(router)


@app.get("/")
def root():
    return {
        "message": "Welcome to GreenScale AI",
        "status": "running"
    }