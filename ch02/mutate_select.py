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

df_filter = df[['Column 1']]
st.subheader('Mutated dataframe')
st.write(df_filter)

st.subheader('Mutated dataframe 2')
asc_df = df.sort_values(by='Column 1', ascending=True)
st.write(asc_df)


st.subheader('Mutated dataframe 3')
mutate_df = df.assign(Column_4 = lambda x: df['Column 1']*2)
st.write(mutate_df)

## You can also
## merge, grouby 
## dataframes (check pandas doc)