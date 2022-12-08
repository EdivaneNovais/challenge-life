from typing import Optional
from datetime import date, datetime
from pydantic import BaseModel, Field

class UserSchema(BaseModel):
    id: int
    active: Optional[bool] 
    age: int
    name: str=Field(..., example="Maria")
    gender: str
    email: str

    class Config:
        orm_mode = True

class UserSchemaCreate(BaseModel):
    age: int
    name: str
    gender: str
    email: str

    class Config:
        orm_mode = True

  