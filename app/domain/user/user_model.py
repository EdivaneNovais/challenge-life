from config.database import Base
from sqlalchemy import Column, Integer, String, Boolean

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    active = Column(Boolean, default=True)
    age = Column(Integer)
    name = Column(String, nullable=False)
    gender = Column(String, nullable=False)
    email = Column(String, nullable=False)
    
    def __repr__(self) -> str:
        return f"{self.name}, {self.age}, {self.active}, {self.email}, {self.gender }"