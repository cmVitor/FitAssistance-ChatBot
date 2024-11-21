import streamlit as st
from cabecalho_utils.ocultar_cabecalho import ocultar_cabecalho_streamlit
from session_state_utils.variables import start_variables
from page_utils.sidebar import config_sidebar

st.set_page_config(page_title="Fit Assistant", page_icon="images\ENGENHARIA DE SOFTWARE-01.png")

ocultar_cabecalho_streamlit()
start_variables()
config_sidebar()

st.text_input("Pergunta", key='user_input', placeholder="Digite sua pergunta aqui...", label_visibility="hidden")
