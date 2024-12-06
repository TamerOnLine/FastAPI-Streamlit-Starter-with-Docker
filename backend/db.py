from db import get_db_connection

# Example usage
try:
    with get_db_connection() as conn:
        print("Connection established!")
except Exception as e:
    print(f"Connection error: {e}")
