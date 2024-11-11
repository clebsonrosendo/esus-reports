import streamlit as st


def new(arg: str):
    db_connection = st.connection("esus_db", type="sql")
    query = db_connection.query(arg, show_spinner=False, ttl=0)

    return query
