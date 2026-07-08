# 🚗 US Traffic Accident Analysis

## 📌 Project Overview

This project analyzes the **US Accidents Dataset** to identify patterns related to **weather conditions, road features, accident severity, and time of day**. The analysis helps uncover accident hotspots and the major factors contributing to traffic accidents through data visualization.

This project was completed as part of my **Data Science Internship – Task 04**.

---

## 🎯 Objective

The objective of this project is to:

- Analyze traffic accident data.
- Identify accident hotspots.
- Study accident patterns by time of day.
- Analyze weather conditions during accidents.
- Examine road features associated with accidents.
- Visualize important trends using Python.

---

# 📂 Dataset

**Dataset:** US Accidents Dataset

**Source:** Kaggle

Downloaded using:

```python
import kagglehub

path = kagglehub.dataset_download("sobhanmoosavi/us-accidents")
```

The dataset contains millions of accident records across the United States, including:

- Accident Severity
- Weather Conditions
- Road Features
- Date & Time
- State Information
- Latitude & Longitude

---

# 🛠 Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- KaggleHub

---

# 📚 Project Workflow

### 1. Download Dataset

- Download dataset using KaggleHub.

### 2. Load Dataset

- Read CSV file using Pandas.

### 3. Data Cleaning

- Handle missing values
- Convert date and time columns
- Prepare data for analysis

### 4. Exploratory Data Analysis (EDA)

The following analyses were performed:

- Accident Severity Distribution
- Accidents by Hour
- Weather Conditions
- Road Features
- Top States with Most Accidents
- Accident Hotspots

---

# 📊 Generated Visualizations

The project generates the following visualizations:

- ✅ Accident Hotspots
- ✅ Accidents by Hour
- ✅ Weather Conditions
- ✅ Road Features
- ✅ Severity Distribution
- ✅ Top States with Most Accidents

---

# 📁 Project Structure

```
SCT_SC_04/
│
├── accident_analysis.py
├── README.md
├── requirements.txt
│
├── accident_hotspots.png
├── accidents_by_hour.png
├── road_features.png
├── severity_distribution.png
├── top_states.png
└── weather_conditions.png
```

---

# ▶️ Installation

Clone the repository

```bash
git clone https://github.com/sunilvk2008-dev/SCT_SC_04.git
```

Move into the project folder

```bash
cd SCT_SC_04
```

Install required libraries

```bash
pip install pandas numpy matplotlib seaborn kagglehub
```

---

# ▶️ Run the Project

```bash
python accident_analysis.py
```

---

# 📈 Results

The analysis identifies:

- Peak accident hours during the day.
- Weather conditions associated with accidents.
- Road features frequently involved in accidents.
- States with the highest number of accidents.
- Geographic accident hotspots across the United States.

---

# 💡 Key Insights

- Most accidents occur during peak traffic hours.
- Fair weather records the highest number of accidents due to higher traffic volume.
- Traffic signals and junctions are common accident locations.
- Certain states consistently report more accidents than others.
- Accident hotspots are concentrated around major urban areas.

---

# 📌 Skills Demonstrated

- Data Cleaning
- Exploratory Data Analysis (EDA)
- Data Visualization
- Time-based Analysis
- Geographic Data Analysis
- Statistical Analysis
- Python Programming
- Git & GitHub

---

# 🚀 Future Improvements

- Add Monthly Trend Analysis
- Add Weekly Accident Analysis
- Build Interactive Dashboard using Streamlit
- Create Interactive Accident Maps using Folium
- Predict Accident Severity using Machine Learning

---

# 👨‍💻 Author

**Sunil Kumar**

B.Tech Artificial Intelligence & Machine Learning Student

GitHub:
https://github.com/sunilvk2008-dev

---

# 🙏 Acknowledgements

- Kaggle – US Accidents Dataset
- Pandas Documentation
- Matplotlib Documentation
- Seaborn Documentation
- KaggleHub

---

⭐ If you found this project useful, consider giving it a star!
