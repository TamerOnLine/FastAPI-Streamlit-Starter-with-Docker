# db/connection.py
import psycopg2
import os

def get_db_connection():
    conn = psycopg2.connect(
        host="db",  # اسم الخدمة التي تم تحديدها في docker-compose.yml
        database=os.getenv("POSTGRES_DB"),  # تحميل المتغير من البيئة (من .env أو docker-compose.yml)
        user=os.getenv("POSTGRES_USER"),  # تحميل المتغير من البيئة
        password=os.getenv("POSTGRES_PASSWORD")  # تحميل المتغير من البيئة
    )
    return conn


