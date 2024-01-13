# Query Parameter
from fastapi import FastAPI
from typing import Union

app =FastAPI()

app_db = [{"first" : "1st"},{"second" :"2nd"},{"third" :"3rd"},{"fourth":"4th"}]

@app.get("/items")
async def get_db_data(skip : int = 0, limit : int =10):
    return app_db[skip : skip + limit]

#run this::  http://127.0.0.1:8000/items?skip=0&limit=2


# Optional Parameter

@app.get("/item_/{item_id}")
async def get_item(item_id : int , opt : Union[str ,None] =None):
    if opt:
        return {"item_id":item_id , "opt" : opt}
    return {"item_id":item_id}

#runt his :: http://127.0.0.1:8000/item_/5?opt=raja