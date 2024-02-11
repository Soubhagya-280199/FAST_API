#Cookies as Headers 

from fastapi import FastAPI,Cookie,Header
from typing import Union
from asyncio import *

app = FastAPI()

@app.get("/items")
async def read_items(
    cookie_id : Union [str,None] = Cookie(None),
    accept_encoding : Union [str,None] = Header(None),
    Accept_Language : Union [str,None] = Header(None),
    Sec_Ch_Ua : Union [str,None] = Header(None)
    ):
    return {"Cookie_id" : cookie_id,
            "accept_encoding" : accept_encoding,
            "Accept_Language" : Accept_Language,
            "Sec_Ch_Ua" : Sec_Ch_Ua}