import streamlit as st
import os

def show():
    # Custom Styling for Centered Button & Clean Layout
    st.markdown("""
        <style>
            /* Set global background & text color */
            .stApp {
                background-color: #121212;
                color: white;
            }

            /* Style headings */
            h1, h3, h5 {
                color: white !important;
                text-align: center;
            }

            /* Style unordered list */
            ul {
                color: white !important;
                font-size: 18px;
                padding-left: 50px;
                padding-right: 50px;
                text-align: left;
            }

            /* Center the button */
            .button-container {
                display: flex;
                justify-content: center;
                align-items: center;
                margin-top: 30px;
                margin-bottom: 30px;
            }

            .stButton>button {
                background-color: #2C3E50;
                color: white;
                border-radius: 10px;
                font-size: 22px;
                padding: 15px 30px;
                border: none;
                display: block;
                margin: auto; /* Forces centering */
            }

            .stButton>button:hover {
                color: #1E90FF !important; /* Changes text color to blue */
                border: 2px solid #1E90FF !important; /* Changes border to blue */
            }

            /* Style text for readability */
            .text-box {
                padding: 20px;
                text-align: center;
                font-size: 20px;
                line-height: 1.6;
            }
        </style>
    """, unsafe_allow_html=True)

    # Title
    st.markdown('<h1>Your Mind Matters - Explore, Understand, Heal</h1>', unsafe_allow_html=True)

    # Student Mental Health Section (Directly Below Main Title)
    st.markdown('<h3>What About Your Mental Health as a Student?</h3>', unsafe_allow_html=True)
    st.markdown("""
        <ul>
            <li><b>🧠 Better Concentration & Memory</b> – Reduces stress and boosts cognitive function.</li>
            <li><b>⏳ Effective Time Management</b> – Keeps you motivated and organized.</li>
            <li><b>💪 Stronger Resilience</b> – Helps you handle academic pressure and setbacks.</li>
            <li><b>🤝 Healthy Relationships</b> – Supports social interactions and teamwork.</li>
            <li><b>😊 Overall Well-Being</b> – Prevents burnout, anxiety, and emotional exhaustion.</li>
        </ul>
    """, unsafe_allow_html=True)

        # Centered Button (Now properly centered with better styling)
    st.markdown("""
            <style>
                .button-container {
                    display: flex;
                    justify-content: center;
                    margin-top: 30px;
                }
                .stButton>button {
                    background-color: #2C3E50; 
                    color: white;
                    border-radius: 10px;
                    font-size: 22px;
                    padding: 15px 30px;
                    border: none;
                }
                .stButton>button:hover {
                    background-color: #1E90FF;
                }
            </style>
        """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 2, 1])  # Creates three columns, centering the button
    with col2:  
            if st.button("Take Assessment"):
                st.switch_page("pages\assessment.py")  # Redirects to assessment.py (if using multipage)


    # Load and display first image
    image_path = os.path.join("assets", "1.jpg")    
    st.image(image_path, use_container_width=True)

    # Why Mental Health Matters
    st.markdown('<h1>Why Your Mental Health Matters?</h1>', unsafe_allow_html=True)
    st.markdown('<div class="text-box">Mental health affects how you think, feel, and interact with the world. A healthy mind helps handle stress, build strong relationships, and stay motivated. Ignoring mental health can lead to burnout, anxiety, and struggles in daily life. Just like physical health, taking care of your mind ensures long-term well-being and happiness.</div>', unsafe_allow_html=True)

    # Load and display second image
    image_path = os.path.join("assets", "2.png")
    st.image(image_path, use_container_width=True)
