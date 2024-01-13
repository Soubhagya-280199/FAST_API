#FastAPI PATH parameters
from enum import Enum
from fastapi import FastAPI


app = FastAPI()

# Basic Example of path parameters --- func1
@app.get("/item")    #here we are passing a path as an argument so that in the node we can access the data with this path
async def get_items():
    return {"message":"Hellow to Path Parameters !!"}

#You can declare the type of path parameter in the function, using standard Python type annotations:
@app.get("/item/{item_id}")
async def get_item_id(item_id : int):
    return {"Item_id":item_id}

#Example of Static method and lets take example of func1  get_items ()
@app.get("/item/{item_id}")
async def get_item(item_id : int):
    return {"fun2 Item_id":item_id}


########## few more go thorugh on pydantics
class Modelname(str,Enum):
    fname = "raja"
    lname = "queen"
    sclname = "ssvm"
@app.get("/name/{item_name}")
async def get_item_price(item_name :Modelname):
    if item_name is Modelname.fname:
        return {"fname":Modelname.fname}
    if item_name is Modelname.lname:
        return {"lname":Modelname.lname}
    if item_name is Modelname.sclname:
        return {"school name":Modelname.sclname}