# Human Activity Recognition System

## Overview
This project is a machine learning-based system that recognizes human physical activities using sensor data. Built as part of the UMBC Data Science Master's Degree Capstone, it accurately classifies 19 different daily and sports activities using data from body-worn sensors.

## Author
- **Name**: Om Sri Rohith Raj Yadav Thalla
- **Program**: Data Science Master's Degree
- **Institution**: University of Maryland, Baltimore County (UMBC)
- **Supervisor**: Dr. Chaojie (Jay) Wang

## Project Structure
```
HUMAN_ACTIVITY_RECOGNITION/
├── app/                           # Streamlit web application
│   ├── app.py                    # Main application file
│   ├── README.md                 # Application documentation
│   └── requirements.txt          # Application dependencies
├── data/                         # Dataset directory
│   ├── extracted_data/           # Processed sensor data
│   ├── daily+and+sports+activities.data
│   └── README.md                 # Dataset documentation
├── docs/                         # Documentation files
│   └── Report.md                 # Detailed project report
├── models/                       # Saved model files
│   ├── pca.joblib               # PCA transformation model
│   ├── random_forest_model.joblib# Trained classifier
│   └── scaler.joblib            # Feature scaler
├── notebooks/                    # Jupyter notebooks
│   ├── .ipynb_checkpoints/      
│   ├── data/                    # Notebook data files
│   ├── analysis_and_modeling.ipynb
│   └── README.md                # Notebook documentation
├── .gitignore
└── README.md                    # Project overview (this file)
```

## Key Features
- **High Accuracy**: 99% accuracy in recognizing 19 different physical activities
- **Real-time Processing**: Instant activity prediction from sensor data
- **Interactive Web Interface**: Built with Streamlit for easy data upload and visualization
- **Robust Model**: Random Forest Classifier with PCA dimensionality reduction
- **Comprehensive Analysis**: Feature importance visualization and confidence scores

## Technologies Used
- **Python** for data processing and modeling
- **Streamlit** for web application development
- **Scikit-learn** for machine learning
- **Pandas & NumPy** for data manipulation
- **Plotly** for interactive visualizations

## Getting Started

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/rohithrajthalla/DATA_606_Human Activity Recognition Using Sensor Data.git
   ```

2. Install requirements:
   ```bash
   pip install -r app/requirements.txt
   ```

3. Run the application:
   ```bash
   cd app
   streamlit run app.py
   ```

## Dataset
The project uses the UCI Machine Learning Repository's Daily and Sports Activities dataset:
- 19 different physical activities
- 8 subjects (4 female, 4 male)
- 5 body-worn sensors (torso, arms, legs)
- 9 sensor readings per location (accelerometer, gyroscope, magnetometer)
- 25 Hz sampling frequency
- 5-minute duration per activity per subject

## Documentation
- `/docs/Report.md`: Comprehensive project report
- `/app/README.md`: Application usage guide
- `/notebooks/README.md`: Analysis and modeling documentation
- `/data/README.md`: Dataset details and structure

## Results
- 99% classification accuracy
- Robust performance across different subjects
- Effective feature engineering and dimensionality reduction
- No overfitting or class imbalance issues

## Links
- [Dataset Source](https://archive.ics.uci.edu/dataset/256/daily+and+sports+activities)
- [Project Presentation](https://drive.google.com/file/d/1zxEkjt_2Cbftn77DO8ukgKR3mZ716n_Z/view?usp=sharing)
- [Demo Video](link_to_be_added)

## Acknowledgments
- Dr. Chaojie (Jay) Wang for project guidance
- UMBC Data Science Program
- UCI Machine Learning Repository for the dataset