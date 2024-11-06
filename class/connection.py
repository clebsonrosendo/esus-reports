import streamlit as st

@st.cache_resource
def new_connection_database():
    db_connection = st.connection("esus_db", type="sql")

    return db_connection

