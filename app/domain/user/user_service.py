from fastapi import HTTPException, status
from sqlalchemy.orm.session import Session
from domain.user.user_model import User
from domain.user.user_repository import UserRepository
from domain.user.user_schema import UserSchema, UserSchemaCreate, UserSchemaUpdate

def validates_age(age: int):
    if age >= 18:
        return True
    return False

def validates_email(db: Session, email: str):
    return UserRepository().filter_by_email(db, User, email)

def create(db: Session, body: UserSchemaCreate) -> UserSchema:
    user = User(**body.dict())
    validation_age = validates_age(body.age)
    validation_email = validates_email(db, body.email)
    if validation_age == True:
        if validation_email is None:
            return UserRepository().create(db, user)
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='ESTE E-MAIL JÁ EXISTE')
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='VOCÊ PRECISA TER IDADE MAIOR QUE 18 ANOS')

def get_users(db: Session) -> UserSchema:
    return UserRepository().all(db, User)

def get_user(db: Session, id: int) -> UserSchema:
    return UserRepository().filter_by_id(db, User, id)

def update_user(db: Session, id: int, body) -> UserSchemaUpdate:
    user = UserSchemaUpdate(**body.dict())
    validation_age = validates_age(body.age)
    validation_email = validates_email(db, body.email)
    if validation_age == True:
        if validation_email is None:
            return UserRepository().update_filter_by_id(db, User, id, user)
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='ESTE E-MAIL JÁ EXISTE')
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='VOCÊ PRECISA TER IDADE MAIOR QUE 18 ANOS')
