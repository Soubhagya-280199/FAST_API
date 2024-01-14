#Query Parameter and String Validation
from fastapi import FastAPI,Query
from typing import Union
from typing_extensions import Annotated

app = FastAPI()

@app.get("/items")
async def get_items(q : Annotated[Union[str,None], Query(max_length=10)] =None):
    result = {"name":"raja","age":15}
    if q:
        result.update({"q":q})
    return result



# run this query
'''http://127.0.0.1:8000/items?q=bantysethy'''
#result {"name":"raja","age":15,"q":"bantysethy"}