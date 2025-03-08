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
  # set index will set the X & Y index based on column
  st.bar_chart(csv.set_index("name")["salary"])
  # the line above will display only Name & Salary based on the data

# to display on streamlit, just install it:
# pip install streamlit
