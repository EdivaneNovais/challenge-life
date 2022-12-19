from datetime import datetime
from fastapi import HTTPException, status
from sqlalchemy.orm.session import Session
from domain.user.user_model import User
from domain.events.events_model import Event
from domain.registration.registration_model import Registration

from domain.registration.registration_repository import RegistrationRepository
from domain.registration.registration_schema import RegistrationSchema, RegistrationSchemaCreate, RegistrationSchemaUpdate


def create(db: Session, body: RegistrationSchemaCreate) -> RegistrationSchema:
    event_id = int(body.event_id)
    event = RegistrationRepository().filter_by_id(db, User, event_id)
    if not event:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Deve existir um evento para se registrar.")
    
    registration = Registration(**body.dict())
    print(registration)
    return RegistrationRepository().create(db, registration)

def get_registration(db: Session, id: int) -> RegistrationSchema:
    return RegistrationRepository().filter_by_id(db, Registration, id)