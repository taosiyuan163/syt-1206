from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List, Optional
from ..database import get_db
from ..services import merchant_service
from ..schemas.merchant import MerchantCreate, MerchantResponse

router = APIRouter()

@router.get("", response_model=List[MerchantResponse])
async def get_merchants(
    query: Optional[str] = None,
    lat: Optional[float] = Query(None),
    lng: Optional[float] = Query(None),
    db: AsyncSession = Depends(get_db)
):
    return await merchant_service.get_merchants(query, lat, lng, db)

@router.get("/{merchant_id}", response_model=MerchantResponse)
async def get_merchant(merchant_id: int, db: AsyncSession = Depends(get_db)):
    return await merchant_service.get_merchant_by_id(merchant_id, db)

@router.post("", response_model=MerchantResponse)
async def create_merchant(
    merchant_data: MerchantCreate,
    db: AsyncSession = Depends(get_db)
):
    return await merchant_service.create_merchant(merchant_data, db)