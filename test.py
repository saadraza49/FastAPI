from fastapi import FastAPI, Body
from pydantic import BaseModel

app = FastAPI()           

class Post(BaseModel):
    title: str
    content: str


@app.get("/")
def read():
    return {"message" : "Hello World"}

@app.post("/create")
def create_post(post: Post):
    print(post.content)
    return {"data" : "Post Created Successfully"}
