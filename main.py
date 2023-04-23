
from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id", "q"}

import json

@app.post("/json")
def write_json(json_data: dict):
    with open("data.json", "w") as f:
        json.dump(json_data, f)
    return {"message": "JSON data written successfully"}

@app.get("/json")
def read_json():
    with open("data.json", "r") as f:
        json_data = json.load(f)
    return json_data