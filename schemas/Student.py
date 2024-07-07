from pydantic import BaseModel

 
class Student(BaseModel):

    STID = int
    Fname = str
    Lname = str
    Fathername = str
    birthday = str
    IDS = str
    BornCity = str
    Addres = str
    Post = int
    Cphon = int
    Hphon = int
    department = int
    Mojor = str
    Marride = str
    ID = int
    SCourseIDs = int
    LIDs = int