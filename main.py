from typing import Union
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/searsh/{item_id}")
def searsh(item_id: str, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get("/artist/{item_id}")
def artist(item_id: str, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/album/{item_id}")
def album(item_id: str, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}