# Human Activity Recognition System

This Human Activity Recognition System is a machine learning-based app built using Streamlit. It predicts various physical activities based on sensor data collected from body-worn sensors. The application uses a trained Random Forest model, PCA for dimensionality reduction, and Standard Scaler for feature scaling.

## Features
- **Predicts Physical Activities**: Upload sensor data in CSV format, and the app will predict the activity performed.
- **Confidence Scores**: Shows top 5 most likely activities with confidence levels.
- **Feature Importance Visualization**: Highlights the most influential sensor readings contributing to the prediction.

## Project Structure
- **app.py**: Main application file to run the Streamlit app.
- **models/**: Directory containing saved model artifacts (`random_forest_model.joblib`, `scaler.joblib`, `pca.joblib`).
- **README.md**: Documentation of the application.
- **requirements.txt**: List of required packages.

## Getting Started

### Prerequisites
Ensure you have Python installed. Then, install the required packages from `requirements.txt`.

### Installation
1. Clone the repository or download the files.
2. Navigate to the project directory.
3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the application:

    ```bash
    streamlit run app.py
    ```

5. Open the provided URL (usually `http://localhost:8501`) to access the app.

### Usage
1. **Upload Sensor Data**: Upload a CSV file with sensor data. The file should contain 45 sensor readings per sample.
2. **View Prediction**: The predicted activity will be displayed, along with a bar chart showing the top 5 most likely activities.
3. **Examine Feature Importance**: A bar chart displays the most influential sensor readings for the prediction.

## Activity Mapping
The app recognizes the following activities:

- Sitting
- Standing
- Lying on back
- Lying on right side
- Ascending stairs
- Descending stairs
- Standing in elevator
- Moving in elevator
- Walking in parking lot
- Walking on treadmill (4 km/h)
- Walking on inclined treadmill
- Running on treadmill (8 km/h)
- Exercising on stepper
- Exercising on cross trainer
- Cycling horizontal
- Cycling vertical
- Rowing
- Jumping
- Playing basketball

## Technical Details
- **Model**: Random Forest Classifier
- **Feature Processing**: Standard Scaler, PCA for dimensionality reduction
- **Frontend**: Streamlit with interactive visualizations using Plotly
