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
    df= df.dropna(subset=['image', 'url']).reset_index(drop=True)
    return df


def even_visualization(df, max_num):
    DATA_PER_ROW = st.sidebar.slider('how many data per row?', min_value=2, max_value=5, value=3)
    res = st.columns(DATA_PER_ROW)   

    for idx, row in reversed(list(df.iterrows())):
        reversed_list_idx = abs(idx-max_num+1)%DATA_PER_ROW
        with res[reversed_list_idx]:
            st.write(row['name'])
            st.image(row['image'])
            st.caption(f"[link to page]({row['url']})")


@st.cache()
def get_spice_df(df, spice_list):
    spice_df = pd.DataFrame(dict((spice, df.ingredients.str.contains(spice)) for spice in spice_list))
    return spice_df
