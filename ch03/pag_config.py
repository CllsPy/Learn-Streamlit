import streamlit as st
from PIL import Image

icon = Image.open('/workspace/Learn-Streamlit/citron.png')

st.set_page_config(
    page_title="My Web Page",
    page_icon=icon,
    layout='centered',
    initial_sidebar_state='expanded',
    menu_items={
        'Get Help': 'https://streamlit.io/',
        'Report a bug': 'https://streamlit.io/',
        'About':'https://streamlit.io/',
    }
)

st.sidebar.title('Hello world')
st.title('Hello world')