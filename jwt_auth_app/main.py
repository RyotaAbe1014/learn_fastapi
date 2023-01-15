from fastapi import FastAPI, Depends
app = FastAPI()
from auth.oauth2 import oauth2_scheme

@app.get("/hello")
async def index(token: str = Depends(oauth2_scheme)):
    return {"message": "hello world"}