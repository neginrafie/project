from sqlalchemy import Boolean, Column, ForeignKey, Integer, String

from database import Base

class Course(Base):

    __tablename__ = "course"
    
    cid = Column(String, primary_key=True) #ایدی هر شخص که یک عدده
    cname = Column(String) 
    department = Column(String)
    credit = Column(Integer)  # تعداد واحد های درس