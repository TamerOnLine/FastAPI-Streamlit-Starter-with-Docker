# db.py

import psycopg2
from psycopg2 import sql


def get_db_connection():
    conn = psycopg2.connect(
        host="db",  
        database="postgres",  
        user="postgres",  
        password="password"  
    )
    return conn
