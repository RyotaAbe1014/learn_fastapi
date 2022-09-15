from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
app = FastAPI()


# @app.get("/hello")
# async def index():
#     return {"message": "hello world"}


# @app.get("/hello2")
# async def index():
#     return {"message": "hello world2"}


# @app.get("/countries/{country_name}")
# async def country(country_name: str):
#     return {"country_name": country_name}


# @app.get("/countries/japan")
# async def country_japan():
#     return {"message": "japan"}


# @app.get("/countries/")
# async def country(country_name: str = "japan", country_number: int = 1):
#     return {
#         "country_name": country_name,
#         "country_number": country_number,
#     }


# @app.get("/countries/{country_name}")
# async def country(country_name: str = "japan", city_name: str = "tokyo"):
#     return {
#         "country_name": country_name,
#         "city_name": city_name,
#     }


# @app.get("/countries/")
# async def country(country_name: Optional[str] = None, country_number: Optional[int] = None):
#     return {
#         "country_name": country_name,
#         "country_number": country_number,
#     }



class Item(BaseModel):
  name: str
  description: Optional[str] = None
  price: int 
  tax: Optional[float] = None

@app.post("/item/")
async def create_item(item: Item):
  return {"item": f"この商品は{item.name}で値段は税込{int(item.price*item.tax)}円です"}
