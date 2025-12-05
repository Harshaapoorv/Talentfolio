from pydantic import BaseModel, EmailStr, Field # type: ignore

class UserBase(BaseModel):
    first_name: str = Field(..., min_length=2, max_length=50)
    last_name: str = Field(..., min_length=2, max_length=50)
    email: EmailStr

class UserCreate(UserBase):
    password: str = Field(..., min_length=8)

class UserUpdate(BaseModel):
    first_name: str | None = Field(None, min_length=2, max_length=50)
    last_name: str | None = Field(None, min_length=2, max_length=50)
    email: EmailStr | None = None
    password: str | None = Field(None, min_length=8)

class UserResponse(UserBase):
    id: int
    is_active: bool = True

    class Config:
        from_attributes = True