import streamlit as st

def show():
    st.title("👤 User Profile")

    menu = st.radio("Select an option:", ["Login", "Signup"])

    if menu == "Login":
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        if st.button("Login"):
            st.success(f"Welcome back, {username}! 🎉")

    elif menu == "Signup":
        new_username = st.text_input("Choose a Username")
        new_password = st.text_input("Choose a Password", type="password")
        if st.button("Sign Up"):
            st.success("Account created successfully! 🎉 Please log in.")
