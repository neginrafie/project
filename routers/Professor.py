from fastapi import Depends, HTTPException,APIRouter
from sqlalchemy.orm import Session
from crud import Professor as crud
from schemas import Professor as schemas
from models import Professor as models
from database import SessionLocal, engine
from Dependency import get_db
models.Base.metadata.create_all(bind=engine)
router = APIRouter


# داده‌های موقت برای نمایش عملیات
Professor_db = []

# Route to create a new Professor
@router.post("/Professor/", response_model=schemas.Professor)
async def create_Professor(Professor: schemas.Professor):
    Professor_db.append(Professor)
    return Professor

# Route to get all Professor
@router.get("/Professor/", response_model=schemas.Professor)
async def read_Professor(student: schemas.Professor):
    return Professor_db

# Route to get a single Professor by Professort_id
@router.get("/Professor/{Professor_id}", response_model=schemas.Professor)
async def read_Professor(sProfessor_id: str):
    for Professor in Professor_db:
        if Professor.Professor_id == Professor_id:
            return Professor
    raise HTTPException(status_code=404, detail="Professor not found")

# Route to update a Professor by Professor
@router.put("/Professor/{Professor_id}", response_model=Professor)
async def update_Professor(Professor_id: str, Professor: Professor):
    for s in Professor_db:
        if s.Professor_id == Professor_id:
            s = Professor # Update existing Professor
            return s
    raise HTTPException(status_code=404, detail="Professor not found")

# Route to delete a Professor by Professor_id
@router.delete("/Professor/{Professor_id}")
async def delete_Professor(Professor_id: str):
    for i, Professor in enumerate(Professor_db):
        if Professor.Professor_id == Professor_id:
            Professor_db.pop(i)
            return {"message": "Professor deleted successfully"}
    raise HTTPException(status_code=404, detail="Professor not found")