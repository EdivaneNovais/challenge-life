from fastapi import Depends
from config.database import get_db
from fastapi.routing import APIRouter
from fastapi import HTTPException, status 
from sqlalchemy.orm.session import Session

from domain.registration import registration_service
from domain.registration.registration_schema import RegistrationSchema, RegistrationSchemaCreate

router = APIRouter()

@router.post("/api/v1/event/{event_id}/registration",
             summary="Operação responsável por criar o cadastro de um evento.",
             response_model=RegistrationSchema)
def create_registration(event_id: int, body: RegistrationSchemaCreate, db: Session = Depends(get_db)):
    validate_email = registration_service.validates_email(db, body.email)

    if validate_email is None:
        return registration_service.create(event_id, db, body)
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='ESTE E-MAIL JÁ EXISTE')
