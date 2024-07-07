from sqlalchemy.orm import Session
import models, schemas
from sqlalchemy import update,delete


def get_Course(db: Session, course_id: int):
    return db.query(models.Course).filter(models.Course.id == course_id).first()



def create_Course(db: Session, course: schemas.Course.Course):
    db_course = models.Course(cid=course.cid, cname=course.cname, department=course.department, credit=course.credit )
    db.add(db_course)
    db.commit(db_course)
    db.refresh(db_course)
    return db_course

def read_course(db: Session, course: schemas.Course):
    db_course = models.Course(cid=course.cid, cname=course.cname, department=course.department, credit=course.credit )
    db.add(db_course)
    db.commit(db_course)
    db.refresh(db_course)
    return db_course

def update_course(db: Session, course: schemas.Course):
    db_course = models.Course(cid=course.cid, cname=course.cname, department=course.department, credit=course.credit )
    db.add(db_course)
    db.commit(db_course)
    db.refresh(db_course)
    return db_course

def delete_course(db: Session, course: schemas.Course):
    db_course = models.Course(cid=course.cid, cname=course.cname, department=course.department, credit=course.credit )
    db.add(db_course)
    db.commit(db_course)
    db.refresh(db_course)
    return db_course