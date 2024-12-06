from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from ..models.user import User
from ..schemas.user import UserCreate
import random
import hashlib

async def send_verification_code(phone: str, db: AsyncSession):
    # Generate a random 6-digit code
    code = str(random.randint(100000, 999999))
    
    # In production, send via SMS service
    # For demo, just return the code
    return {"message": "Verification code sent", "code": code}

async def verify_and_login(user_data: UserCreate, db: AsyncSession):
    # In production, verify against stored code
    # For demo, accept any code
    
    stmt = select(User).where(User.phone == user_data.phone)
    result = await db.execute(stmt)
    user = result.scalar_one_or_none()
    
    if not user:
        # Create new user
        user = User(
            phone=user_data.phone,
            name=user_data.name,
            user_type=user_data.user_type,
            hashed_password=hashlib.sha256(
                user_data.verification_code.encode()
            ).hexdigest()
        )
        db.add(user)
        await db.commit()
        await db.refresh(user)
    
    return user