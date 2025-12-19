from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from src.schemas.calculation import (
    CalculationRequest,
    CalculationResponse,
    CalculationResultSchema
)
from src.services.calculation import CalculationService
from src.core.dependencies import get_db

router = APIRouter(prefix="", tags=["calculations"])


@router.post("/calc", response_model=CalculationResponse)
async def calculate(
    request: CalculationRequest,
    db: AsyncSession = Depends(get_db)
) -> CalculationResponse:
    """Calculate total cost of materials"""
    try:
        total = await CalculationService.calculate_total(request, db)
        return CalculationResponse(total_cost_rub=total)
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Calculation error: {str(e)}"
        )


@router.get("/recent", response_model=list[CalculationResultSchema])
async def get_recent_calculations(
    limit: int = 10,
    db: AsyncSession = Depends(get_db)
):
    """Get recent calculations"""
    results = await CalculationService.get_recent_calculations(db, limit)
    return results