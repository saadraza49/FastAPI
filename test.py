from fastapi import FastAPI, Body
from pydantic import BaseModel
from typing import Optional

app = FastAPI()           

class Post(BaseModel):         # This is a model class
    name: str                 # These are the required fields
    fname: str
    age: int
    published: bool = True              
    rating : Optional[int] = 0

@app.get("/")                  # This is a get request
def read():
    return {"message" : "Hello World"}

@app.post("/create")           # This is a post request
def create_post(post: Post):
    print(post)
    print(post.dict())         # Converts the post object to a dictionary
    return {"data" : post}