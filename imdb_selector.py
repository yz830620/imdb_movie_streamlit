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

def get_unique_genres(df):
    all_unique_genres = df.genres.unique()
    unique_genres = set()
    for multi_genres in all_unique_genres:
        unique_genres.update(multi_genres.split('|'))
    return unique_genres

movie_table = get_df()


table_min_year = int(movie_table.title_year.min())
table_max_year = int(movie_table.title_year.max())

st.write(f'min year: {table_min_year}, max year: {table_max_year}')

max_year = st.slider('movie not more than ...', min_value=table_min_year, max_value=table_max_year, value=2000)
min_year = st.slider('movie not less than ...', min_value=table_min_year, max_value=table_max_year, value=1990)

unique_genres = get_unique_genres(movie_table)

selected_genres = st.selectbox('select the genre you like', unique_genres)

st.write(f'max year: {max_year}, min year: {min_year}, selected genres: {selected_genres}')