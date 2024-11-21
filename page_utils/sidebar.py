import streamlit as st

def config_sidebar():

    st.sidebar.title("Fit Assistant")

    st.sidebar.write("""
        **O Fit Assistant** é uma ferramenta de linguagem que utiliza inteligência artificial e bases contextuais para fornecer respostas de alta qualidade sobre vida saudável e treinos personalizados.
    """)
    
    st.sidebar.image("images\ENGENHARIA DE SOFTWARE-01.png", use_column_width=True)