import streamlit as st


connection_page = st.Page(
    'pages/conexoes.py',
    title='Gerenciador de Conexões',
    icon=':material/database:')

professional_page = st.Page(
    'pages/profissionais.py',
    title='Relatórios Profissional',
    icon=':material/analytics:')

services_page = st.Page(
    'pages/atendimentos.py',
    title='Atendimentos Profissional',
    icon=':material/groups:')

evolution_page = st.Page(
    'pages/evolucoes.py',
    title='Evoluções',
    icon=':material/how_to_reg:')

time_page = st.Page(
    'pages/horarios.py',
    title='Horários dos Profissionais',
    icon=':material/pending_actions:')

managerbk_page = st.Page(
    'pages/backups.py',
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