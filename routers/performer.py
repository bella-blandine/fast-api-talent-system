
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.db import SessionLocal
from models.performer import Performer

router = APIRouter(prefix="/performers", tags=["Performers"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def get_performers(db: Session = Depends(get_db)):
    return db.query(Performer).all()

@router.post("/")
def create_performer(name: str, email: str, db: Session = Depends(get_db)):
    db_performer = Performer(name=name, email=email)
    db.add(db_performer)
    db.commit()
    db.refresh(db_performer)
    return db_performer
