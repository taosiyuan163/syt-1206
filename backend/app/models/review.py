from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from ..database import Base

class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True)
    merchant_id = Column(Integer, ForeignKey("merchants.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    rating = Column(Float)
    content = Column(String(500))
    created_at = Column(DateTime, server_default=func.now())
    
    merchant = relationship("Merchant", back_populates="reviews")
    user = relationship("User")