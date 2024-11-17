import streamlit as st

def display_name(name: str) -> str:
    st.info(f'**Name**: {name}')

name_input = st.text_input('Your name:')

if not name_input:
    st.error('No name entered')
    st.stop()

display_name(name_input)