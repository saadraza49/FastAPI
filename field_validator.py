from fastapi import FastAPI
from pydantic import BaseModel , Field , field_validator
from typing import Optional

app = FastAPI()

class User(BaseModel):
    name: str
    marks: float
    @field_validator("marks")
    def check_marks(cls, value):
        if value<40:
            raise ValueError("Student must have atleast 40 marks")
        return value
    
    password: str
    @field_validator("password")
    def check_password(cls , value):
        if len(value) < 8:
            raise ValueError("Password must be atleast 8 letters")
        if not any(char.isdigit() for char in value):
            raise ValueError("Password must contain atleast 1 number")
        return value

    married: Optional[bool] = False
    
@app.post("/user")
def user_post(user : User):
    return{ "user" : user}