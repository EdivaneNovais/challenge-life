import json
from datetime import datetime
from fastapi import HTTPException, status
from sqlalchemy.orm.session import Session
from domain.user.user_model import User
from domain.events.events_model import Event
from domain.events.events_repository import EventRepository
from domain.events.events_schema import EventSchema, EventSchemaCreate, EventSchemaUpdate

def create(db: Session, body: EventSchemaCreate) -> EventSchema:
    user_id = int(body.user_id)
    user = EventRepository().filter_by_id(db, User, user_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Deve existir um usuário para criar um evento.")
    
    event = Event(**body.dict())
    print(event)
    return EventRepository().create(db, event)

def get_event(db: Session, id: int) -> EventSchema:
    return EventRepository().filter_by_id(db, Event, id)

def update_event(db: Session, id: int, body) -> EventSchemaUpdate:
    event = EventSchemaUpdate(**body.dict())
    return EventRepository().update_filter_by_id(db, Event, id, event)

# def validates_date(db: Session, start: datetime):
#     return EventRepository(). 
    