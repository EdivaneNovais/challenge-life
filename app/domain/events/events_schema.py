from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field
from domain.user.user_schema import UserSchema

class EventSchema(BaseModel):
    id: int
    name: str=Field(..., example="My event")
    description: str=Field(..., example="meetup dev conf") 
    start: datetime=Field(..., example="2022, 5, 27, 12, 30, 0, 0") 
    end: datetime
    online_event: Optional[bool] 
    location_addres: str 
    organizer_email: str 
    status: Optional[str] 
    capacity: int 
    user: Optional[UserSchema] 
    
    class Config:
        orm_mode = True
        
class EventSchemaCreate(BaseModel):
    name: str=Field(..., example="My event")
    description: str=Field(..., example="meetup dev conf")
    start: datetime
    end: datetime
    online_event: Optional[bool] 
    location_addres: str
    organizer_email: str 
    capacity: int 
    user_id: int=Field(..., example=2)
    
class Confg: 
    orm_mode = True
    
    
    