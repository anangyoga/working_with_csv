import pandas as pd
import streamlit as st

st.title("CSV Operation")

# panda used when we're working with tabular data
# if the pandas has wiggly yellow line, just run the command below:
# python -m venv .venv
# source ./.venv/Scripts/activate
# pip install pandas

with open("data.csv") as file:
  csv = pd.read_csv(file)
  # print(csv)
  st.write("### Data")
  st.dataframe(csv)

# to display on streamlit, just install it:
# pip install streamlit
