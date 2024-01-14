#Path Parameter and Numeric Validation

from fastapi import  FastAPI,Body,Path,Query
from typing import Union
from typing_extensions import Annotated

app = FastAPI()

@app.get("/items/{item_id}")
async def get_item(item_id : Annotated[int,Path(title="its a int values")],
                   q : Annotated[Union[str,None],Query(alias="item_pass")]):
    result = {"item_id":item_id}
    if q:
        result.update({"q":q})
    return result




# pass *

@app.get("/value/{item_id}")
async def read_items(*, item_id: int = Path(title="The ID of the item to get"), q: str):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results


#Number validation
@app.get("/val/{item_id}")
async def read_items(
    item_id: Annotated[int, Path(title="The ID of the item to get", ge=1)], q: str
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results