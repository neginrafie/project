from sqlalchemy.orm import Session
import models, schemas
from sqlalchemy import update,delete

def get_Student(db: Session, Student_id: int):
    return db.query(models.Student).filter(models.Student.id == Student_id).first()

def create_student(db: Session, Student: schemas.Student):
    db_student = models.Student(STID=student.STID, Fname=student.Fname,Lname=student.Lname, Fathername=student.Fathername, 
    birthday=student.birthday,IDS=student.IDS, BornCity=student.BornCity, Addres=student.Addres, Post=student.Post, 
    Cphon=student.Cphon, Hphon=student.Hphon, department=student.department,
    Mojor=student.Mojor, Marride=student.Marride, ID=student.ID, SCourseIDs=student.SCourseIDs, LIDs=student.LIDs)
    db.add(db_student)
    db.commit(db_student)
    db.refresh(db_student)
    return db_student


def read_student(db: Session, Student: schemas.Student):
    db_student = models.Student(STID=student.STID, Fname=student.Fname,Lname=student.Lname, Fathername=student.Fathername, 
    birthday=student.birthday,IDS=student.IDS, BornCity=student.BornCity, Addres=student.Addres, Post=student.Post, 
    Cphon=student.Cphon, Hphon=student.Hphon, department=student.department,
    Mojor=student.Mojor, Marride=student.Marride, ID=student.ID, SCourseIDs=student.SCourseIDs, LIDs=student.LIDs)
    db.add(db_student)
    db.commit(db_student)
    db.refresh(db_student)
    return db_student

def update_student(db: Session, Student: schemas.Student):
    db_student = models.Student(STID=student.STID, Fname=student.Fname,Lname=student.Lname, Fathername=student.Fathername, 
    birthday=student.birthday,IDS=student.IDS, BornCity=student.BornCity, Addres=student.Addres, Post=student.Post, 
    Cphon=student.Cphon, Hphon=student.Hphon, department=student.department,
    Mojor=student.Mojor, Marride=student.Marride, ID=student.ID, SCourseIDs=student.SCourseIDs, LIDs=student.LIDs)
    db.add(db_student)
    db.commit(db_student)
    db.refresh(db_student)
    return db_student

def delete_student(db: Session, Student: schemas.Student):
    db_student = models.Student(STID=student.STID, Fname=student.Fname,Lname=student.Lname, Fathername=student.Fathername, 
    birthday=student.birthday,IDS=student.IDS, BornCity=student.BornCity, Addres=student.Addres, Post=student.Post, 
    Cphon=student.Cphon, Hphon=student.Hphon, department=student.department,
    Mojor=student.Mojor, Marride=student.Marride, ID=student.ID, SCourseIDs=student.SCourseIDs, LIDs=student.LIDs)
    db.add(db_student)
    db.commit(db_student)
    db.refresh(db_student)
    return db_student