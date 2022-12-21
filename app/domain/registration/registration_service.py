from fastapi import HTTPException, status
from sqlalchemy.orm.session import Session
from domain.user.user_model import User
from domain.events.events_model import Event
from domain.registration.registration_model import Registration

from domain.registration.registration_repository import RegistrationRepository
from domain.registration.registration_schema import RegistrationSchema, RegistrationSchemaCreate, RegistrationSchemaUpdate

def validates_email(db: Session, email: str):
    return RegistrationRepository().filter_by_email(db, Registration, email)

def create(event_id: int, email: str, db: Session, body: RegistrationSchemaCreate) -> RegistrationSchema:
    event = RegistrationRepository().filter_by_id(db, Event, event_id)
    if not event:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Deve existir um evento para se registrar.")
    
    user = RegistrationRepository().filter_by_email(db, User, email)
    if user is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Precisa ser um usuário para se registrar.")
        
    registration = Registration(**body.dict())
    print(registration)
    
    validation_email = validates_email(db, body.email)
    if validation_email is None:
        validation_capacity = RegistrationRepository().get_capacity(db, Event, event_id)
        if validation_capacity.capacity == 0:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='EVENTO LOTADO')
        else:
            capacity = validation_capacity.capacity - 1
            RegistrationRepository().update_capacity(db, Event, event_id, capacity)
            return RegistrationRepository().create(db, registration)
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='ESTE E-MAIL JÁ EXISTE')

def get_registration(db: Session, id: int, email: str) -> RegistrationSchema:
    return RegistrationRepository().filter_by_id_and_email(db, Registration, id, email)

def update_registration(db: Session, id: int, body, email: str) -> RegistrationSchemaUpdate:
    registration = RegistrationSchemaUpdate(**body.dict())
    return RegistrationRepository(). update_filter_by_id(db, Registration, id, registration, email)

