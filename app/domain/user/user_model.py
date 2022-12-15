from config.database import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Boolean
from domain.events.events_model import Event

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    active = Column(Boolean, default=True)
    age = Column(Integer)
    name = Column(String, nullable=False)
    gender = Column(String, nullable=False)
    email = Column(String, nullable=False)
    event = relationship(Event, backref="events")

    def __repr__(self) -> str:
        return f"{self.name}, {self.age}, {self.active}, {self.email}, {self.gender }"