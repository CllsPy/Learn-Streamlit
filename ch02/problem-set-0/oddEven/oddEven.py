import streamlit as st


'''
Question 1: Flow Control
Write a Streamlit app that takes a user input (an integer) and:

- If the number is even, display "The number is even."
- If the number is odd, display "The number is odd."
'''

number = st.number_input('')
st.button('enviar')

if st.button:
    if number%2 == 0:
        st.write(f'{number} is even')

    else:
        st.write(f'{number} is odd')