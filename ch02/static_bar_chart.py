import pandas as pd
import streamlit as st
import matplotlib.pyplot as fig
import plotly.graph_objects as go


data = pd.DataFrame(
    data={'Name':['Carlos', 'Bia', 'David'], 
    'Score1': [1, 10, 5], 
    'Score2':[2, 8, 6]
    })

st.header("Bar")
data.set_index('Name').plot(kind='bar', stacked=False, xlabel='name', ylabel='score')
st.pyplot(fig)

st.header("Line")
data.set_index('Name').plot(kind='line', stacked=False, xlabel='name', ylabel='score')
st.pyplot(fig)


st.header("Interative")

## we can use plotly for 
## interative graphs

fig = go.Figure(data=[
    go.Line(name='S1', x=data['Name'], y=data['Score1']),
    go.Line(name='S2', x=data['Name'], y=data['Score2']),
])

fig.update_layout(
    xaxis_title='Name',
    yaxis_title='Score',
    legend_title='Name'

)

st.plotly_chart(fig)