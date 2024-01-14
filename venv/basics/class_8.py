# Multiple Parameters

#First, of course, you can mix Path, Query and request body parameter declarations freely and FastAPI will know what to do.

from fastapi import FastAPI,Query,Body,Path
from pydantic import BaseModel
from typing import Union
from typing_extensions import Annotated

app = FastAPI()

class Item(BaseModel):
    name : Union[str,None] = None
    price : Union[float,None] = None


@app.put("/item/{item_id}")
async def get_items(item_id : Annotated[int, Path(title="Get the item_id",ge=3,le=10)],
                    item: Union[Item,None]=None,
                    q: Union[str,None]=None):
    result = {"item_id":item_id,"item":item}
    if q:
        result.update({"q":q})

    return result

