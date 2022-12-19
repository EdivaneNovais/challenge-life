from typing import Optional
from pydantic import BaseModel, Field
from domain.user.user_schema import UserSchema
from domain.events.events_schema import EventSchema

class RegistrationSchema(BaseModel):
    id: int
    user_email: str=Field(..., example="test@gmail.com")
    registration_status: str=Field(..., example="RESERVED")
    user: Optional[UserSchema]  
    event: Optional[EventSchema] 
    
    class Config:
        orm_mode = True
        
class RegistrationSchemaCreate(BaseModel):
    user_email: str=Field(..., example="test@gmail.com")
    registration_status: str=Field(..., example="RESERVED")
    user_id: int=Field(..., example=1)
    event_id: int=Field(..., example=1)
    
class RegistrationSchemaUpdate(BaseModel):
    user_email: str
    registration_status: str
    user_id: int=Field(..., example=1)
    event_id: int=Field(..., example=1)
    
    class Config:
        orm_mode = True
    