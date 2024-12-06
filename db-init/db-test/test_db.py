import sys

# Add the path containing db.py
sys.path.append('/app')

from db import get_db_connection

# Test the connection
try:
    with get_db_connection() as conn:
        print("Successfully connected to the database!")
except Exception as e:
    print(f"Connection failed: {e}")

