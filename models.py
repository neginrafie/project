
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String

from database import Base
  



#جدول دانشجو

class Student(Base): # check studentnamb

    __tablename__ = "Student"

    STID = Column(Integer,primary_key=True)
    Fname = Column(String)
    Lname = Column(String)
    Fathername = Column(String)
    birthday = Column(String)
    IDS = Column(String)
    BornCity = Column(String)
    Addres = Column(String)
    Post = Column(Integer)
    Cphon = Column(Integer)
    Hphon = Column(Integer)
    department = Column(Integer)
    Mojor = Column(String)
    Marride = Column(String)
    ID = Column(Integer)
    SCourseIDs = Column(Integer)
    LIDs = Column(Integer,ForeignKey("Professor.LID"))

Courses=relationship("Course",secondary=association_course_Student,back_populates
="Students")


#جدول استاد 
class Professor(Base):
    
    __tablename__ = "Professor"

    LID = Column(Integer,primary_key=True)
    Fname = Column(String)
    Lname = Column(String)
    department = Column(String)
    Mojor = Column(String)
    Marride = Column(String)
    Post = Column(Integer)
    Cphon = Column(Integer)
    Hphon = Column(Integer)
    LCourseIDs = Column(Integer)

Courses=relationship("Course",secondary=association_Course_Professor,back_populates
="Professor")

#جدول درس

class Course(Base):

    __tablename__ = "course"
    
    cid = Column(String, primary_key=True) #ایدی هر شخص که یک عدده
    cname = Column(String) 
    department = Column(String)
    credit = Column(Integer)  # تعداد واحد های درس

    Students=relationship("Student",secondary=association_Course_Student,back_populates="Courses")
    Professor=relationship("Professor",secondary= association_Course_Professor,back_populates ="Courses")


association_Course_Professor=Table("ssociation_course_",Base.metadata,
    Column("CID",ForeignKey("Course.CID",ondelete="cascade",onupdate="cascade")),
Column("LID",ForeignKey("Profesoor.LID",ondelete="cascade",onupdate="cascade")))

association_course_Student=Table("association_course_Student",Base.metadata,
    Column("CID",ForeignKey("Course.CID",ondelete="cascade",onupdate="cascade")),
Column("STID",ForeignKey("Student.STID",ondelete="cascade",onupdate="cascade")))