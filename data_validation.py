from fastapi import FastAPI
from pydantic import BaseModel , EmailStr , Field
from typing import Optional

app = FastAPI()

class User(BaseModel):

    username: str = Field(..., min_length=2, max_length=50)
    age: int = Field(..., gt=0, lt=60)
    email : EmailStr
    cgpa : float = Field(..., gt=0, lt=4.0)
    married : Optional[bool] = Field(default=False)
    salary: int = Field(..., gt=0)



@app.post("/user/create")
def create_user(user : User):
    return {"user" : user} 

@app.get("/")
def home():
    return "home"
