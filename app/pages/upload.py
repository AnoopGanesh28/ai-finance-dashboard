import streamlit as st

def show():
    st.header("Upload Transactions")
    uploaded_file=st.file_uploader("Choose a CSV file", type="csv")
    if uploaded_file is not None:
        st.success("File uploaded!")
        