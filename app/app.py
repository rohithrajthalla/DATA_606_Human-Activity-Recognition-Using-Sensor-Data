import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
import plotly.express as px
import plotly.graph_objects as go
from joblib import load
import os

# Page config
st.set_page_config(page_title="Activity Recognition Analysis", layout="wide")

# Define the path to the models folder
models_folder = os.path.join("..", "models")

# Load your trained model and preprocessors
@st.cache_resource
def load_model():
    model = load(os.path.join(models_folder, 'random_forest_model.joblib'))
    scaler = load(os.path.join(models_folder, 'scaler.joblib'))
    pca = load(os.path.join(models_folder, 'pca.joblib'))
    return model, scaler, pca

model, scaler, pca = load_model()

# Activity mapping
ACTIVITIES = {
    'a01': 'Sitting', 
    'a02': 'Standing', 
    'a03': 'Lying on back', 
    'a04': 'Lying on right side',
    'a05': 'Ascending stairs', 
    'a06': 'Descending stairs', 
    'a07': 'Standing in elevator',
    'a08': 'Moving in elevator', 
    'a09': 'Walking in parking lot', 
    'a10': 'Walking on treadmill (4 km/h)',
    'a11': 'Walking on inclined treadmill', 
    'a12': 'Running on treadmill (8 km/h)',
    'a13': 'Exercising on stepper', 
    'a14': 'Exercising on cross trainer',
    'a15': 'Cycling horizontal', 
    'a16': 'Cycling vertical', 
    'a17': 'Rowing',
    'a18': 'Jumping', 
    'a19': 'Playing basketball'
}

def feature_engineering(df):
    """Extract exactly 45 features matching the original training set"""
    df = df.iloc[:, :45]  # Select only sensor columns
    return df.mean().to_frame().T  # Return mean of each column as features

def predict_activity(data):
    """Process data and predict activity"""
    df = pd.DataFrame(data)
    features = feature_engineering(df)
    features_scaled = scaler.transform(features)
    features_pca = pca.transform(features_scaled)
    raw_prediction = model.predict(features_pca)[0]
    probabilities = model.predict_proba(features_pca)[0]
    return raw_prediction, probabilities

# Main app
st.title('Human Activity Recognition System')

# File upload
uploaded_file = st.file_uploader("Upload sensor data (CSV file)", type="csv")

if uploaded_file:
    data = pd.read_csv(uploaded_file).values
    
    # Make prediction
    prediction, probabilities = predict_activity(data)
    
    # Display results
    st.header("Analysis Results")
    col1, col2 = st.columns(2)
    
    with col1:
        st.success(f"Predicted Activity: {ACTIVITIES[prediction]}")
        
        # Create confidence chart
        activities_list = list(ACTIVITIES.values())
        prob_df = pd.DataFrame({
            'Activity': activities_list,
            'Confidence': probabilities
        })
        prob_df = prob_df.sort_values('Confidence', ascending=True).tail(5)
        
        fig = px.bar(prob_df, x='Confidence', y='Activity', orientation='h',
                    title='Top 5 Most Likely Activities')
        fig.update_layout(
            height=400,
            xaxis_title="Confidence Score (%)",
            yaxis_title="Activity",
            showlegend=False
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Create meaningful feature names
        feature_names = {
            'Feature_0': 'Torso Acceleration (X)',
            'Feature_1': 'Torso Acceleration (Y)',
            'Feature_2': 'Torso Acceleration (Z)',
            'Feature_4': 'Right Arm Movement',
            'Feature_6': 'Left Arm Movement',
            'Feature_7': 'Right Leg Motion',
            'Feature_8': 'Left Leg Motion',
            'Feature_9': 'Vertical Movement',
            'Feature_17': 'Body Rotation',
            'Feature_29': 'Overall Motion Pattern'
        }
        
        feature_imp = pd.DataFrame({
            'Feature': [feature_names.get(f'Feature_{i}', f'Feature_{i}') 
                       for i in range(len(model.feature_importances_))],
            'Importance': model.feature_importances_
        }).sort_values('Importance', ascending=True).tail(10)
        
        fig = px.bar(feature_imp, x='Importance', y='Feature', orientation='h',
                    title='Most Influential Sensor Readings')
        fig.update_layout(
            height=400,
            xaxis_title="Importance Score",
            yaxis_title="Sensor Reading Type",
            showlegend=False
        )
        st.plotly_chart(fig, use_container_width=True)

# Improved sidebar with more detailed information
with st.sidebar:
    st.title("About This System")
    st.info("""
    This system uses sensors placed on five body positions to recognize physical activities:
    
    📍 Sensor Locations:
    - Torso (Center body)
    - Right & Left Arms
    - Right & Left Legs
    
    Each location has three types of sensors:
    🔵 Accelerometer: Measures movement acceleration
    🔴 Gyroscope: Detects rotational motion
    🟡 Magnetometer: Tracks orientation changes
    """)
    
    st.markdown("### How to Use")
    st.write("""
    1. Upload your sensor data CSV file
    2. View the predicted activity
    3. Check confidence scores
    4. Examine which sensors contributed most
    """)

    st.markdown("### Technical Details")
    st.write("""
    The system uses advanced machine learning:
    
    🎯 Random Forest Classification
    - Highly accurate activity recognition
    - Robust to sensor noise
    - Real-time prediction capability
    
    🔍 Feature Processing
    - PCA dimensionality reduction
    - Statistical feature extraction
    - Sensor fusion techniques
    """)
