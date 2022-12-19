from sqlalchemy.orm import relationship
from config.database import Base
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy import Column, String, Integer

class Registration(Base):
    __tablename__ = "registrations"
    
    id = Column(Integer, primary_key=True, index=True)
    user_email = Column(String, nullable=False) 
    registration_status = Column(String, nullable=False) 
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", backref="users", uselist=False)
    event_id = Column(Integer, ForeignKey("events.id"))
    event = relationship("Event", backref="events", uselist=False)
    
    def __repr__(self) -> str:
        return f"{self.user_email}, {self.registration_status}"