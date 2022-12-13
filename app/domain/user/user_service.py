from sqlalchemy.orm.session import Session
from domain.user.user_model import User
from domain.user.user_repository import UserRepository
from domain.user.user_schema import UserSchema, UserSchemaCreate, UserSchemaUpdate


def create(db: Session, body: UserSchemaCreate) -> UserSchema:
    user = User(**body.dict())
    return UserRepository().create(db, user)

def get_users(db: Session) -> UserSchema:
    return UserRepository().all(db, User)

def get_user(db: Session, id: int) -> UserSchema:
    return UserRepository().filter_by_id(db, User, id)

def validates_age(age: int):
    if age >= 18:
        return True
    return False

def validates_email(db: Session, email: str):
    return UserRepository().filter_by_email(db, User, email)

def update_user(db: Session, id: int, body) -> UserSchema:
    user = UserSchemaUpdate(**body.dict())
    return UserRepository().update_filter_by_id(db, User, id, user)