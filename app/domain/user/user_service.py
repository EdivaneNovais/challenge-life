from sqlalchemy.orm.session import Session
from domain.user.user_model import User
from domain.user.user_repository import UserRepository
from domain.user.user_schema import UserSchema, UserSchemaCreate


def create(db: Session, body: UserSchemaCreate) -> UserSchema:
    user = User(**body.dict())
    return UserRepository().create(db, user)

def get_users(db: Session) -> UserSchema:
    return UserRepository().all(db, User)

def get_user(db: Session, id: int) -> UserSchema:
    return UserRepository().filter_by_id(db, User, id)