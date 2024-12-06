import psycopg2
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def get_db_connection():
    # Fetch environment variables
    db_host = os.getenv("DB_HOST", "db")
    db_name = os.getenv("POSTGRES_DB")
    db_user = os.getenv("POSTGRES_USER")
    db_password = os.getenv("POSTGRES_PASSWORD")

    if not all([db_name, db_user, db_password]):
        raise EnvironmentError("Missing required environment variables.")

    # Connect to PostgreSQL database
    conn = psycopg2.connect(
        host=db_host,
        database=db_name,
        user=db_user,
        password=db_password
    )
    return conn

# Test connection
try:
    conn = get_db_connection()
    print("Connection successful!")
    conn.close()
except Exception as e:
    print(f"Connection failed: {e}")
