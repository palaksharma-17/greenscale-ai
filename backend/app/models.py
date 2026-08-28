from datetime import datetime

from sqlalchemy import Column, Integer, String, Float, DateTime

from backend.app.database import Base


class Workload(Base):
    __tablename__ = "workloads"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, nullable=False)

    cpu_required = Column(Float, nullable=False)

    memory_required = Column(Float, nullable=False)

    duration = Column(Float, nullable=False)

    priority = Column(
        String,
        nullable=False,
        default="medium"
    )

    status = Column(
        String,
        nullable=False,
        default="pending"
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )