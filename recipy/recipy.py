"""
# My Second app
DESC: app for Recipy recommendation

"""
import shutil
import streamlit as st
import pandas as pd
import gzip

with gzip.open('recipy/recipeitems-latest.json.gz', 'rb') as f_in:
    with open('recipy/recipeitems-latest.json', 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)


@st.cache
def get_df():
    df = pd.read_json('recipeitems-latest.json', lines=True)
    return df

recipes = get_df()
st.write(recipes.head(10))
st.write(len(recipes))