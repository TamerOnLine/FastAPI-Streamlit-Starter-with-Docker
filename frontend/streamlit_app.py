import streamlit as st
from db import get_connection

st.title("Streamlit Data Entry")

# Form to get user input
with st.form("data_entry_form"):
    name = st.text_input("Name")
    age = st.number_input("Age", min_value=0, max_value=120)
    submitted = st.form_submit_button("Submit")

if submitted:
    # Validate inputs
    if name.strip() == "":
        st.error("Name cannot be empty.")
    elif age <= 0:
        st.error("Age must be a positive number.")
    else:
        # Insert data into the database
        try:
            conn = get_connection()
            cursor = conn.cursor()
            query = "INSERT INTO example (name, age) VALUES (%s, %s)"
            cursor.execute(query, (name, age))
            conn.commit()
            cursor.close()
            conn.close()
            st.success("Data successfully inserted into the database!")
        except Exception as e:
            st.error(f"An error occurred: {e}")
