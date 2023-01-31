from fastapi import FastAPI, Depends, Path, Query
from pydantic import BaseModel, Field
app = FastAPI()

class Item(BaseModel):
    item_id : int = Field(Path(description="aaaa"))
    item_name: str = Field(Query(description="bbbb"))




@app.get("/items/{item_id}")
async def read_item(item_id: Item = Depends()):
    item = {"item_id": item_id}
    return item