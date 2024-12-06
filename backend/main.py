from fastapi import HTTPException
from fastapi import FastAPI
from db import get_db_connection

from pydantic import BaseModel


app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI service!"}

# نموذج البيانات باستخدام Pydantic
class ExampleItem(BaseModel):
    name: str
    age: int

@app.post("/example/")
def create_example_item(item: ExampleItem):
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        # استعلام لإدخال البيانات
        cur.execute(
            "INSERT INTO example (name, age) VALUES (%s, %s)",
            (item.name, item.age)
        )
        conn.commit()
        cur.close()
        conn.close()
        return {"message": "Item added successfully", "item": item.dict()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
