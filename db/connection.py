# db/connection.py

import psycopg2
from psycopg2 import sql

def get_db_connection():
    conn = psycopg2.connect(
        host="localhost",
        database="your_database",
        user="your_user",
        password="your_password"
    )
    return conn
