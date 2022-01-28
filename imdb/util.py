import pandas as pd
import streamlit as st


@st.cache
def get_df_imdb():
    df = pd.read_csv('imdb/movie_metadata.csv')
    df= df.dropna(subset=['title_year'])
    df['title_year'] = df.title_year.astype(int)
    return df


def get_unique_genres(df):
    all_unique_genres = df.genres.unique()
    unique_genres = set()
    for multi_genres in all_unique_genres:
        unique_genres.update(multi_genres.split('|'))
    return sorted(unique_genres)
