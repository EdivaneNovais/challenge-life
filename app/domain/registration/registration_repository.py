from typing import Any

from sqlalchemy.orm.session import Session

from commons.base_repository import BaseRepository


class RegistrationRepository(BaseRepository):
    
    def filter_by_id_and_email(self, db: Session, cls, id: int, email: str) -> Any:
        return db.query(cls).filter(cls.id == id and cls.email == email).all()
    
    def get_capacity(self, db: Session, cls, id_event: int):
        return db.query(cls).filter(cls.id == id_event).first()
    
    def update_capacity(self, db: Session, cls, id_event: int, capacity: int):
        db.query(cls).filter(cls.id == id_event).update({
            cls.capacity: capacity
        })
        db.commit