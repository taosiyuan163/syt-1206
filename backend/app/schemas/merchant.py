from pydantic import BaseModel
from datetime import time
from typing import Optional, List
from .product import ProductResponse
from .review import ReviewResponse

class MerchantBase(BaseModel):
    name: str
    image: str
    address: str
    phone: str
    open_time: time
    close_time: time
    min_price: float
    max_price: float

class MerchantCreate(MerchantBase):
    pass

class MerchantResponse(MerchantBase):
    id: int
    rating: float
    products: Optional[List[ProductResponse]] = None
    reviews: Optional[List[ReviewResponse]] = None

    class Config:
        from_attributes = True