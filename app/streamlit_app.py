import streamlit as st

st.title("Streamlit Application")

st.write("This is a simple Streamlit app running in a Docker container.")

user_name = st.text_input("Enter your name:")
if user_name:
    st.write(f"Hello, {user_name}!")
