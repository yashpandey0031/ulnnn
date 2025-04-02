import streamlit as st

def show():
    # Custom CSS Styling
    st.markdown("""
        <style>

            /* Headings */
            .title {
                text-align: center;
                color: white;
                font-size: 40px;
                font-weight: bold;
                margin-top: 20px;
            }
            
            .section-title {
                font-size: 28px;
                margin-top: 30px;
                font-weight: bold;
            }

            /* Links Styling */
            .resource-links a {
                color: #154360;
                text-decoration: none;
                font-size: 18px;
                font-weight: bold;
            }

            .resource-links a:hover {
                color: #1B4F72;
                text-decoration: underline;
            }

            /* Lists */
            .resource-list {
                font-size: 18px;
                color: white;
                padding-left: 20px;
            }

            /* Centered Button */
            .stButton>button {
                display: block;
                margin: 20px auto;
                background-color: #1B4F72;
                color: white;
                border-radius: 10px;
                font-size: 18px;
                padding: 12px 24px;
                font-weight: bold;
            }

            .stButton>button:hover {
                background-color: #154360;
            }
        </style>
    """, unsafe_allow_html=True)

    # Title
    st.markdown('<h2 class="title">📚 Mental Health Resources</h2>', unsafe_allow_html=True)

    # Organizations & Help Centers
    st.markdown('<p class="section-title">🏥 Organizations & Help Centers</p>', unsafe_allow_html=True)
    st.markdown("""
    <ul class="resource-list">
        <li><a href="https://www.who.int" class="resource-links">World Health Organization (WHO)</a></li>
        <li><a href="https://www.nami.org" class="resource-links">National Alliance on Mental Illness (NAMI)</a></li>
        <li><a href="https://www.mhanational.org" class="resource-links">Mental Health America (MHA)</a></li>
        <li><a href="https://www.apa.org" class="resource-links">American Psychological Association (APA)</a></li>
        <li><a href="https://www.samhsa.gov" class="resource-links">SAMHSA (US Government Mental Health)</a></li>
    </ul>
    """, unsafe_allow_html=True)

    # Recommended Books
    st.markdown('<p class="section-title">📖 Recommended Books</p>', unsafe_allow_html=True)
    st.markdown("""
    <ul class="resource-list">
        <li>The Happiness Trap - Russ Harris</li>
        <li>Atomic Habits - James Clear</li>
        <li>Feeling Good: The New Mood Therapy - David D. Burns</li>
        <li>Lost Connections - Johann Hari</li>
        <li>The Mindful Way Through Depression - Mark Williams</li>
        <li>The Upward Spiral - Alex Korb</li>
    </ul>
    """, unsafe_allow_html=True)

    # Research Papers
    st.markdown('<p class="section-title">📄 Research Papers & Articles</p>', unsafe_allow_html=True)
    st.markdown("""
    <ul class="resource-list">
        <li><a href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3584580/" class="resource-links">Cognitive Behavioral Therapy: An Overview</a></li>
        <li><a href="https://www.frontiersin.org/articles/10.3389/fpsyg.2019.00487/full" class="resource-links">Effects of Meditation on Mental Health</a></li>
        <li><a href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7452876/" class="resource-links">Social Media & Mental Health: A Review</a></li>
        <li><a href="https://journals.sagepub.com/doi/10.1177/1073858415608147" class="resource-links">Neuroplasticity & Mental Health</a></li>
    </ul>
    """, unsafe_allow_html=True)

    # Online Courses
    st.markdown('<p class="section-title">🎓 Online Courses & Webinars</p>', unsafe_allow_html=True)
    st.markdown("""
    <ul class="resource-list">
        <li><a href="https://www.coursera.org/learn/the-science-of-well-being" class="resource-links">The Science of Well-Being – Yale (Free)</a></li>
        <li><a href="https://palousemindfulness.com" class="resource-links">Mindfulness-Based Stress Reduction (MBSR) Course</a></li>
        <li><a href="https://www.coursera.org/specializations/positive-psychology" class="resource-links">Positive Psychology – UPenn</a></li>
    </ul>
    """, unsafe_allow_html=True)

    # Mental Health Apps
    st.markdown('<p class="section-title">📱 Mental Health Apps</p>', unsafe_allow_html=True)
    st.markdown("""
    <ul class="resource-list">
        <li><a href="https://www.headspace.com" class="resource-links">Headspace (Meditation & Mindfulness)</a></li>
        <li><a href="https://www.calm.com" class="resource-links">Calm (Sleep & Relaxation)</a></li>
        <li><a href="https://woebothealth.com" class="resource-links">Woebot (AI Chat for Mental Health)</a></li>
    </ul>
    """, unsafe_allow_html=True)

    # Support Communities
    st.markdown('<p class="section-title">🤝 Support Communities & Forums</p>', unsafe_allow_html=True)
    st.markdown("""
    <ul class="resource-list">
        <li><a href="https://www.reddit.com/r/mentalhealth/" class="resource-links">r/MentalHealth on Reddit</a></li>
        <li><a href="https://www.7cups.com" class="resource-links">7 Cups (Free Emotional Support)</a></li>
    </ul>
    """, unsafe_allow_html=True)

    # Emergency Helplines
    st.markdown('<p class="section-title">☎️ Emergency Helplines</p>', unsafe_allow_html=True)
    st.markdown("""
    <ul class="resource-list">
        <li><a href="https://www.crisistextline.org" class="resource-links">Crisis Text Line (Text HOME to 741741)</a></li>
        <li><a href="https://suicidepreventionlifeline.org" class="resource-links">National Suicide Prevention Lifeline</a></li>
        <li><a href="https://www.samaritans.org" class="resource-links">Samaritans (UK Helpline)</a></li>
    </ul>
    """, unsafe_allow_html=True)

    # Centered Button
    if st.button("🔍 Explore More Resources"):
        st.success("Redirecting to additional resources...")

