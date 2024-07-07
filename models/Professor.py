from sqlalchemy import Boolean, Column, ForeignKey, Integer, String

from database import Base

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