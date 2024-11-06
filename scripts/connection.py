import streamlit as st


def query(arg:str):
    db_connection = st.connection("postgresql", type="sql")
    df = db_connection(arg, show_spinner=False)

    return df
