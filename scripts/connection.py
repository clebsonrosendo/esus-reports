# import streamlit as st
# import pandas as pd


# def new():
#     conn = st.connection("postgresql", type="sql")
#     df = conn.query('SELECT * FROM tb_atendimentos;', ttl="10m")
#     dd = pd.DataFrame(df)

#     return dd

# nerd = new()
# print(nerd)