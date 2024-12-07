
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.db import SessionLocal
from models.judge import Judge

router = APIRouter(prefix="/judges", tags=["Judges"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def get_judges(db: Session = Depends(get_db)):
    return db.query(Judge).all()

@router.post("/")
def create_judge(name: str, email: str, db: Session = Depends(get_db)):
    db_judge = Judge(name=name, email=email)
    db.add(db_judge)
    db.commit()
    db.refresh(db_judge)
    return db_judge
