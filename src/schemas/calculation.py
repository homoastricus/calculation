from pydantic import BaseModel, Field
from datetime import datetime
from decimal import Decimal
from typing import List


class MaterialSchema(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    qty: float = Field(..., gt=0)
    price_rub: float = Field(..., gt=0)


class CalculationRequest(BaseModel):
    materials: List[MaterialSchema] = Field(..., min_items=1)


class CalculationResponse(BaseModel):
    total_cost_rub: float


class CalculationResultSchema(BaseModel):
    id: int
    total_cost_rub: Decimal
    created_at: datetime

    class Config:
        from_attributes = True