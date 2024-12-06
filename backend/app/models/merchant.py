from sqlalchemy import Column, Integer, String, Float, ForeignKey, Time
from sqlalchemy.orm import relationship
from ..database import Base

class Merchant(Base):
    __tablename__ = "merchants"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    name = Column(String(100))
    image = Column(String(255))
    address = Column(String(255))
    phone = Column(String(11))
    open_time = Column(Time)
    close_time = Column(Time)
    min_price = Column(Float)
    max_price = Column(Float)
    rating = Column(Float, default=0.0)
    
    products = relationship("Product", back_populates="merchant")
    reviews = relationship("Review", back_populates="merchant")