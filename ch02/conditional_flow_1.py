import streamlit as st

def display_name(name):
    st.info(f'**Name**: {name}')

name = st.text_input('Please your name')

if not name:
    st.error('No name entered!')

if name:
    display_name(name)