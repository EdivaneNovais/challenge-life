from typing import Any
from sqlalchemy.orm.session import Session

class BaseRepository():
    def create(self, db: Session, model: Any) -> Any:
        db.add(model)
        db.commit()
        db.refresh(model)
        return model

    def all(self, db: Session, cls) -> Any:
        return db.query(cls).all()

    def filter_by_id_and_email(self, db: Session, cls, id: int, email: str) -> Any:
        return db.query(cls).filter(cls.id == id and cls.email == email).all()
    
    def filter_by_id(self, db: Session, cls, id: int) -> Any:
        return db.query(cls).filter(cls.id == id).all()
    
    def filter_by_email(self, db: Session, cls, email: str) -> Any:
        return db.query(cls).filter(cls.email == email).first()
    
    def update_filter_by_id(self, db: Session, cls, id: int, body, email: str) -> Any: 
        user_obj = db.query(cls).filter(cls.id == id and cls.email == email)
        user_obj.update(dict(body))
        db.commit()
        
   