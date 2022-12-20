from pydantic import BaseModel, Field

class RegistrationSchema(BaseModel):
    id: int
    email: str=Field(..., example="test@gmail.com")
    registration_status: str=Field(..., example="RESERVED") 
    
    class Config:
        orm_mode = True
        
class RegistrationSchemaCreate(BaseModel):
    email: str=Field(..., example="test@gmail.com")
    registration_status: str=Field(..., example="RESERVED")
    
class RegistrationSchemaUpdate(BaseModel):
    email: str
    registration_status: str
    
    class Config:
        orm_mode = True
    