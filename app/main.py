import streamlit as st
from pages import dashboard, reports, upload

st.set_page_config(page_title="AI Finance Dashboard", layout="wide")

st.sidebar.title("AI Finance Dashboard")
page = st.sidebar.radio(
    "Navigate",
    ("Upload Transactions", "Dashboard", "Reports"),
    index=0
)

if page == "Upload Transactions":
    upload.show()
elif page == "Dashboard":
    dashboard.show()
elif page == "Reports":
    reports.show()