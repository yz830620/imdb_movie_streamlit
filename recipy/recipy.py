"""
# My Second app
DESC: app for Recipy recommendation

"""
import streamlit as st
import pandas as pd
import subprocess



subprocess.run(["wget ", "-O", "recipeitems-latest.json.gz", "'https://docs.google.com/uc?export=download&id=1hGSFmpptgZyX4jOal8B9LFDiLZACPSqO'"])
subprocess.run(["gunzip", "recipeitems-latest.json.gz"])
