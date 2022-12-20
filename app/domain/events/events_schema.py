from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field

class EventSchema(BaseModel):
    id: int
    name: str=Field(..., example="My event")
    description: str=Field(..., example="meetup dev conf") 
    start: datetime=Field(..., example="2022, 5, 27, 12, 30, 0, 0") 
    end: datetime
    online_event: Optional[bool] 
    location_address: str 
    organizer_email: str 
    status: Optional[str] 
    capacity: int 
    
    class Config:
        orm_mode = True
        
class EventSchemaCreate(BaseModel):
    name: str=Field(..., example="My event")
    description: str=Field(..., example="meetup dev conf")
    start: datetime
    end: datetime
    online_event: Optional[bool] 
    location_address: str
    organizer_email: str 
    capacity: int 
    
class EventSchemaUpdate(BaseModel):
    name: str
    description: str
    start: datetime
    end: datetime
    online_event: bool
    location_address: str
    organizer_email: str
    capacity: int
    
class Confg: 
    orm_mode = True
    
    
    