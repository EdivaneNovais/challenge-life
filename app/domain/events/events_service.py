import json
from fastapi import HTTPException, status
from sqlalchemy.orm.session import Session
from domain.user.user_model import User
from domain.events.events_model import Event
from domain.events.events_repository import EventRepository
from domain.events.events_schema import EventSchema, EventSchemaCreate

def create(db: Session, body: EventSchemaCreate) -> EventSchema:
    user_id = int(body.user_id)
    user = EventRepository().filter_by_id(db, User, user_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Deve existir um usuário para criar um evento")
    
    event = Event(**body.dict())
    print(event)
    return EventRepository().create(db, event)

def get_events(db: Session) -> EventSchema:
    return EventRepository().all(db, Event)