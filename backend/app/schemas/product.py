from pydantic import BaseModel

class ProductBase(BaseModel):
    name: str
    price: float
    description: str
    image: str

class ProductCreate(ProductBase):
    pass

class ProductResponse(ProductBase):
    id: int
    merchant_id: int

    class Config:
        from_attributes = True