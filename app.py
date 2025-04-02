import streamlit as st
from pages import home, about, assessment, resources, profile

st.set_page_config(page_title="Mental Health App", layout="wide")

# Sidebar Navigation
st.sidebar.title("Navigation")
selected_page = st.sidebar.radio("Go to", ["Home", "About", "Assessment", "Resources", "Profile"])

# Load the selected page
if selected_page == "Home":
    home.show()
elif selected_page == "About":
    about.show()
elif selected_page == "Assessment":
    assessment.show()
elif selected_page == "Resources":
    resources.show()
elif selected_page == "Profile":
    profile.show()
