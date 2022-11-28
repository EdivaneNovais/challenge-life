import os
from datetime import datetime
from sqlalchemy import Column, column
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.sqltypes import DateTime
from sqlalchemy.ext.declarative import declared_attr, declarative_base

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:mypass@db:5432"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class BaseModel(object):
    @declared_attr
    def created_at(cis):
        return Column(DateTime, default=datetime.now)


    @declared_attr
    def updated_at(cis):
        return Column(DateTime, default=datetime.now, onupdate=datetime.now)

Base = declarative_base(cls=BaseModel)

def get_db():
    db = None
    try:
        db = SessionLocal()
        Base.metadata.create_all(engine)
        yield db
    finally:
        if db:
            db.close()