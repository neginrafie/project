from fastapi import Depends, HTTPException,APIRouter
from sqlalchemy.orm import Session
from crud import Student as crud
from schemas import Student as schemas
from models import Student as models
from database import SessionLocal, engine
from Dependency import get_db
models.Base.metadata.create_all(bind=engine)
router = APIRouter




student_db = []

# Route to create a new student
@app.post("/Student/", response_model=schemas.Student)
async def create_student(student: schemas.Student):
    Student_db.append(student)
    return student

# Route to get all student
@router.get("/Student/", response_model=schemas.Student)
async def read_student(student: schemas.Student):
    return student_db

# Route to get a single student by student_id
@router.get("/Student/{student_id}", response_model=schemas.Student)
async def read_student(student_id: str):
    for student in student_db:
        if student.student_id == student_id:
            return student
    raise HTTPException(status_code=404, detail="Student not found")

# Route to update a student by student_id
@router.put("/Student/{student_id}", response_model=Student)
async def update_student(student_id: str, student: Student):
    for s in student_db:
        if s.student_id == student_id:
            s = student # Update existing student
            return s
    raise HTTPException(status_code=404, detail="Student not found")

# Route to delete a student by student_id
@router.delete("/Student/{student_id}")
async def delete_student(student_id: str):
    for i, student in enumerate(student_db):
        if student.student_id == student_id:
            student_db.pop(i)
            return {"message": "Student deleted successfully"}
    raise HTTPException(status_code=404, detail="Student not found")