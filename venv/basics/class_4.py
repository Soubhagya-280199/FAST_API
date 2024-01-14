#Request Body
'''
When you need to send data from a client (let's say, a browser) to your API, you send it as a request body.

A request body is data sent by the client to your API. A response body is the data your API sends to the client.'''


from fastapi import FastAPI,Query,Path
from typing import Union
from pydantic import BaseModel

app = FastAPI()
#Example 1
class Item(BaseModel):
    itemname : str
    description : Union [str,None] = None
    count : Union [int, None] = None
    price : Union [float, None] = None

@app.post("/items")
async def get_item(item : Item):
    return {"item": item}

### Example 2
class Numbers(BaseModel):
    item_name : str
    item_price : Union [int ,None] = None
    item_tax : Union [float , None] = None

@app.post("/item/item_tax")
async def item_cal(numbers : Numbers):
    number_dict = numbers.dict()
    if numbers.item_tax:
        total_price = numbers.item_tax + numbers.item_price
        number_dict.update({f"total": total_price})
    return number_dict




## Request body + path parameters
class School(BaseModel):
    class_name : Union [str ,None] =None
    stud_count : Union [float ,None] = None
    stud_age : Union [int, None] = None

@app.post("/school/{class_no}")
async def school_data(data : School , class_no : int ):
    result = data.dict()
    if class_no:
        count = data.stud_count + data.stud_age
        result.update({f"Calc": count})
        return {f"class_no exist so": result}

    return {f"class_no Not exist so":result}





# an example of query parameter with string validation
@app.get("/string_validation")
async def ignore(q: Union[str , None ] =Query(None, min_length = 3 , max_length= 10)):
    result  = {"text":"I am inox ipo"}
    if q:
        result.update({"Query result": q})

# an example of path parameter with Numeric validation
@app.get("/pass/{pass_id}")
async def pass_ignore(*, pass_id :int =Path(...,title="numeric validator",ge=2,le=8),
                      q: str="Hello"):
    result = {"item_id":pass_id}
    if q:
        result.update({"Query":q})
    return result
