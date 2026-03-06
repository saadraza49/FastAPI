from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Employee(BaseModel):
    name: str
    age: int
    married : Optional[bool] = None
    salary: int

@app.get("/")
def home():
    return "home"

# Path Parameters
@app.get("/students/{roll_no}")            
def students(roll_no : int):
    if roll_no == 252591:           # Slight if condition to check the roll no
        return{
            "roll no" : roll_no,
            "name" : "saad",
            "age" : 19
        }
    else:
        return "invalid roll no"
    
# Query Parameters
@app.get("/items/")                     
def grocery_items(item : str, price: int):
    return{
        "item" : item , "price" : price
    }

# Request Body Parameters
@app.post("/employee/create/")          
def create_employee(employee : Employee):
    return employee

# Query Default Parameters 
@app.get("/items/discount")                 
def discounted_items(item : str= "Nothing", discount : int =0 ):
    return{
        "item" : item , "discount" : discount
    }


# Query and Path Parameters together
@app.get("/users/{user_id}")
def get_user(user_id: int, active: bool = True):
    return {"user_id": user_id, "active": active}