import pandas as pd
import streamlit as st
st.titles("upload csv")
file=st.file_uploader("Choose a file",type="csv")
if file:
  df=pd.read_csv(file)
  st.write("Preview of uploaded file:")
  st.dataframe(df)
