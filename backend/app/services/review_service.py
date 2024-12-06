from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func
from ..models.review import Review
from ..models.merchant import Merchant
from ..schemas.review import ReviewCreate

async def get_reviews(merchant_id: int, db: AsyncSession):
    stmt = select(Review).where(Review.merchant_id == merchant_id)
    result = await db.execute(stmt)
    return result.scalars().all()

async def create_review(merchant_id: int, review_data: ReviewCreate, db: AsyncSession):
    # Create the review
    review = Review(**review_data.dict(), merchant_id=merchant_id)
    db.add(review)
    
    # Update merchant's average rating
    stmt = select(func.avg(Review.rating)).where(Review.merchant_id == merchant_id)
    result = await db.execute(stmt)
    avg_rating = result.scalar_one()
    
    # Update merchant rating
    merchant_stmt = select(Merchant).where(Merchant.id == merchant_id)
    merchant_result = await db.execute(merchant_stmt)
    merchant = merchant_result.scalar_one()
    merchant.rating = float(avg_rating)
    
    await db.commit()
    await db.refresh(review)
    return review