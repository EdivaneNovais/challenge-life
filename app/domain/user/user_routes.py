from typing import List
from fastapi import Depends
from fastapi.routing import APIRouter
from config.database import get_db
from fastapi import HTTPException, status
from sqlalchemy.orm.session import Session

from domain.user import user_service
from domain.user.user_schema import UserSchema, UserSchemaCreate, UserSchemaUpdate

router = APIRouter()

@router.get("/users",
            summary="Operação Responsavel por retornar todos os usuarios cadastrados.",
            response_model=List[UserSchema])
def get_users(db: Session = Depends(get_db)):
    return user_service.get_users(db)

@router.get("/users/{id}", 
            summary="Operação responsável por retornar um usuário.",
            response_model=List[UserSchema])
def get_user(id: int, db: Session = Depends(get_db)):
    return user_service.get_user(db, id)

@router.post("/users",
            summary="Operação responsável por criar um novo usuário.",
            response_model=UserSchema)
def create_user(body: UserSchemaCreate, db: Session = Depends(get_db)):
    return user_service.create(db, body)
      
@router.put("/users/{id}",
            summary="Operação responsável por atualizar um usuário.",
            response_model=UserSchema)
def update_user(id: int, body:UserSchemaUpdate, db: Session = Depends(get_db)):
    return user_service.update_user(db, id, body)
    
