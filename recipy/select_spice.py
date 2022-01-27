"""
# My Second app
DESC: app for Recipy recommendation
"""
import streamlit as st
from util import get_df_recipy, get_spice_df, even_visualization


def app():
    st.subheader('Recipy Recommendation')
    st.caption('create by Even Pan, Date: 2022/1/27')

    recipes = get_df_recipy()

    st.write('recipes quantity: ', len(recipes))

    with st.container():
        st.image('recipy/spice.jpg', caption='source: unsplash(https://unsplash.com/s/photos)')

    spice_list = ['salt', 'pepper', 'oregano', 'sage', 'parsley', 'rosemary', 'tarragon', 'thyme', 'paprika', 'cumin']
    options = st.multiselect("Enter which spice you are interested(multi-select)", spice_list, spice_list[0])

    spice_df = get_spice_df(recipes, spice_list)


    selection = spice_df.query(' & '.join(options))
    st.write(f'There are `{len(selection)}` recipes after your query.')

    max_number = st.slider('how many to display', min_value=4, max_value=16, value=4)

    selected_result = recipes.iloc[selection.index]
    selected_result = selected_result.dropna(subset=['image', 'url']).head(max_number).reset_index()
    # st.write(selected_result)

    even_visualization(selected_result,max_number)
