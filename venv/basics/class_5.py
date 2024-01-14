# Body Fields

from fastapi import FastAPI,Body
from pydantic import BaseModel,Field
from typing import Union
from typing_extensions import Annotated

app = FastAPI()


class Item(BaseModel):
    name : str
    description : Union[ str, None] = Field(default=None,
    title="Description of Field in In FASTAPI", min_length=5, max_length=20)
    price : Union[float,None] = Field(gt=2,le=10)
    tax : Union[float,None] = Field(gt=1,le=5)


@app.put("/item/{item_id}")
async def update_item(item_id:int,
                      item:Annotated[Item,Body(embed=True)]):
    result = {"item_id":item_id , "item" : item}

    return {"result":result}

