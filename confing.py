from fastapi import FastAPI
from routers import Course , Profesoor, Student


app = FastAPI()
app.include_router(Course.router,tags=['Course'])