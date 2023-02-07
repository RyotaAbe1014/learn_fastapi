from fastapi import FastAPI
from enum import Enum
from pydantic import BaseModel

app = FastAPI()


class ColorModel(BaseModel):
    color_id: int
    color_name: str


class ColorEnum(Enum):
    RED = (1, "red")
    GREEN = (2, "green")
    BLUE = (3, "blue")

    def __init__(self, color_id, color_name):
        self.color_id = color_id
        self.color_name = color_name


@app.get('/color/{color_id}', response_model=ColorModel)
async def get_color(color_id: int):
    """
    受け取ったカラーIDを元にEnumのタプルからカラー名を返す
    """
    color = [c for c in ColorEnum if c.value[0] == color_id][0]
    return ColorModel(color_id=color.value[0], color_name=color.value[1])
