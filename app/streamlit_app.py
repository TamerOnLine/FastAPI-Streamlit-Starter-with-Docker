import streamlit as st
import requests

st.title("Streamlit Application")

st.write("This is a simple Streamlit app running in a Docker container.")

name = st.text_input("Enter a name:")

# إذا كان هناك اسم مدخل من قبل المستخدم، إرسال البيانات إلى FastAPI
if name:
    response = requests.post("http://fastapi:8000/add_name", json={"name": name})
    if response.status_code == 200:
        st.write(f"Name received: {response.json()['name_received']}")
    else:
        st.write("Error sending data to FastAPI")
