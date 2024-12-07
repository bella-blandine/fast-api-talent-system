
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.db import SessionLocal
from models.audition import Audition

router = APIRouter(prefix="/auditions", tags=["Auditions"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def get_auditions(db: Session = Depends(get_db)):
    return db.query(Audition).all()

@router.post("/")
def create_audition(title: str, description: str, judge_id: int, db: Session = Depends(get_db)):
    db_audition = Audition(title=title, description=description, judge_id=judge_id)
    db.add(db_audition)
    db.commit()
    db.refresh(db_audition)
    return db_audition
