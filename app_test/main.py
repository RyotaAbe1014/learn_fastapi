from fastapi import FastAPI
app = FastAPI()


@app.get("/")
async def index():
    return {"message": "Hello"}


@app.post("/users")
async def users(users: User):
    return {"users": users}

@app.post("/rooms")
async def rooms(rooms: Room):
    return {"rooms": rooms}


@app.post("/booking")
async def booking(booking: Booking):
    return {"booking": booking}
