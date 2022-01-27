import shutil
import gzip
import pandas as pd
import streamlit as st


@st.cache
def extract_gz():
    with gzip.open('recipy/recipeitems-latest.json.gz', 'rb') as f_in:
        with open('recipy/recipeitems-latest.json', 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)


@st.cache(allow_output_mutation=True)
def get_df_recipy():
    df = pd.read_json('recipy/recipeitems-latest.json', lines=True)
    df['description'] = df.description.str.lower()
    df= df.dropna(subset=['image', 'url']).reset_index()
    return df


def even_visualization(df, max_num):
    for i,j in zip(range(max_num-1, 0, -2) , range(max_num-2, 0, -2)):
        res1, res2 = st.columns(2)
        with res1:
            st.subheader(df.name[i])
            st.image(df.image[i])
            st.caption(df.url[i])
        with res2:
            st.subheader(df.name[j])
            st.image(df.image[j])
            st.caption(df.url[j])


@st.cache()
def get_spice_df(df, spice_list):
    spice_df = pd.DataFrame(dict((spice, df.ingredients.str.contains(spice)) for spice in spice_list))
    return spice_df


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
