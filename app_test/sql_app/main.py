from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from typing import List
from . import crud, models, schemas
from .database import SessionLocal, engine

# データベースを生成する(?)
models.Base.metadata.create_all(bind=engine)


app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# @app.get("/")
# async def index():
#     return {"message": "Hello"}

# read
@app.get("/users", response_model=List[schemas.User])
# response_modelとは情報を返す際のデータ構造を示す,
# schemas.Userは基本的にレコードと1対1のため複数返す場合はListで囲い、List型で返すことを明記する必要がある
async def read_users(skip: int = 100, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/rooms", response_model=List[schemas.Room])
async def read_rooms(skip: int = 100, limit: int = 100, db: Session = Depends(get_db)):
    rooms = crud.get_rooms(db, skip=skip, limit=limit)
    return rooms


@app.get("/bookings", response_model=List[schemas.Booking])
async def read_bookings(skip: int = 100, limit: int = 100, db: Session = Depends(get_db)):
    bookings = crud.get_bookings(db, skip=skip, limit=limit)
    return bookings


# create
@app.post("/users")
async def users(users: User):
    return {"users": users}


@app.post("/rooms")
async def rooms(rooms: Room):
    return {"rooms": rooms}


@app.post("/bookings")
async def booking(booking: Booking):
    return {"booking": booking}
