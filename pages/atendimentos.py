import streamlit as st
import scripts.connection as conn
import pandas as pd
import time
import datetime


st.title('Atendimentos Profissional')
st.warning('Recurso Indisponível no Momento')


file = open("../querys/atendimentos_prof.sql", "r")
file = str(file.read())

# Get data DB
query = conn.new(file)
# Generate DataFrame
df = pd.DataFrame(query)
# Date Filter
select_date_i = st.selectbox('Data', options=df['Data'].unique(), index=None, placeholder='Escolha um dia', format="DD/MM/YYYY")
select_date_f = st.selectbox('Data', options=df['Data'].unique(), index=None, placeholder='Escolha um dia', format="DD/MM/YYYY")

# Show Button
if select_date:
    df_filtered = df[df["Data"] >= select_date_i & df["Data"] <= select_date_f]
    st.dataframe(df_filtered, hide_index=False)
