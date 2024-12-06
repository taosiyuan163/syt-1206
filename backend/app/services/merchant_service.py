from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func
from sqlalchemy.orm import joinedload
from ..models.merchant import Merchant
from ..schemas.merchant import MerchantCreate
from typing import Optional

async def get_merchants(
    query: Optional[str],
    lat: Optional[float],
    lng: Optional[float],
    db: AsyncSession
):
    stmt = select(Merchant).options(
        joinedload(Merchant.products),
        joinedload(Merchant.reviews)
    )
    
    if query:
        stmt = stmt.where(Merchant.name.ilike(f"%{query}%"))
    
    # In production, implement proper distance calculation
    # For demo, return all merchants
    result = await db.execute(stmt)
    return result.scalars().all()

async def get_merchant_by_id(merchant_id: int, db: AsyncSession):
    stmt = select(Merchant).where(
        Merchant.id == merchant_id
    ).options(
        joinedload(Merchant.products),
        joinedload(Merchant.reviews)
    )
    result = await db.execute(stmt)
    return result.scalar_one_or_none()

async def create_merchant(merchant_data: MerchantCreate, db: AsyncSession):
    merchant = Merchant(**merchant_data.dict())
    db.add(merchant)
    await db.commit()
    await db.refresh(merchant)
    return merchant