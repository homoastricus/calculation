from sqlalchemy import Column, Integer, Numeric, DateTime, func
from sqlalchemy.orm import declarative_base
from src.db.database import Base


class CalculationResult(Base):
    __tablename__ = "calc_results"

    id = Column(Integer, primary_key=True, index=True)
    total_cost_rub = Column(Numeric(10, 2), nullable=False)
    created_at = Column(DateTime, server_default=func.now(), index=True)