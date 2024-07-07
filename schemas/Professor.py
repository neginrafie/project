from pydantic import BaseModel

class Professor(BaseModel):

    LID = int
    Fname = str
    Lname = str
    department = str
    Mojor = str
    Marride = str
    Post = int
    Cphon = int
    Hphon = int
    LCourseIDs = int