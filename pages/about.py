import streamlit as st

def show():
    # Title
    st.title("ℹ About This Project")

    # Project Description
    st.write("""
    This project is an **AI-powered mental health assessment tool** designed to help individuals evaluate their mental well-being 
    and access **useful resources** for guidance and support. 

    ### 🔹 Features:
    - 🧠 **AI-based mental health prediction** based on a structured quiz.
    - 🎯 **Personalized recommendations** tailored to the user's responses.
    - 🔒 **Secure user authentication** for data privacy.
    - 📚 **Comprehensive mental health resources** to guide users in seeking help.
    - 🌍 **Aligned with Sustainable Development Goals (SDGs).**
    """)

    # SDGs Covered
    st.markdown("""
    ### 🌏 SDGs Covered:
    - **🩺 SDG 3: Good Health & Well-being** – Promoting mental health awareness and accessibility.
    - **🎓 SDG 4: Quality Education** – Providing educational resources on mental well-being.
    - **⚖ SDG 10: Reduced Inequalities** – Ensuring access to mental health support for all.
    - **🤝 SDG 17: Partnerships for the Goals** – Collaborating with organizations to improve mental health accessibility.
    """)

    # Disclaimer
    st.markdown("""
    ---
    ⚠ **Disclaimer:**  
    The AI-generated quiz **is not a medical diagnosis**. It is only meant to give you a general idea about your mental health condition.  
    If you're experiencing mental health challenges, **please consult a qualified medical professional**.  
    """)

