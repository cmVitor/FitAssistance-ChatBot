import streamlit as st

def start_variables():
    if 'messages' not in st.session_state:
        st.session_state.messages = []

    if 'scroll_position' not in st.session_state:
        st.session_state['scroll_position'] = None