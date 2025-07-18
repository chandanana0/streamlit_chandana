import streamlit as st
st.text("Hello! Please enter your name below:")
name = st.text_input("Your Name")
if name:
    st.text(f"Hello, {name}!")
