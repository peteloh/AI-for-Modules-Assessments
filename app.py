"""
# My first app
Here's our first attempt at using data to create a table:
"""

import streamlit as st
import pandas as pd

import main

st.set_page_config(layout="wide")

st.header("Exercise A")
dataframe = main.analyse("ExA")
st.write(dataframe)

st.header("Exercise B")
dataframe = main.analyse("ExB")
st.write(dataframe)

st.header("Exercise C")
dataframe = main.analyse("ExC")
st.write(dataframe)

st.header("Exercise D")
dataframe = main.analyse("ExD")
st.write(dataframe)