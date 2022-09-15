from fastapi import FastAPI

app = FastAPI()


@app.get("/hello")
async def index():
    return {"message": "hello world"}


@app.get("/hello2")
async def index():
    return {"message": "hello world2"}


@app.get("/countries/{country_name}")
async def country(country_name: str):
    return {"country_name": country_name}


@app.get("/countries/japan")
async def country_japan():
    return {"message": "japan"}
