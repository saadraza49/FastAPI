from fastapi import FastAPI, Body

app = FastAPI()           

@app.get("/")
def read():
    return {"message" : "Hello World"}

@app.post("/create")
def create_post(post: dict = Body(...)):
    print(post)
    return {"message" : "Post Created Successfully"}
