# Human Activity Recognition System

## 1. Title and Author

- **Project Title**: Human Activity Recognition System
- **Prepared for**: UMBC Data Science Master Degree Capstone by Dr Chaojie (Jay) Wang
- **Author**: Om Sri Rohith Raj Yadav Thalla
- **GitHub Repository**: [rohithrajthalla](https://github.com/rohithrajthalla)
- **LinkedIn Profile**: [rohithrajthalla](https://www.linkedin.com/in/rohithrajthalla/)
- **PowerPoint Presentation**: [Project Presentation](https://drive.google.com/file/d/1zxEkjt_2Cbftn77DO8ukgKR3mZ716n_Z/view?usp=sharing)
- **YouTube Video**: [Youtube Video](https://youtu.be/8m1YLKTKQSQ)

## 2. Background

### What is it about?
This project focuses on developing a Human Activity Recognition (HAR) system that can automatically identify and classify different physical activities performed by individuals using sensor data. The system utilizes data collected from multiple body-worn sensors to predict various daily and sports activities.

### Why does it matter?
Human Activity Recognition has significant applications in:
- Healthcare monitoring and rehabilitation
- Sports performance analysis
- Elderly care and fall detection
- Personal fitness tracking
- Smart home automation
- Medical research and diagnosis

### Research Questions
1. How accurately can we identify different physical activities using sensor data from body-worn devices?
2. Which sensor locations and measurements are most crucial for activity recognition?
3. Can we develop a robust model that works effectively across different subjects despite variations in how they perform activities?

## 3. Data

### Data Source
- Dataset: Daily and Sports Activities Dataset
- Source: UCI Machine Learning Repository
- URL: https://archive.ics.uci.edu/dataset/256/daily+and+sports+activities

### Data Specifications
- **Data Size**: Multiple text files organized hierarchically
- **Data Shape**: 
  - 19 activities × 8 subjects × 60 segments = 9,120 total segments
  - Each segment: 125 rows × 45 columns
  - Total samples: 1,140,000 (9,120 × 125)
- **Time Period**: 5-minute duration per activity per subject
- **Sampling Rate**: 25 Hz

### Row Representation
Each row represents a single time point (1/25 second) of sensor measurements across all body locations.

### Data Dictionary
#### Sensor Units (5 locations):
1. T: Torso
2. RA: Right Arm
3. LA: Left Arm
4. RL: Right Leg
5. LL: Left Leg

#### Sensors per Unit:
Each unit contains 9 sensors:
1. Accelerometer (x, y, z)
2. Gyroscope (x, y, z)
3. Magnetometer (x, y, z)

#### Column Structure (45 total columns):
1. Columns 1-9: Torso sensors
2. Columns 10-18: Right Arm sensors
3. Columns 19-27: Left Arm sensors
4. Columns 28-36: Right Leg sensors
5. Columns 37-45: Left Leg sensors

## 4. Exploratory Data Analysis (EDA)

### Data Processing and Integration
- Implemented a comprehensive data loading function to combine data across:
  - 19 different activities
  - 8 subjects
  - 60 segments per activity-subject combination
- Created a unified dataset with additional columns for activity and subject identification
- Verified data quality: no missing values found
- Identified and analyzed duplicate patterns in the data

### Data Distribution Analysis

#### Activity Distribution
- Conducted analysis of sample distribution across all 19 activities
- Created visualization using Plotly Express to show the distribution
- Found balanced representation across activities, indicating a well-structured dataset
- Each activity has consistent representation in the dataset

### Time Series Analysis
Key findings from temporal analysis:
1. **Stationary Activities**
   - Sitting (A01) and Standing (A02) show consistent, flat patterns
   - Minimal sensor reading variations

2. **Dynamic Activities**
   - Ascending stairs (A05) and Jumping (A18) display significant variations
   - Clear periodic patterns in sensor readings

3. **High-Intensity Activities**
   - Running (A12) and Basketball (A19) show distinctive high-amplitude fluctuations
   - Unique patterns helpful for activity differentiation

## 5. Model Training

### Data Preprocessing
1. **Data Splitting**
   - Training set: 80% of data
   - Testing set: 20% of data
   - Random state: 42 for reproducibility

2. **Feature Scaling**
   - Applied StandardScaler to normalize sensor readings
   - Mean = 0, standard deviation = 1

### Feature Engineering
1. **Magnitude Calculations**
   - Computed magnitude for each sensor type per body part:
   - $$\text{Magnitude} = \sqrt{x^2 + y^2 + z^2}$$

2. **Statistical Features**
   - Rolling window calculations for each sensor:
     - Mean
     - Standard deviation
     - Variance
   - Window size: 5 time steps

### Dimensionality Reduction
- **Principal Component Analysis (PCA)**
  - Retained 95% of variance
  - Significantly reduced feature dimensionality
  - Applied after standardization

### Model Selection and Training
Selected **Random Forest Classifier** for the following reasons:
1. **Advantages**:
   - Efficient handling of high-dimensional data
   - Built-in feature importance ranking
   - Robust against overfitting
   - Excellent for multi-class classification

2. **Model Configuration**:
   - Number of estimators: 100
   - Random state: 42 for reproducibility

### Model Performance
1. **Overall Metrics**:
   - Accuracy: 99%
   - Strong macro and weighted averages across classes

2. **Cross-validation Results**:
   - Consistent performance across folds
   - No signs of overfitting
   - Robust model behavior across different data splits

## 6. Application Development

### Web Application Overview
The system is implemented as a user-friendly web application using Streamlit, providing an intuitive interface for users to upload sensor data and receive real-time activity predictions.

### Key Components
1. **User Interface**
   - Clean, modern interface
   - Drag-and-drop file upload
   - Real-time analysis display

2. **Analysis Features**
   - Primary activity prediction
   - Top 5 most likely activities
   - Sensor importance visualization
   - Confidence scores

3. **Technical Implementation**
   - Integrated trained models
   - Real-time data processing
   - Interactive visualizations

## 7. Conclusion

### Project Achievements
1. **Model Performance**
   - Achieved 99% accuracy in activity recognition
   - Robust performance across different subjects and activities
   - Successfully handled variations in activity execution

2. **Validation Results**
   - Cross-validation confirmed model stability
   - Learning curves showed optimal model complexity
   - No evidence of overfitting or class imbalance
   - Consistent performance across different data splits

3. **Technical Innovation**
   - Successfully implemented complex feature engineering
   - Effective dimensionality reduction while maintaining performance
   - Created an intuitive, user-friendly interface

### Key Findings
1. **Sensor Importance**
   - Identified most crucial sensor locations and types
   - Demonstrated effectiveness of multi-sensor approach
   - Validated sensor placement strategy

2. **Activity Recognition**
   - High accuracy across diverse activities
   - Robust performance in distinguishing similar activities
   - Effective handling of dynamic movements

### Future Improvements
1. **Model Enhancement**
   - Explore deep learning approaches
   - Investigate real-time processing optimization
   - Consider additional feature engineering techniques

2. **Application Development**
   - Implement mobile device integration
   - Add real-time monitoring capabilities
   - Expand visualization options

3. **Data Collection**
   - Include more subjects for broader diversity
   - Add more complex activities
   - Consider environmental variations

### Impact and Applications
The system demonstrates significant potential for:
- Healthcare monitoring
- Sports performance analysis
- Rehabilitation tracking
- Elderly care systems
- Personal fitness applications

## 8. References

1. UCI Machine Learning Repository: Daily and Sports Activities Dataset
2. Scikit-learn Documentation for Random Forest Classifier
3. Streamlit Documentation for Web Application Development