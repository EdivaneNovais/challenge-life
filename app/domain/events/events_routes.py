from typing import List
from fastapi import Depends
from config.database import get_db
from fastapi.routing import APIRouter
from fastapi import HTTPException, status
from sqlalchemy.orm.session import Session

from domain.events import events_service
from domain.events.events_schema import EventSchema, EventSchemaCreate

router = APIRouter()

@router.post("/api/v1/event",
             summary="Operação responsável por criar um evento.",
             response_model=EventSchema)
def create_event(body: EventSchemaCreate, db: Session = Depends(get_db)):
    return events_service.create(db, body)



