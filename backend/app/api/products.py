from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from ..database import get_db
from ..services import product_service
from ..schemas.product import ProductCreate, ProductResponse

router = APIRouter()

@router.get("", response_model=List[ProductResponse])
async def get_products(merchant_id: int, db: AsyncSession = Depends(get_db)):
    return await product_service.get_products(merchant_id, db)

@router.post("", response_model=ProductResponse)
async def create_product(
    merchant_id: int,
    product_data: ProductCreate,
    db: AsyncSession = Depends(get_db)
):
    return await product_service.create_product(merchant_id, product_data, db)

@router.put("/{product_id}", response_model=ProductResponse)
async def update_product(
    product_id: int,
    product_data: ProductCreate,
    db: AsyncSession = Depends(get_db)
):
    return await product_service.update_product(product_id, product_data, db)

@router.delete("/{product_id}")
async def delete_product(product_id: int, db: AsyncSession = Depends(get_db)):
    await product_service.delete_product(product_id, db)
    return {"message": "Product deleted successfully"}