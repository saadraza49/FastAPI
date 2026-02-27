from fastapi import FastAPI
from pydantic import BaseModel , EmailStr , Field 
from typing import Optional

app = FastAPI()

class User(BaseModel):
    user_id: int = Field(...,gt=0)
    username: str = Field(... , min_length=3, max_length=50)
    age:int = Field(...,gt=18 , lt=60)
    email: EmailStr
    married: Optional[bool] = False

@app.get("/")
def home():
    return "home"

@app.post("/user/create/{user_id}")
def create_user(user : User):
    return {"user1" : user} 