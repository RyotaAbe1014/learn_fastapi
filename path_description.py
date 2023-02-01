from fastapi import FastAPI, Depends, Path, Query, Body
from pydantic import BaseModel, Field
app = FastAPI()





class Item(BaseModel):
    item_id : int = Field(Path(None,description="aaaa"))
    item_name: str = Field(Query(None, description="bbbb"))
    item_name2: str = Field(Body(None, description="ccc"))



@app.get("/items/{item_id}")
async def read_item(item_id: Item = Depends()):
    item = {"item_id": item_id}
    return item