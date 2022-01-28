import streamlit as st

# Custom imports 
from multipage import MultiPage
from imdb import imdb_selector
from recipy import select_spice, text_ingredient

from recipy.util import extract_gz

# Create an instance of the app 
app = MultiPage()
extract_gz()
# Title of the main page
st.title("Data Storyteller Application")

# Add all your applications (pages) here
app.add_page("imdb movie selector", imdb_selector.app)
app.add_page("select spice", select_spice.app)
app.add_page("text ingredient", text_ingredient.app)

# The main app
app.run()