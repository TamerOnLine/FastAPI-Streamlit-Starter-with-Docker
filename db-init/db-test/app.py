import os
import psycopg2
import time
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def get_db_connection():
    """Try connecting to the database, retry if it fails."""
    while True:
        try:
            conn = psycopg2.connect(
                host=os.getenv("DB_HOST"),
                database=os.getenv("POSTGRES_DB"),
                user=os.getenv("POSTGRES_USER"),
                password=os.getenv("POSTGRES_PASSWORD")
            )
            return conn
        except psycopg2.OperationalError as e:
            print(f"Database not ready yet. Retrying in 5 seconds... Error: {e}")
            time.sleep(5)

if __name__ == "__main__":
    # Wait until the database is ready
    connection = get_db_connection()
    print("Connection successful!")
    connection.close()

    # Keep the container running (if needed)
    while True:
        time.sleep(60)
