from fastapi import Depends, HTTPException,APIRouter
from sqlalchemy.orm import Session
from crud import Course as crud
from schemas import Course as schemas
from models import Course as models
from database import SessionLocal, engine
from Dependency import get_db
models.Base.metadata.create_all(bind=engine)
router = APIRouter


Course_db = []
@router.post("/Course/", response_model=schemas.Course)
def create_Course(course: schemas.Course, db: Session = Depends(get_db)):
    db_course = crud.get_course(db, courseid=course.cid)
    if db_course:
        raise HTTPException(status_code=400, detail="Course already exists")
    return crud.create_course(db=db, course=course)


@router.get("/Course/", response_model=schemas.Course)
def read_course():
    return course_db

@router.get("/Course/{course_id}", response_model=schemas.CreateCourse) #path parameters
def read_course(course_id: str, db: Session = Depends(get_db)):
    db_course = crud.get_course(db, course_id=course_id)
    if db_course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    return db_course

@router.put("/Course/{course_id}", response_model=schemas.course)
async def update_course(course_id: str, db: Session = Depends(get_db)):
    for s in course_db:
        if s.course_id == course_id:
            s = course # Update existing course
            return s
    raise HTTPException(status_code=404, detail="course not found")

# Route to delete a course by course_id
@router.delete("/Course/{course_id}")
def delete_course(courset_id: int, db: Session = Depends(get_db)):
    for i, course in enumerate(course_db):
        if course.course_id == course_id:
            course_db.pop(i)
            return {"message": "course deleted successfully"}
    raise HTTPException(status_code=404, detail="course not found")