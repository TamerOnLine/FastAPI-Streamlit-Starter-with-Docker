# app.py

import streamlit as st
import psycopg2


def get_db_connection():
    conn = psycopg2.connect(
        host="db",  
        database="postgres",  
        user="postgres",  
        password="password"  
    )
    return conn

# إضافة بيانات مستخدم
st.title('Add User Data')

name = st.text_input('Name')
email = st.text_input('Email')
age = st.number_input('Age', min_value=0)

if st.button('Submit'):
    if name and email:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        cursor.execute("INSERT INTO user_data (name, email, age) VALUES (%s, %s, %s)", (name, email, age))
        conn.commit()
        
        cursor.close()
        conn.close()
        
        st.success('User data added successfully!')
    else:
        st.error('Please fill in all fields')
