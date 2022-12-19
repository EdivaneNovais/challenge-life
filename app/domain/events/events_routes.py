from typing import List
from fastapi import Depends
from config.database import get_db
from fastapi.routing import APIRouter
from fastapi import HTTPException, status
from sqlalchemy.orm.session import Session

from domain.events import events_service
from domain.events.events_schema import EventSchema, EventSchemaCreate, EventSchemaUpdate

router = APIRouter() 

@router.post("/api/v1/event",
             summary="Operação responsável por criar um evento.",
             response_model=EventSchema)
def create_event(body: EventSchemaCreate, db: Session = Depends(get_db)):
    return events_service.create(db, body)

@router.get("/api/v1/event/{id}",
            summary="Operação responsável por retornar um evento",
            response_model=List[EventSchema])
def get_event(id: int, db: Session = Depends(get_db)):
    return events_service.get_event(db, id)

@router.put("/api/v1/event/{id}",
            summary="Operação responsável por atualizar um evento",
            response_model=EventSchema)
def update_event(id: int, body:EventSchemaUpdate, db:Session = Depends(get_db)):
    return events_service.update_event(db, id, body)



