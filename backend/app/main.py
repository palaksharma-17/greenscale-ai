from fastapi import FastAPI

from backend.app.database import engine, Base
from backend.app.routers import workloads


app = FastAPI(
    title="GreenScale AI",
    description="Carbon-Aware Dynamic Multi-Cloud Workload Orchestrator",
    version="1.0.0"
)


# Create database tables
Base.metadata.create_all(bind=engine)


# Register workload routes
app.include_router(workloads.router)


@app.get("/")
def root():
    return {
        "message": "GreenScale AI is running!",
        "status": "online"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.get("/database-test")
def database_test():
    try:
        with engine.connect():
            return {
                "database": "connected",
                "status": "success"
            }
    except Exception as e:
        return {
            "database": "connection failed",
            "error": str(e)
        }