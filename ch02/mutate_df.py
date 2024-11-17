import numpy as np
import pandas as pd
import streamlit as st

# seed
# create df
# filter

np.random.seed(1)

df = pd.DataFrame(
    np.random.rand(4, 3), 
    columns=('Column 1', 'Column 2', 'Column 3')
    )

st.subheader('Original dataframe')
st.write(df)

df_filter = df[df['Column 1'] > 0.3]
st.subheader('Mutated dataframe')
st.write(df_filter)
