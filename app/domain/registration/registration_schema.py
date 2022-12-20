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
    registration_status: str=Field(..., example="CANCELED")
    
    class Config:
        orm_mode = True
    