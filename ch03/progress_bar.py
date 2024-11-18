import streamlit as st
import wget

progress_text = st.empty()
progress_bar = st.progress(0)

def streamlit_progress_bar(current, total, width):
    percent = int((current/total)*100)
    progress_text.subheader(f'Progress {percent}')
    progress_bar.progress(percent)

wget.download('https://raw.githubusercontent.com/Abacatinhos/agenda-tech-brasil/refs/heads/main/README.md', bar = streamlit_progress_bar)
