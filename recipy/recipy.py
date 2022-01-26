"""
# My Second app
DESC: app for Recipy recommendation

"""
from lib2to3.pgen2.pgen import DFAState
import shutil
import streamlit as st
import pandas as pd
import gzip

with gzip.open('recipy/recipeitems-latest.json.gz', 'rb') as f_in:
    with open('recipy/recipeitems-latest.json', 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)


@st.cache(allow_output_mutation=True)
def get_df():
    df = pd.read_json('recipy/recipeitems-latest.json', lines=True)
    df['description'] = df.description.str.lower()
    return df

st.title('recipy recommendation')

recipes = get_df()

st.write('recipes quantity: ', len(recipes))


spice_list = ['salt', 'pepper', 'oregano', 'sage', 'parsley', 'rosemary', 'tarragon', 'thyme', 'paprika', 'cumin']
options = st.multiselect("enter which spice you are interested(multi-select)", spice_list, spice_list[0])


spice_df = pd.DataFrame(dict((spice, recipes.ingredients.str.contains(spice)) for spice in spice_list))

selection = spice_df.query(' & '.join(options))
st.write(len(selection))

st.write(recipes.name[selection.index])