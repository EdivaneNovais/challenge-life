from typing import List
from fastapi import Depends
from config.database import get_db
from fastapi.routing import APIRouter
from fastapi import HTTPException, status
from sqlalchemy.orm.session import Session

from domain.registration import registration_service
from domain.registration.registration_schema import RegistrationSchema, RegistrationSchemaCreate, RegistrationSchemaUpdate

router = APIRouter()

@router.post("/api/v1/event/{event_id}/registration",
             summary="Operação responsável por criar o cadastro de um evento.",
             response_model=RegistrationSchema)
def create_registration(body: RegistrationSchemaCreate, db: Session = Depends(get_db)):
    return registration_service.create(db, body)