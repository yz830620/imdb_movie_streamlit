"""
# My Second app
DESC: app for Recipy recommendation

"""

import streamlit as st

from .util import get_df_recipy, get_spice_df, even_visualization


def app():
    st.subheader('Recipy Recommendation')
    st.caption('create by Even Pan, Date: 2022/1/27')

    recipes = get_df_recipy()

    st.write('recipes quantity: ', len(recipes))

    interested_ingredient = st.text_input("try to type in the ingredient you are interested in~~", "shit")

    st.write(f'There are `{recipes.ingredients.str.contains(interested_ingredient).sum()}` recipes contain `{interested_ingredient}`')

    ingredient_mask = recipes.ingredients.str.contains(interested_ingredient)

    max_number = st.sidebar.slider('how many to display', min_value=4, max_value=30, value=15)

    ingredient_recipy = recipes[ingredient_mask].head(max_number).reset_index()

    even_visualization(ingredient_recipy, max_number)

if __name__ == "__main__":
    app()