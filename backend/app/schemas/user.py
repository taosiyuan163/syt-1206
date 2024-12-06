from pydantic import BaseModel, constr

class UserBase(BaseModel):
    phone: constr(regex=r'^\d{11}$')
    name: str
    user_type: str

class UserCreate(UserBase):
    verification_code: str

class UserResponse(UserBase):
    id: int

    class Config:
        from_attributes = True