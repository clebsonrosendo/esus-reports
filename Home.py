import streamlit as st


connection_page = st.Page(
    'pages/Connection.py',
    title='Gerenciador de Conexões',
    icon=':material/database:')

professional_page = st.Page(
    'pages/Report_Professional.py',
    title='Relatórios Profissional',
    icon=':material/analytics:')

services_page = st.Page(
    'pages/Atendimentos.py',
    title='Atendimentos Profissional',
    icon=':material/groups:')

evolution_page = st.Page(
    'pages/Evolucoes.py',
    title='Evoluções',
    icon=':material/how_to_reg:')

time_page = st.Page(
    'pages/Horarios.py',
    title='Horários dos Profissionais',
    icon=':material/pending_actions:')

managerbk_page = st.Page(
    'pages/Gerenciador_Backups.py',
    title='Gerenciador de Backups',
    icon=':material/cloud_upload:')


pg = st.navigation([services_page,
                    professional_page,
                    evolution_page,
                    time_page,
                    managerbk_page,
                    connection_page])

# Config page
st.set_page_config(page_title='PÁGINA INICIAL', page_icon=':material/home:')
pg.run()