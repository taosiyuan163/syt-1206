from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from ..models.merchant import Merchant
import aiohttp
import math

async def get_location_info(lat: float, lng: float):
    # In production, use a geocoding service
    # For demo, return mock data
    return {
        "address": "示例地址",
        "city": "北京市",
        "district": "朝阳区"
    }

async def search_nearby(query: str, lat: float, lng: float, db: AsyncSession):
    # In production, implement proper geospatial search
    # For demo, return filtered merchants
    stmt = select(Merchant).where(Merchant.name.ilike(f"%{query}%"))
    result = await db.execute(stmt)
    merchants = result.scalars().all()
    
    # Add mock distance
    for merchant in merchants:
        merchant.distance = round(random.uniform(0.1, 5.0), 1)
    
    return merchants