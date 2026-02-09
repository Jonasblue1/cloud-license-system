from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware

from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Cloud License Management API")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # allow all (dev mode)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/upload")
def upload(data: list[dict], db: Session = Depends(get_db)):
    for item in data:
        record = models.Software(**item)
        db.add(record)
    db.commit()
    return {"message": "Stored successfully"}

@app.get("/licenses")
def get_licenses(db: Session = Depends(get_db)):
    return db.query(models.Software).all()
