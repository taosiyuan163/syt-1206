from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from ..models.product import Product
from ..schemas.product import ProductCreate
from fastapi import HTTPException

async def get_products(merchant_id: int, db: AsyncSession):
    stmt = select(Product).where(Product.merchant_id == merchant_id)
    result = await db.execute(stmt)
    return result.scalars().all()

async def create_product(merchant_id: int, product_data: ProductCreate, db: AsyncSession):
    product = Product(**product_data.dict(), merchant_id=merchant_id)
    db.add(product)
    await db.commit()
    await db.refresh(product)
    return product

async def update_product(product_id: int, product_data: ProductCreate, db: AsyncSession):
    stmt = select(Product).where(Product.id == product_id)
    result = await db.execute(stmt)
    product = result.scalar_one_or_none()
    
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    
    for key, value in product_data.dict().items():
        setattr(product, key, value)
    
    await db.commit()
    await db.refresh(product)
    return product

async def delete_product(product_id: int, db: AsyncSession):
    stmt = select(Product).where(Product.id == product_id)
    result = await db.execute(stmt)
    product = result.scalar_one_or_none()
    
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    
    await db.delete(product)
    await db.commit()