"""
# My first app
Here's our first attempt at using data to create a table:
"""

import streamlit as st
import pandas as pd

@st.cache
def get_df():
    df = pd.read_csv('movie_metadata.csv')
    return df

movie_table = get_df()


table_min_year = int(movie_table.title_year.min())
table_max_year = int(movie_table.title_year.max())

st.write(f'min year: {table_min_year}, max year: {table_max_year}')

max_year = st.number_input('movie not newer than ...', min_value=table_min_year, max_value=table_max_year, value=2000)
min_year = st.number_input('movie not older than ...', min_value=table_min_year, max_value=table_max_year, value=1990)


st.write(f'max year: {max_year}, min year: {min_year}')