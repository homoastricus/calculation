from decimal import Decimal
from sqlalchemy.ext.asyncio import AsyncSession
from src.schemas.calculation import CalculationRequest
from src.models.calculation import CalculationResult


class CalculationService:
    @staticmethod
    async def calculate_total(request: CalculationRequest, db: AsyncSession) -> float:
        total = sum(material.qty * material.price_rub for material in request.materials)

        result = CalculationResult(total_cost_rub=Decimal(str(total)))
        db.add(result)
        await db.commit()
        await db.refresh(result)

        return float(total)

    @staticmethod
    async def get_recent_calculations(db: AsyncSession, limit: int = 10):
        from sqlalchemy import select
        from sqlalchemy.orm import selectinload

        stmt = (
            select(CalculationResult)
            .order_by(CalculationResult.created_at.desc())
            .limit(limit)
        )

        result = await db.execute(stmt)
        return result.scalars().all()