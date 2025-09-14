from datetime import datetime
from pydantic import BaseModel






class UserBase(BaseModel):
    username: str
    role: str

class UserCreate(UserBase):
    password: str

class UserResponse(UserBase):
    id: int
    class Config:
        orm_mode = True

class AttendanceBase(BaseModel):
    user_id: int
    present: bool


class AttendanceResponse(AttendanceBase):
    id: int
    timestamp: datetime
    class Config:
        orm_mode = True
        

