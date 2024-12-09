'''
create a forms that, don't accept another thing
than an image.
'''
import streamlit as st

with st.form("my_form"):
    st.write("Inside the form")
    #slider_val = st.slider("Form slider")
    #checkbox_val = st.checkbox("Form checkbox")
 
    try: 
        file = st.file_uploader("Choose a file")


        # Every form must have a submit button.
        submitted = st.form_submit_button("Submit")
        if submitted:
            st.write("slider", slider_val, "checkbox", checkbox_val)
        
    except:
        "Please Add A file!"

st.write("Outside the form")