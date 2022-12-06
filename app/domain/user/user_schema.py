import imp
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
<<<<<<< HEAD
    #active: bool
=======
>>>>>>> 14a6389a6fac9a1e790607f477e4d5a598d87c2e
    age: int
    name: str=Field
    gender: str
    email: str

    class Config:
        orm_mode = True

  