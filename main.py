
from fastapi import FastAPI
from routers import audition, performer, judge
from database.db import engine
from models import audition as audition_models, performer as performer_models, judge as judge_models

app = FastAPI()

@app.on_event("startup")
def startup():
    audition_models.Base.metadata.create_all(bind=engine)
    performer_models.Base.metadata.create_all(bind=engine)
    judge_models.Base.metadata.create_all(bind=engine)


app.include_router(audition.router, prefix="/auditions", tags=["Auditions"])
app.include_router(performer.router, prefix="/performers", tags=["Performers"])
app.include_router(judge.router, prefix="/judges", tags=["Judges"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Talent System API"}
