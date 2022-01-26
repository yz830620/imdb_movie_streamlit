"""
# My Second app
DESC: app for Recipy recommendation

"""
import streamlit as st
import pandas as pd
import subprocess



subprocess.run(["curl", "-L", "-o", "recipeitems-latest.json.gz", "https://docs.google.com/uc?export=download&id=1hGSFmpptgZyX4jOal8B9LFDiLZACPSqO"])
subprocess.run(["gunzip", "recipeitems-latest.json.gz"])


recipes = st.cache(pd.read_json('recipeitems-latest.json', lines=True))
st.write(recipes.head())