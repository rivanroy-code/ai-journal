from fastapi import FastAPI, HTTPException, status, Path
from pydantic import BaseModel
from typing import Optional
from db.base import SessionLocal

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def root():
    return {"message": "Let's build this app!"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

