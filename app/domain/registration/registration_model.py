from config.database import Base
from sqlalchemy import Column, String, Integer

class Registration(Base):
    __tablename__ = "registrations"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, nullable=False) 
    registration_status = Column(String, nullable=False) 
    event_id = Column(Integer, nullable=False)
    
    def __repr__(self) -> str:
        return f"{self.email}, {self.registration_status}"