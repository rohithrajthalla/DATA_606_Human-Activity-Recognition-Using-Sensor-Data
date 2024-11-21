# Dataset Information

## Overview
This repository contains a comprehensive dataset of daily and sports activities, captured through wearable sensors. The dataset includes recordings from 19 different activities performed by 8 subjects, with data collected at 25 Hz sampling frequency over 5-minute durations.

## Dataset Specifications
- **Source**: UCI Machine Learning Repository
- **URL**: [Daily and Sports Activities Dataset](https://archive.ics.uci.edu/dataset/256/daily+and+sports+activities)
- **Data Size**: Multiple text files organized hierarchically
- **Time Period**: 5-minute duration per activity per subject
- **Sampling Rate**: 25 Hz
- **Segment Duration**: 5 seconds
- **Total Segments**: 9,120 (19 activities × 8 subjects × 60 segments)
- **Records per Segment**: 125 rows (5 seconds × 25 Hz)
- **Total Samples**: 1,140,000 (9,120 × 125)

## Directory Structure
```
data/
├── extracted_data/
│   └── data/
│       ├── a01/  # Activity 1 (Sitting)
│       │   ├── p1/  # Person 1
│       │   │   ├── s01.txt  # Segment 1
│       │   │   └── ...      # Through s60.txt
│       │   └── ...          # Through p8/
│       └── ...              # Through a19/
├── daily+and+sports+activities.data  # Raw dataset
└── README.md                # This file
```

## Data Collection Details

### Subjects
- 8 subjects (4 female, 4 male)
- Age range: 20-30 years
- Activities performed in subjects' own style without restrictions

### Recording Environment
- Bilkent University Sports Hall
- Electrical and Electronics Engineering Building
- Flat outdoor area on campus

## Activities List

1. A01: Sitting
2. A02: Standing
3. A03: Lying on back
4. A04: Lying on right side
5. A05: Ascending stairs
6. A06: Descending stairs
7. A07: Standing in elevator still
8. A08: Moving around in elevator
9. A09: Walking in parking lot
10. A10: Walking on treadmill (4 km/h, flat)
11. A11: Walking on treadmill (4 km/h, 15° inclined)
12. A12: Running on treadmill (8 km/h)
13. A13: Exercising on stepper
14. A14: Exercising on cross trainer
15. A15: Cycling on exercise bike (horizontal)
16. A16: Cycling on exercise bike (vertical)
17. A17: Rowing
18. A18: Jumping
19. A19: Playing basketball

## Sensor Configuration

### Sensor Units Location
1. T: Torso
2. RA: Right Arm
3. LA: Left Arm
4. RL: Right Leg
5. LL: Left Leg

### Sensors per Unit
Each unit contains 9 sensors:
- 3-axis accelerometer (x, y, z)
- 3-axis gyroscope (x, y, z)
- 3-axis magnetometer (x, y, z)

## File Format

### Data Files
- Format: Text files (.txt)
- Rows: 125 (5 seconds × 25 Hz)
- Columns: 45 (5 units × 9 sensors)
- Values: Comma-separated

### Column Organization (45 total columns)
1. Columns 1-9: Torso sensors
2. Columns 10-18: Right Arm sensors
3. Columns 19-27: Left Arm sensors
4. Columns 28-36: Right Leg sensors
5. Columns 37-45: Left Leg sensors

For each unit, the 9 columns represent:
```
[x_acc, y_acc, z_acc, x_gyro, y_gyro, z_gyro, x_mag, y_mag, z_mag]
```


## How to Get the Data

1. Download the dataset from [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/256/daily+and+sports+activities)
2. Download the zip file and store it in the data folder
3. Place the downloaded file `daily+and+sports+activities.data` in this directory
4. The `extracted_data` folder will be generated automatically when running the data processing scripts in the notebooks directory


## Usage Notes
- Each activity segment is independent
- Inter-subject variations exist in speeds and amplitudes
- Data is raw and unprocessed
- Missing or corrupted data should be handled appropriately before use
- Data has been verified for quality with no missing values
- Each activity has consistent representation in the dataset
- Time series data is sampled at 25 Hz

## Note
These data files are not tracked in Git due to their size. Please follow the instructions above to set up your local data directory.
