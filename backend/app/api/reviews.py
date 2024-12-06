from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from ..database import get_db
from ..services import review_service
from ..schemas.review import ReviewCreate, ReviewResponse

router = APIRouter()

@router.get("", response_model=List[ReviewResponse])
async def get_reviews(merchant_id: int, db: AsyncSession = Depends(get_db)):
    return await review_service.get_reviews(merchant_id, db)

@router.post("", response_model=ReviewResponse)
async def create_review(
    merchant_id: int,
    review_data: ReviewCreate,
    db: AsyncSession = Depends(get_db)
):
    return await review_service.create_review(merchant_id, review_data, db)