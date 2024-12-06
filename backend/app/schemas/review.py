from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class ReviewBase(BaseModel):
    rating: float
    content: str
    user_id: int

class ReviewCreate(ReviewBase):
    pass

class ReviewResponse(ReviewBase):
    id: int
    merchant_id: int
    created_at: datetime
    user_name: Optional[str] = None

    class Config:
        from_attributes = True