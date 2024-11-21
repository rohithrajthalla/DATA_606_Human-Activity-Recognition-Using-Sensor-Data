# Analysis Notebooks

## Overview
This directory contains Jupyter notebooks used for data analysis, preprocessing, and model development for the Human Activity Recognition project. These notebooks document the step-by-step process of building and evaluating our machine learning models.

## Main Notebooks

### `analysis_and_modeling.ipynb`
Primary notebook containing the complete analysis pipeline:
- Data loading and preprocessing
- Exploratory Data Analysis (EDA)
- Feature engineering
- Model development and evaluation
- Results visualization

## Usage Instructions

1. **Environment Setup**
   - Ensure you have Python 3.8+ installed
   - Install required packages:
     ```bash
     pip install -r ../app/requirements.txt
     ```
   - Launch Jupyter Notebook:
     ```bash
     jupyter notebook
     ```

2. **Data Preparation**
   - Make sure you have downloaded the dataset following instructions in `/data/README.md`
   - The notebooks expect the data to be in the correct structure under the `/data` directory

3. **Execution Order**
   - Start with `analysis_and_modeling.ipynb`
   - Run cells sequentially to ensure proper execution
   - Some cells may take several minutes to execute, especially during model training

## Key Features

### Data Preprocessing
- Loading raw sensor data
- Handling missing values
- Signal processing and filtering
- Feature extraction
- Data normalization

### Exploratory Data Analysis
- Sensor data visualization
- Statistical analysis
- Feature correlation analysis
- Activity distribution analysis

### Model Development
- Feature selection
- Model training and validation
- Hyperparameter tuning
- Performance evaluation
- Cross-validation

### Visualization
- Activity patterns
- Sensor data plots
- Model performance metrics
- Confusion matrices

## Output Files
The notebooks generate several output files that are saved in the project structure:
- Trained models → `/models/`
- Preprocessed data → `/data/extracted_data/`
- Scalers and transformers → `/models/`

## Dependencies
Key libraries used in the notebooks:
- pandas
- numpy
- scikit-learn
- matplotlib
- seaborn
- joblib


## Contributing
When contributing to the notebooks:
- Add clear markdown documentation
- Include comments in complex code sections
- Update requirements.txt if new dependencies are added
- Test all cells before committing

## Issues
If you encounter any issues:
1. Ensure all dependencies are correctly installed
2. Check that the data is properly downloaded and structured
3. Verify that all previous cells have been executed in order
4. Refer to the main project README for additional troubleshooting

For any questions or issues, please open an issue in the main repository.