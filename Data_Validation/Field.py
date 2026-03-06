from fastapi import FastAPI
from pydantic import BaseModel , EmailStr , Field 
from typing import Optional

app = FastAPI()

class User(BaseModel):
    user_id: int = Field(...,gt=0)          # positive integer
    username: str = Field(... , min_length=3, max_length=50)   # string length
    age:int = Field(...,gt=18 , lt=60)      # above 18 and below 60
    email: EmailStr                         # email validation
    married: Optional[bool] = False         # optional boolean

@app.get("/")
def home():
    return "home"

@app.post("/user/create")
def create_user(user : User):
    return {"user" : user} 