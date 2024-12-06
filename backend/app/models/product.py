from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from ..database import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    merchant_id = Column(Integer, ForeignKey("merchants.id"))
    name = Column(String(100))
    price = Column(Float)
    description = Column(String(500))
    image = Column(String(255))
    
    merchant = relationship("Merchant", back_populates="products")