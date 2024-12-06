from sqlalchemy import Column, Integer, String, Enum
from ..database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    phone = Column(String(11), unique=True, index=True)
    name = Column(String(50))
    user_type = Column(Enum('consumer', 'merchant', name='user_types'))
    hashed_password = Column(String(100))  # For storing verification codes