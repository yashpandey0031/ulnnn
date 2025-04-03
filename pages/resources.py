import streamlit as st 

def show():
        # Custom CSS Styling
    st.markdown("""
        <style>
            .title {
                text-align: center;
                color: white;
                font-size: 50px;
                font-weight: bold;
                margin-top: 20px;
            }
            .section-title {
                font-size: 32px;
                margin-top: 40px;
                font-weight: bold;
            }
            .resource-box {
                background: white;  /* Changed from #FFFFFF to white */
                padding: 20px;
                border-radius: 20px;
                margin: 20px auto;  /* Center content within a fixed width */
                width: 80%;  /* Ensuring it doesn’t take the full page */
                color: black; /* Changed from white to black for readability */
            }
            .resource-list {
                font-size: 20px;
                padding-left: 20px;
            }
            .section-unhealthy {
                background: #880000; /*  Maroon */
                padding: 20px;
                border-radius: 20px;
                margin: 20px 0;
                color: white;
                box-shadow: 5px 5px 15px rgba(0,0,0,0.3);
            }
            .section-highstress {
                background: #FF4500; /* Orange Red */
                padding: 20px;
                border-radius: 20px;
                margin: 20px 0;
                color: white;
                box-shadow: 5px 5px 15px rgba(0,0,0,0.3);
            }
            .section-balanced {
                background: #f7a239; /* Amber */
                padding: 20px;
                border-radius: 20px;
                margin: 20px 0;
                color: white;
                box-shadow: 5px 5px 15px rgba(0,0,0,0.3);
            }
            .section-healthy {
                background: #228B22; /* Forest Green */
                padding: 20px;
                border-radius: 20px;
                margin: 20px 0;
                color: white;
                box-shadow: 5px 5px 15px rgba(0,0,0,0.3);
            }
            .resource-links a {
                color: #FFD700;
                text-decoration: none;
                font-size: 20px;
                font-weight: bold;
            }
            .resource-links a:hover {
                color: #FFA500;
                text-decoration: underline;
            }
            .stButton>button {
                display: block;
                margin: 20px auto;
                background-color: #FFD700;
                color: black;
                border-radius: 10px;
                font-size: 20px;
                padding: 14px 28px;
                font-weight: bold;
            }
            .stButton>button:hover {
                background-color: #FFA500;
            }
                
        </style>
    """, unsafe_allow_html=True)

    # Title
    st.markdown('<h1 class="title">📚 Mental Health Resources</h1>', unsafe_allow_html=True)

    stress_levels = {
        "Unhealthy Lifestyle with Extreme Stress": {
            "Helplines": [
                "<a href='http://healthcollective.in/suicide-prevention-helplines/' target='_blank'>Suicide Prevention / Mental Health Helplines</a>",
                "<a href='https://findahelpline.com/' target='_blank'>Find A Helpline</a>",
                "<a href='https://www.drishtiias.com/daily-news-analysis/kiran-mental-health-rehabilitation-helpline' target='_blank'>Kiran Mental Health Rehabilitation Helpline</a>",
                "<a href='https://telemanas.mohfw.gov.in/home' target='_blank'>National Tele Mental Health Programme of India</a>"
            ],
            "Support Communities": [
                "<a href='https://www.thelivelovelaughfoundation.org/find-help/helplines' target='_blank'>The Live Love Laugh Foundation for Free Helpline and Counselling</a>",
                "<a href='https://www.7cups.com/' target='_blank'>7 Cups (Free Emotional Support)</a>",
                "<a href='https://www.reddit.com/r/mentalhealth/' target='_blank'>r/MentalHealth on Reddit</a>",
                "<a href='https://www.vandrevalafoundation.com/' target='_blank'>Vandrevala Foundation For Counselling</a>"
            ],
            "Additional Resources": [
                "<a href='https://www.who.int' target='_blank'>World Health Organization (WHO)</a>",
                "<a href='https://www.sangath.in/' target='_blank'>Sangath</a>",
                "<a href='https://icallhelpline.org/' target='_blank'>iCall Tata Service Helpline</a>"
            ]
        },
        "High-Stress Workaholic Lifestyle": {
            "Books": [
                "The Mindful Way Through Depression - Mark Williams",
                "Burnout: The Secret to Unlocking the Stress Cycle - Emily Nagoski & Amelia Nagoski",
                "The Joy of Missing Out: Live More by Doing Less - Tanya Dalton",
                "The Things You Can See Only When You Slow Down - Haemin Sunim"
            ],
            "Articles & Research Papers": [
                "<a href='https://www.mentalhealth.org.uk/explore-mental-health/publications/how-manage-and-reduce-stress' target='_blank'>How to Manage and Reduce Stress</a>",
                "<a href='https://pmc.ncbi.nlm.nih.gov/articles/PMC4117275/' target='_blank'>Workaholism: An Overview and Current Status of the Research</a>",
                "<a href='https://hbr.org/2024/09/a-workaholics-guide-to-reclaiming-your-life' target='_blank'>A Workaholic’s Guide to Reclaiming Your Life</a>"
            ],
            "Helplines": [
                "SAMHSA (US Government Mental Health) - 1-800-662-HELP (4357)",
                "Vandrevala Foundation Helpline (India) - 1860 266 2345",
                "iCall - Tata Institute of Social Sciences (India) - +91 9152987821"
            ]
        },
        "Balanced Lifestyle with Moderate Stress": {
            "Books": [
                "Atomic Habits - James Clear",
                "The Little Book of Hygge - Meik Wiking",
                "Feeling Good: The New Mood Therapy - David D. Burns",
                "Lost Connections - Johann Hari"
            ],
            "Courses": [
                "Mindfulness-Based Stress Reduction (MBSR) Course",
                "The Science of Stress Management - Udemy",
                "The Creative Toolkit: 6 Techniques to Spark Original Ideas - Skillshare"
            ],
            "Apps": [
                "Woebot (AI Chat for Mental Health)",
                "Forest (Gamified Approach for Focused Work)",
                "MyFitnessPal (Mindful Nutrition Tracking)"
            ]
        },
        "Low-Stress Healthy Group": {
            "Books": [
                "The Happiness Trap - Russ Harris",
                "Atomic Habits - James Clear",
                "The Upward Spiral - Alex Korb",
                "The Blue Zones: 9 Lessons for Living Longer - Dan Buettner"
            ],
            "Courses": [
                "The Science of Well-Being - Yale (Free)",
                "Positive Psychology - UPenn"
            ],
            "Apps": [
                "Headspace (Meditation & Mindfulness)",
                "Calm (Sleep & Relaxation)"
            ]
        }
    }

    for level, categories in stress_levels.items():
        section_class = "section-healthy"  # Default
        if "Unhealthy" in level:
            section_class = "section-unhealthy"
        elif "High-Stress" in level:
            section_class = "section-highstress"
        elif "Balanced" in level:
            section_class = "section-balanced"

        st.markdown(f'<div class="{section_class}">', unsafe_allow_html=True)  # FIXED
        st.markdown(f'<h2 class="section-title">{level}</h2>', unsafe_allow_html=True)
        
        for category, resources in categories.items():
            st.markdown(f'<h3>{category}</h3>', unsafe_allow_html=True)
            st.markdown("<ul class='resource-list'>", unsafe_allow_html=True)
            for resource in resources:
                st.markdown(f'<li>{resource}</li>', unsafe_allow_html=True)
            st.markdown("</ul>", unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)  # Close div properly
