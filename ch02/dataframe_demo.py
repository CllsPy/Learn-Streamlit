import streamlit as st
import pandas as pd
import plotly.express as px

program = st.sidebar.selectbox('Select App', ['Dataframe', 'Demo'])
code = st.sidebar.checkbox('Display Code')

if program == 'Dataframe':
    df = px.data.stocks()    
    st.title('DataFrame Demo')
    stocks = st.multiselect(
        'Select stocks', 
        df.columns[1:], [df.columns[1]])

    st.subheader('Stock Values')
    st.write(df[['date'] + stocks].set_index('date'))

    fig = px.line(
        df, x='date', 
        y=stocks, hover_data={'date': '|%Y %b %d'})
    st.write(fig)


if code:
 
    st.code(
    
        """
        
        import streamlit as st
        
        import pandas as pd
        
        import plotly.express as px
        
        df = px.data.stocks()
        
        st.title('DataFrame demo')
        
        program = st.sidebar.selectbox('Select 
        program',['Dataframe Demo'])
        
        code = st.sidebar.checkbox('Display code')
        
        stocks = st.multiselect('Select stocks',df.columns[1:],[df.
        columns[1]])
        
        st.subheader('Stock value')
        
        st.write(df[['date'] + stocks].set_index('date'))
        
        fig = px.line(df, x='date', y=stocks,
        
        hover_data={"date": "|%Y %b %d"}
        
        )
        
        st.write(fig)
        
        """
    
    )

