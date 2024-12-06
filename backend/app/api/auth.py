from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from ..database import get_db
from ..services import auth_service
from ..schemas.user import UserCreate, UserResponse

router = APIRouter()

@router.post("/verification-code")
async def send_verification_code(phone: str, db: AsyncSession = Depends(get_db)):
    return await auth_service.send_verification_code(phone, db)

@router.post("/login", response_model=UserResponse)
async def login(user_data: UserCreate, db: AsyncSession = Depends(get_db)):
    return await auth_service.verify_and_login(user_data, db)