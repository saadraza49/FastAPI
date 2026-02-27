from fastapi import FastAPI
from pydantic import BaseModel , EmailStr , Field
from typing import Optional

app = FastAPI()

class User(BaseModel):

    username: str = Field(..., min_length=2, max_length=50)
    age: int = Field(..., gt=0, lt=60)
    email : EmailStr
    cgpa : float = Field(..., gt=0.00, lt=4.00)
    married : Optional[bool] = Field(default=False)
    salary: int = Field(..., gt=0)


@app.get("/")
def home():
    return "home"

@app.post("/user/create")
def create_user(user : User):
    return {"user" : user} 

