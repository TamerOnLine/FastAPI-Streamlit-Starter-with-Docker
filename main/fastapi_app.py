from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class NameRequest(BaseModel):
    name: str

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

@app.post("/add_name")
async def add_name(data: NameRequest):
     return {"name_received": data.name}
