import streamlit as st


connection_page = st.Page(
    'pages/Connection.py',
    title='Gerenciador de Conexões',
    icon=':material/database:')

professional_page = st.Page(
    'pages/Report_Professional.py',
    title="Relatórios Profissional",
    icon=":material/lab_profile:")


pg = st.navigation([professional_page, connection_page])

# Config page
st.set_page_config(page_title="PÁGINA INICIAL", page_icon=":material/home:")
pg.run()