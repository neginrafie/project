from sqlalchemy.orm import Session
import models, schemas
from sqlalchemy import update,delete

def get_Professor(db: Session, Professor_id: int):
    return db.query(models.Professor).filter(models.Professor.id == Professor_id).first()

def create_Professor(db: Session, Professor: schemas.Professor):
    db_student = models.Student(LID=student.LID, Fname=student.Fname,Lname=student.Lname, Post=student.Post, 
    Cphon=Professor.Cphon, Hphon=student.Hphon, department=student.department,
    Mojor=Professor.Mojor, Marride=student.Marride, LCourseIDs=student.LCourseIDs)
    db.add(db_Professor)
    db.commit(db_Professor)
    db.refresh(db_Professor)
    return db_Professor


def update_Professor(db: Session, Professor: schemas.Professor):
    db_student = models.Student(LID=student.LID, Fname=student.Fname,Lname=student.Lname, Post=student.Post, 
    Cphon=Professor.Cphon, Hphon=student.Hphon, department=student.department,
    Mojor=Professor.Mojor, Marride=student.Marride, LCourseIDs=student.LCourseIDs)
    db.add(db_Professor)
    db.commit(db_Professor)
    db.refresh(db_Professor)
    return db_Professor


def delete_Professor(db: Session, Professor: schemas.Professor):
    db_student = models.Student(LID=student.LID, Fname=student.Fname,Lname=student.Lname, Post=student.Post, 
    Cphon=Professor.Cphon, Hphon=student.Hphon, department=student.department,
    Mojor=Professor.Mojor, Marride=student.Marride, LCourseIDs=student.LCourseIDs)
    db.add(db_Professor)
    db.commit(db_Professor)
    db.refresh(db_Professor)
    return db_Professor