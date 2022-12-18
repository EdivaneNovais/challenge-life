from typing import List
from fastapi import Depends
from fastapi.routing import APIRouter
from config.database import get_db
from fastapi import HTTPException, status
from sqlalchemy.orm.session import Session

from domain.user import user_service
from domain.user.user_schema import UserSchema, UserSchemaCreate, UserSchemaUpdate


router = APIRouter()


@router.get("/api/v1/users",
            summary="Operação Responsavel por retornar todos os usuarios cadastrados.",
            response_model=List[UserSchema])
def get_users(db: Session = Depends(get_db)):
    return user_service.get_users(db)

@router.get("/api/v1/users/{id}", 
            summary="Operação responsável por retornar um usuário.",
            response_model=List[UserSchema])
def get_user(id: int, db: Session = Depends(get_db)):
    return user_service.get_user(db, id)

@router.post("/api/v1/users",
            summary="Operação responsável por criar um novo usuário.",
            response_model=UserSchema)
def create_user(body: UserSchemaCreate, db: Session = Depends(get_db)):
    print(body)
     
    validation_email = user_service.validates_email(db, body.email)
    validation_age = user_service.validates_age(body.age)
    
    if validation_age == True:
        if validation_email == []:
            return user_service.create(db, body)
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='ESTE E-MAIL JÁ EXISTE')
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='VOCÊ PRECISA TER  IDADE MAIOR QUE 18 ANOS')

@router.put("/api/v1/users/{id}",
            summary="Operação responsável por atualizar um usuário.",
            response_model=UserSchema)
def update_user(id: int, body:UserSchemaUpdate, db: Session = Depends(get_db)):
    return user_service.update_user(db, id, body)
    
