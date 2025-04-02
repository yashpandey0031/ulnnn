import streamlit as st
import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.cluster import KMeans
def show():
    st.title("📝 Mental Health Assessment")
    
    @st.cache_data
    def load_data():
        df = pd.read_csv('pages\main.csv')
        if 'User_ID' in df.columns:
            df = df.drop(columns=['User_ID'])
        return df

    # Load the data
    df = load_data()

    # Preprocess the data
    label_encoders = {}
    categorical_cols = df.select_dtypes(include=['object']).columns.tolist()
    if 'Mental_Health_Condition' in categorical_cols:
        categorical_cols.remove('Mental_Health_Condition')  # Exclude from encoding

    for col in categorical_cols:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col])
        label_encoders[col] = le

    scaler = StandardScaler()
    df_scaled = scaler.fit_transform(df.drop(columns=['Mental_Health_Condition'], errors='ignore'))

    # Apply K-Means clustering
    k = 4  # Number of clusters
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    df['Cluster'] = kmeans.fit_predict(df_scaled)

    # Define cluster names
    cluster_names = {
        0: "Low-Stress Healthy Group",
        1: "High-Stress Unhealthy Lifestyle",
        2: "Balanced Lifestyle with Moderate Stress",
        3: "Workaholic with High Stress"
    }
    df['Cluster_Name'] = df['Cluster'].map(cluster_names)

    # Streamlit App
    st.title("Mental Health Prediction App")
    st.write("Enter details to predict mental health group.")

    # User input fields
    def user_input():
        age = st.number_input("Age", min_value=10, max_value=100, value=30)
        gender = st.selectbox("Gender", df['Gender'].unique())
        occupation = st.selectbox("Occupation", df['Occupation'].unique())
        country = st.selectbox("Country", df['Country'].unique())
        severity = st.selectbox("Severity", df['Severity'].unique())
        consultation_history = st.selectbox("Consultation History", df['Consultation_History'].unique())
        stress_level = st.selectbox("Stress Level", df['Stress_Level'].unique())
        sleep_hours = st.number_input("Sleep Hours", min_value=0.0, max_value=24.0, value=7.0)
        work_hours = st.number_input("Work Hours", min_value=0, max_value=100, value=40)
        physical_activity = st.number_input("Physical Activity Hours", min_value=0, max_value=24, value=5)
        social_media = st.number_input("Social Media Usage (Hours)", min_value=0, max_value=24, value=3)
        diet_quality = st.selectbox("Diet Quality", df['Diet_Quality'].unique())
        smoking_habit = st.selectbox("Smoking Habit", df['Smoking_Habit'].unique())
        alcohol_consumption = st.selectbox("Alcohol Consumption", df['Alcohol_Consumption'].unique())
        medication_usage = st.selectbox("Medication Usage", df['Medication_Usage'].unique())
        
        data = pd.DataFrame([[age, gender, occupation, country, severity, consultation_history, stress_level, sleep_hours, 
                            work_hours, physical_activity, social_media, diet_quality, smoking_habit, 
                            alcohol_consumption, medication_usage]],
                            columns=['Age', 'Gender', 'Occupation', 'Country', 'Severity', 'Consultation_History', 
                                    'Stress_Level', 'Sleep_Hours', 'Work_Hours', 'Physical_Activity_Hours', 
                                    'Social_Media_Usage', 'Diet_Quality', 'Smoking_Habit', 'Alcohol_Consumption', 
                                    'Medication_Usage'])
        
        for col in categorical_cols:
            if col in data.columns and col in label_encoders:
                try:
                    data[col] = label_encoders[col].transform(data[col])
                except ValueError:
                    data[col] = 0  # Assign unknown labels to a default category
        
        return data

    user_data = user_input()

    if st.button("Predict Mental Health Group"):
        user_data_scaled = scaler.transform(user_data)
        
        # Predict the cluster
        predicted_cluster = kmeans.predict(user_data_scaled)[0]
        predicted_group = cluster_names[predicted_cluster]
        
        st.subheader("Prediction")
        st.write(f"Predicted Mental Health Group: *{predicted_group}*")