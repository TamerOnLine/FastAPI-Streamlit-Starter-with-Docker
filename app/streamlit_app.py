# app.py

import streamlit as st
import psycopg2
import os

# الاتصال بقاعدة البيانات
def get_db_connection():
    conn = psycopg2.connect(
        host="db",  # اسم الخدمة في docker-compose
        database=os.getenv("POSTGRES_DB"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD")
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
