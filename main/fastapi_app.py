# main.py

from fastapi import FastAPI
from db import get_db_connection
import psycopg2
import json

app = FastAPI()

@app.post("/add_user/")
async def add_user(name: str, email: str, age: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute("INSERT INTO user_data (name, email, age) VALUES (%s, %s, %s)", (name, email, age))
    conn.commit()
    
    cursor.close()
    conn.close()
    
    return {"message": "User added successfully!"}

