import datetime
import pytz
from fastapi import HTTPException, status
from sqlalchemy.orm.session import Session
from domain.events.events_model import Event
from domain.events.events_repository import EventRepository
from domain.events.events_schema import EventSchema, EventSchemaCreate, EventSchemaUpdate

def validate_date(start: datetime, end: datetime):
    today = datetime.datetime.now().replace(tzinfo=pytz.UTC)
    if start > today and end > today:
        return True
    return False

def create(db: Session, body: EventSchemaCreate) -> EventSchema:
    event = Event(**body.dict())
    print(event)
    validation_date = validate_date(body.start, body.end)
    if validation_date == True: 
        return EventRepository().create(db, event)
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='A DATA DEVE SER MAIOR QUE A DATA ATUAL')

def get_event(db: Session, id: int) -> EventSchema:
    return EventRepository().filter_by_id(db, Event, id)

def update_event(db: Session, id: int, body) -> EventSchemaUpdate:
    event = EventSchemaUpdate(**body.dict())
    return EventRepository().update_filter_by_id(db, Event, id, event)

