from fastapi import FastAPI
from backend.db import models, database
from routers import users, classroom

# Create DB tables
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="Smart Classroom Monitoring System")

app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(classroom.router, prefix="/classroom", tags=["Classroom"])

@app.get("/")
def root():
    return {"message": "Smart Classroom API Running"}
