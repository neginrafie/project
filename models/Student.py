
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from database import Base

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