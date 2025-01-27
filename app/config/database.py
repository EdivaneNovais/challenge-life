import os
import sqlite3
from datetime import datetime
from sqlalchemy import Column
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.sqltypes import DateTime
from sqlalchemy.ext.declarative import declared_attr, declarative_base

SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///mydatabase.db")

connect = sqlite3.connect("mydatabase.db")
cursor_obj = connect.cursor()

# QUERY BANCO DE DADOS 
# cursor_obj.execute("DROP TABLE IF EXISTS users")
# cursor_obj.execute("DROP TABLE IF EXISTS events")
# cursor_obj.execute("DROP TABLE IF EXISTS registrations")


table_users = """CREATE TABLE users (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    ACTIVE BOOLEAN, 
    AGE INTEGER NOT NULL, 
    NAME VARCHAR NOT NULL, 
    GENDER VARCHAR NOT NULL, 
    EMAIL VARCHAR NOT NULL,
    created_at VARCHAR NOT NULL, 
    updated_at VARCHAR NOT NULL
);"""

table_events = """CREATE TABLE events (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    NAME VARCHAR NOT NULL,
    DESCRIPTION VARCHAR NOT NULL,
    START DATETIME NOT NULL,
    END DATETIME NOT NULL,
    ONLINE_EVENT BOOLEAN,
    LOCATION_ADDRESS VARCHAR NOT NULL,
    ORGANIZER_EMAIL VARCHAR NOT NULL,
    STATUS VARCHAR,
    CAPACITY INTEGER NOT NULL,
    created_at VARCHAR NOT NULL, 
    updated_at VARCHAR NOT NULL
);"""

table_registration =  """CREATE TABLE registrations (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    EMAIL VARCHAR NOT NULL,
    REGISTRATION_STATUS VARCHAR NOT NULL,
    EVENT_ID INTEGER,
    created_at VARCHAR NOT NULL, 
    updated_at VARCHAR NOT NULL,
    CONSTRAINT fk_event FOREIGN KEY (ID) REFERENCES events (ID)
);"""

    
# cursor_obj.execute(table_users)
# cursor_obj.execute(table_events)
# cursor_obj.execute(table_registration)

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