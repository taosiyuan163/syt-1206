from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from ..database import get_db
from ..services import location_service

router = APIRouter()

@router.get("/current")
async def get_current_location(lat: float, lng: float):
    return await location_service.get_location_info(lat, lng)

@router.get("/search")
async def search_nearby(
    query: str,
    lat: float,
    lng: float,
    db: AsyncSession = Depends(get_db)
):
    return await location_service.search_nearby(query, lat, lng, db)