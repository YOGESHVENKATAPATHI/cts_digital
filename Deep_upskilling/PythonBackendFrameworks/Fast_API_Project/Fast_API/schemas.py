from pydantic import BaseModel,EmailStr
from typing import Optional

#Course_Create
class CourseCreate(BaseModel):

    name: str
    code: str
    credits: int
    department_id: int

#Course_Response
class CourseResponse(CourseCreate):

    id: int

    class Config:
        from_attributes = True
        
class CourseUpdate(BaseModel):

    name: Optional[str] = None
    code: Optional[str] = None
    credits: Optional[int] = None
    department_id: Optional[int] = None
    
#User_Create
class UserCreate(BaseModel):

    email: EmailStr
    password: str
    
#User_Response
class UserResponse(BaseModel):

    id: int
    email: EmailStr
    is_active: bool

    class Config:
        from_attributes = True

class LoginRequest(BaseModel):

    email: EmailStr
    password: str
    
class Token(BaseModel):

    access_token: str
    token_type: str