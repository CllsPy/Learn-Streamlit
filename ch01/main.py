import os, sys
import streamlit as st
import sys

def calculate_sum(n1:float, n2:float) -> float:
    "Adding corresponding elements"
    return n1 + n2

def calculate_sub(n1:float, n2:float) -> float:
    "Subtract corresponding elements"
    return n1 - n2

def calculate_prod(n1:float, n2:float) -> float:
    "Multiply corresponding elements"
    return n1*n2

def calculate_div(n1:float, n2:float) -> float:
    "Division corresponding elements"
    return n1/n2

st.title("Operations")

n1 = st.number_input("N1: ")
n2 = st.number_input("N2: ")

if st.button('SUM'):
    st.write(f"Sum is {calculate_sum(n1, n2)}")

if st.button('SUB'):
    st.write(f"Sub is {calculate_sub(n1, n2)}")

if st.button('PROD'):
    st.write(f"Prod is {calculate_prod(n1, n2)}")

if st.button('DIV'):
    st.write(f"Div is {calculate_div(n1, n2)}")
