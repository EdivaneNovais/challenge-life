import string
from config.database import Base
from sqlalchemy.types import Date
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, column
# from domain.events.events_model import Events 

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    active: Column(bool)
    age: Column(int)
    name: Column(String, nullable=False)
    gender: Column(String, nullable=False)
    email: Column(String, nullable=False)

    def __repr__(self) -> str:
        return f"{self.name}, {self.age}, {self.active}, {self.email}, {self.gender }"