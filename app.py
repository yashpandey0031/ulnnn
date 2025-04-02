import streamlit as st
from pages import home, about, assessment, resources, profile

st.set_page_config(page_title="Mental Health App", layout="wide")

# If sidebar isn't needed, remove its content
for _ in range(10):  
    st.sidebar.empty()

# Sidebar Navigation
st.sidebar.title("Navigation")
selected_page = st.sidebar.radio("Go to", ["Home", "Assessment", "Resources","About Us"])

# Load the selected page
if selected_page == "Home":
    home.show()
elif selected_page == "About Us":
    about.show()
elif selected_page == "Assessment":
    assessment.show()
elif selected_page == "Resources":
    resources.show()
