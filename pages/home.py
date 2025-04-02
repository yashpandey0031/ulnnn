import streamlit as st
import os

def show():
    # Custom Styling (Background Color)
    st.markdown("""
        <style>
            .stApp {
                background-color: #B7E4C7;
            }
            .stButton>button {
                background-color: #2C3E50;
                color: white;
                border-radius: 10px;
                font-size: 18px;
                padding: 10px 20px;
            }
            .stButton>button:hover {
                background-color: #34495E;
            }
        </style>
    """, unsafe_allow_html=True)

    # Title and Subtitle
    st.markdown('<h1 style="text-align:center; color:black; font-size:50px; font-weight:bold;">Your Mind Matters - Explore, Understand, Heal</h1>', unsafe_allow_html=True)

    # Load Local Image
    image_path = os.path.join("assets", "1.jpg")    
    st.image(image_path, use_container_width=True)

    # Why Mental Health Matters
    st.markdown('<h1 style="text-align:center; color:black; font-size:50px; font-weight:bold;">Why Your Mental Health Matters?</h1>', unsafe_allow_html=True)
    st.markdown('<h5 style="text-align:center; color:black; font-size:20px;">Mental health matters because it affects everything—how you think, feel, and interact with the world. A healthy mind helps you handle stress, build strong relationships, and stay motivated. Ignoring mental health can lead to burnout, anxiety, and struggles in daily life. Just like physical health, taking care of your mind ensures long-term well-being and happiness.</h5>', unsafe_allow_html=True)

    # Load Second Image
    image_path = os.path.join("assets", "2.png")
    st.image(image_path, use_container_width=True)

    # Student Mental Health Section
    st.markdown('<h3 style="color:black;">What About Your Mental Health as a Student?</h3>', unsafe_allow_html=True)

    st.markdown("""
        <ul style="color:black; font-size:18px;">
            <li><b>🧠 Better Concentration & Memory</b> – Reduces stress and boosts cognitive function.</li>
            <li><b>⏳ Effective Time Management</b> – Keeps you motivated and organized.</li>
            <li><b>💪 Stronger Resilience</b> – Helps you handle academic pressure and setbacks.</li>
            <li><b>🤝 Healthy Relationships</b> – Supports social interactions and teamwork.</li>
            <li><b>😊 Overall Well-Being</b> – Prevents burnout, anxiety, and emotional exhaustion.</li>
        </ul>
    """, unsafe_allow_html=True)

    # Custom Button
    if st.button("Take Assessment"):
        st.success("Redirecting to Assessment Page...")
