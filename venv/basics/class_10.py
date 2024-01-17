'''Declare Request Example Data¶
You can declare examples of the data your app can receive.
Here are several ways to do it'''

from fastapi import FastAPI,Body
from pydantic import BaseModel,Field
from typing import Union
from typing_extensions import Annotated

app = FastAPI()

#### 1 USING EXTRA JSON SCHEMA
# class Item(BaseModel):
#     name : Union[str]
#     desc : Union[str,None] =None
#     price : float
#
#     '''Version 1'''
#     # class Config:
#     #     "json_schema_extra" : {
#     #         "examples" :[
#     #             {
#     #                 "name": "Banty",
#     #                 "desc": "Welcome to fastapi",
#     #                 "price": 12.4
#     #             }
#     #         ]
#     #
#     #     }
#     '''version 2'''
#     model_config = {
#         "json_schema_extra": {
#             "examples": [
#                 {
#                     "name": "Banty",
#                     "desc": "Welcome to fastapi",
#                     "price": 12.4
#                 }
#             ]
#         }
#     }
#
# @app.put("/item/{item_id}")
# async def put_item(item_id:int , item : Item):
#     result = {"item_id":item_id, "item":item}
#     return result




#### 2 using Field additional arguments
# class Item(BaseModel):
#     name : str = Field(examples=["Soubahgya"])
#     desc : Union[str,None] = Field(default=None, examples=["Welcome to api fast"])
#     price : float = Field(examples=[12.5])
#
# @app.put("/item/{item_id}")
# async def put_items(item_id: int, item :Item):
#     result = {"item_id":item_id,"item":item}
#     return result


#### 3 Using Examples in your Body()
class Item(BaseModel):
    name : str
    desc : Union[str,None]= None
    price : float

@app.put("/item/{item_id}")
async def put_items(item_id: int, item: Annotated[Item, Body(examples=[{"name": "banty",
                                                                        "desc": "welcome",
                                                                        "price": 12.2}
                                                                       ])]):
    result = {"item_id": item_id, "item": item}
    return result

