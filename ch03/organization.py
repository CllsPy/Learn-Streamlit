import streamlit as st
from datetime import datetime

# Expander in sidebar
st.sidebar.header('Expander')
with st.sidebar.expander('Time'):
    time = datetime.now().strftime('%H:%M:%S')
    st.write('**%s**' %(time))

with st.sidebar.expander('Hour'):
    st.write('HOURS')


st.sidebar.header('Columns')
col1, col2 = st.sidebar.columns(2)

with col1:
    op1 = st.selectbox('Choose', ['A', 'B'])

with col2:
    op2 = st.selectbox('Choose', ['D', 'F'])

container  = st.sidebar.container()
container.subheader('Container')
op3 = container.slider('Please slection opt 3')
st.sidebar.warning('Elements outside of container')
container.info('**Option 3:** %s' % (op3))

st.subheader('Columns')
col1, col2 = st.columns(2)

with col1:
    st.selectbox('Op4', ['ABC', 'ASW'])

with col2:
    st.selectbox('Op5', ['ASWA', 'ASSW'])

container = st.container()
container.subheader('Container')
op6 = container.slider('Values')
container.write('SOME RANDOM TEXT')
st.warning('out element')
placeholder = st.empty()