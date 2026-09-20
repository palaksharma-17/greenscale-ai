from fastapi import FastAPI

<<<<<<< HEAD
from app.api.routes import router
=======
from backend.app.database import engine, Base
from backend.app.routers import workloads
>>>>>>> e54240e4bb85afe94a0fe4fcfb18d282db7e586c


app = FastAPI(
    title="GreenScale AI",
<<<<<<< HEAD
    description="Carbon-aware dynamic multi-cloud workload orchestrator",
    version="0.1.0"
)


app.include_router(router)
=======
    description="Carbon-Aware Dynamic Multi-Cloud Workload Orchestrator",
    version="1.0.0"
)


# Create database tables
Base.metadata.create_all(bind=engine)


# Register workload routes
app.include_router(workloads.router)
>>>>>>> e54240e4bb85afe94a0fe4fcfb18d282db7e586c


@app.get("/")
def root():
    return {
<<<<<<< HEAD
        "message": "Welcome to GreenScale AI",
        "status": "running"
    }
=======
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
>>>>>>> e54240e4bb85afe94a0fe4fcfb18d282db7e586c
