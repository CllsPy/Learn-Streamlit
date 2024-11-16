import streamlit as st

with st.form('feedback_form'):
    st.header('feedback_form')

    col1, col2 = st.columns(2)

    with col1:
        name = st.text_input('Please, your name')
        rating = st.slider('Rate', 0, 10, 5)

    with col2:    
        db = st.date_input('birth')
        radio = st.radio("You would recommend this app?", ('Yes', 'No'))
        submit = st.form_submit_button('Submit')