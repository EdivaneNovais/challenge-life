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
             summary="Operação responsável por cadastrar um usúario no evento.",
             response_model=RegistrationSchema)
def create_registration(event_id: int, body: RegistrationSchemaCreate, db: Session = Depends(get_db)):
    return registration_service.create(event_id, body.email, db, body)
   
@router.get("/api/v1/event/{event_id}/registration/{email}",
            summary="Operação responsável por recuperar o status de um evento",
            response_model=List[RegistrationSchema])
def get_registration(id: int, email: str, db: Session = Depends(get_db)):
    return registration_service.get_registration(db, id, email)
            
@router.patch("/api/v1/event/{event_id}/registration/{email}",
              summary="Operação responsável por mudar o status de um evento",
              response_model=RegistrationSchema)
def update_registration(id: int, email: str, body: RegistrationSchemaUpdate, db: Session = Depends(get_db)):
    return registration_service.update_registration(db, id, body, email)