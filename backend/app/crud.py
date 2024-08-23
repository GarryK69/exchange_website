from sqlalchemy.orm import Session
from .models import User

def create_user(db: Session, name: str, email: str) -> User:
    db_user = User(name=name, email=email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_by_id(db: Session, user_id: int) -> User:
    return db.query(User).filter(User.id == user_id).first()
