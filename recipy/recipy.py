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

st.title('Recipy Recommendation')

recipes = get_df()

st.write('recipes quantity: ', len(recipes))

# st.write(recipes.head())

with st.container():
    st.image('recipy/spice.jpg', caption='source: unsplash(https://unsplash.com/s/photos)')



spice_list = ['salt', 'pepper', 'oregano', 'sage', 'parsley', 'rosemary', 'tarragon', 'thyme', 'paprika', 'cumin']
options = st.multiselect("Enter which spice you are interested(multi-select)", spice_list, spice_list[0])


spice_df = pd.DataFrame(dict((spice, recipes.ingredients.str.contains(spice)) for spice in spice_list))

selection = spice_df.query(' & '.join(options))
st.write(f'There are `{len(selection)}` recipes after your query.')

selected_result = recipes.iloc[selection.index]
selected_result = selected_result.dropna(subset=['image', 'url']).sample(4).reset_index()
# st.write(selected_result)

with st.container():
    res1, res2 = st.columns(2)

    with res1:
        st.subheader(selected_result.name[0])
        st.image(selected_result.image[0])
        st.write(f'check out recipy [here]({selected_result.url[0]})')

    with res2:
        st.subheader(selected_result.name[1])
        st.image(selected_result.image[1])
        st.write(f'check out recipy [here]({selected_result.url[1]})')

    res3, res4 = st.columns(2)

    with res3:
        st.subheader(selected_result.name[2])
        st.image(selected_result.image[2])
        st.write(f'check out recipy [here]({selected_result.url[2]})')
    
    with res4:
        st.subheader(selected_result.name[3])
        st.image(selected_result.image[3])
        st.write(f'check out recipy [here]({selected_result.url[3]})')
