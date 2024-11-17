import streamlit as st

col1, col2 = st.columns(2)
def div(n1:float, n2:float) -> float:
    st.info(f'{n1}/{n2} = {n1/n2}')

with col1:
    num1 = st.number_input('First', value=0, step=1)

with col2:
    num2 = st.number_input('Second', value=0, step=1)

if not num1 and num2:
    st.error('Insert a number')
    st.stop()

try:
    div(num1, num2)


## method 1
#except ZeroDivisionError:
#    st.error('Cannot divide by zero')

## method 2

except Exception as e:
    st.error(f'Error{e}')