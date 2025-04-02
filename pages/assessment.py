import streamlit as st
import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.cluster import KMeans

def show():
    st.markdown("""
        <style>
            .stButton>button:hover {
                color: #1E90FF !important; /* Changes text color to blue */
                border: 2px solid #1E90FF !important; /* Changes border to blue */
            }

            /* Set text color to white */
            h1, h3, h5, ul, li {
                color: white !important;
            }
        </style>
    """, unsafe_allow_html=True)
    st.title("📝 Mental Health Assessment")
    
    @st.cache_data
    def load_data():
        df = pd.read_csv('pages/main.csv')
        if 'User_ID' in df.columns:
            df = df.drop(columns=['User_ID'])
        return df

    # Load the data
    df = load_data()

    # Preprocess the data
    label_encoders = {}
    category_mappings = {}  # Store mappings for UI display
    categorical_cols = df.select_dtypes(include=['object']).columns.tolist()
    if 'Mental_Health_Condition' in categorical_cols:
        categorical_cols.remove('Mental_Health_Condition')  # Exclude from encoding

    for col in categorical_cols:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col])
        label_encoders[col] = le
        category_mappings[col] = dict(zip(le.classes_, le.transform(le.classes_)))  # Save mapping

    scaler = StandardScaler()
    df_scaled = scaler.fit_transform(df.drop(columns=['Mental_Health_Condition'], errors='ignore'))

    # Apply K-Means clustering
    k = 4  # Number of clusters
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    df['Cluster'] = kmeans.fit_predict(df_scaled)

    # Define cluster names
    cluster_names = {
        0: "Low-Stress Healthy Group",
        1: "Balanced Lifestyle with Moderate Stress",
        2: "High-Stress Workaholic Lifestyle",
        3: "Unhealthy Lifestyle with Extreme Stress"
    }
    df['Cluster_Name'] = df['Cluster'].map(cluster_names)

    # Streamlit App
    st.markdown('<h2 class="title">📚 Mental Health Prediction App</h2>', unsafe_allow_html=True)
    st.write("Enter details to predict mental health group.")

    # User input fields
    def user_input():
        age = st.number_input("Age", min_value=10, max_value=100, value=25)

        gender = st.selectbox("Gender", list(category_mappings['Gender'].keys()))
        occupation = st.selectbox("Occupation", list(category_mappings['Occupation'].keys()))
        country = st.selectbox("Country", list(category_mappings['Country'].keys()))
        severity = st.selectbox("Severity of your Mental condition", list(category_mappings['Severity'].keys()))
        consultation_history = st.selectbox("Consultation History regarding Mental Health", list(category_mappings['Consultation_History'].keys()))
        stress_level = st.selectbox("Stress Level", list(category_mappings['Stress_Level'].keys()))
        diet_quality = st.selectbox("Diet Quality", list(category_mappings['Diet_Quality'].keys()))
        smoking_habit = st.selectbox("Smoking Habit", list(category_mappings['Smoking_Habit'].keys()))
        alcohol_consumption = st.selectbox("Alcohol Consumption", list(category_mappings['Alcohol_Consumption'].keys()))
        medication_usage = st.selectbox("Medication Usage", list(category_mappings['Medication_Usage'].keys()))

        sleep_hours = st.number_input("Sleep Hours (per day)", min_value=0.0, max_value=18.0, value=7.0)
        work_hours = st.number_input("Work Hours (per week)", min_value=0, max_value=70, value=40)
        physical_activity = st.number_input("Physical Activity Hours (per week)", min_value=0, max_value=35, value=5)
        social_media = st.number_input("Social Media Usage (per day)", min_value=0, max_value=40, value=3)

        # Convert selected values into encoded values before using them in the model
        data = pd.DataFrame([[
            age, 
            category_mappings['Gender'][gender], 
            category_mappings['Occupation'][occupation], 
            category_mappings['Country'][country], 
            category_mappings['Severity'][severity], 
            category_mappings['Consultation_History'][consultation_history], 
            category_mappings['Stress_Level'][stress_level], 
            sleep_hours, 
            work_hours, 
            physical_activity, 
            social_media, 
            category_mappings['Diet_Quality'][diet_quality], 
            category_mappings['Smoking_Habit'][smoking_habit], 
            category_mappings['Alcohol_Consumption'][alcohol_consumption], 
            category_mappings['Medication_Usage'][medication_usage]
        ]], 
        columns=['Age', 'Gender', 'Occupation', 'Country', 'Severity', 'Consultation_History', 
                 'Stress_Level', 'Sleep_Hours', 'Work_Hours', 'Physical_Activity_Hours', 
                 'Social_Media_Usage', 'Diet_Quality', 'Smoking_Habit', 'Alcohol_Consumption', 
                 'Medication_Usage'])

        return data

    user_data = user_input()

    if st.button("Predict Mental Health Group"):
        user_data_scaled = scaler.transform(user_data)
        
        # Predict the cluster
        predicted_cluster = kmeans.predict(user_data_scaled)[0]
        predicted_group = cluster_names[predicted_cluster]
        
        st.subheader("Prediction")
        st.write(f"Predicted Mental Health Group: *{predicted_group}*")
