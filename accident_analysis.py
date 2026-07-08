import pandas as pd
import matplotlib.pyplot as plt
import os
import kagglehub

# ============================================
# Download Dataset
# ============================================

path = kagglehub.dataset_download("sobhanmoosavi/us-accidents")

print("Dataset Path:", path)

# Find CSV file
csv_file = None

for file in os.listdir(path):
    if file.endswith(".csv"):
        csv_file = os.path.join(path, file)
        break

print("CSV File:", csv_file)

# ============================================
# Load Dataset
# ============================================

df = pd.read_csv(csv_file, nrows=500000)

print(df.head())
print(df.shape)

# ============================================
# Dataset Information
# ============================================

print(df.info())

print(df.isnull().sum())

# ============================================
# Convert Start_Time to DateTime
# ============================================

df["Start_Time"] = pd.to_datetime(df["Start_Time"])

# Create Hour Column
df["Hour"] = df["Start_Time"].dt.hour

# ============================================
# Accidents by Hour
# ============================================

hourly = df["Hour"].value_counts().sort_index()

plt.figure(figsize=(10,5))
plt.plot(hourly.index, hourly.values, marker="o")
plt.title("Accidents by Hour of Day")
plt.xlabel("Hour")
plt.ylabel("Number of Accidents")
plt.grid(True)
plt.savefig("accidents_by_hour.png")
plt.show()

# ============================================
# Weather Conditions
# ============================================

weather = df["Weather_Condition"].value_counts().head(10)

plt.figure(figsize=(10,6))
plt.bar(weather.index, weather.values)
plt.xticks(rotation=45, ha="right")
plt.title("Top 10 Weather Conditions")
plt.tight_layout()
plt.savefig("weather_conditions.png")
plt.show()

# ============================================
# Road Conditions
# ============================================

road_columns = [
    "Bump",
    "Crossing",
    "Give_Way",
    "Junction",
    "No_Exit",
    "Railway",
    "Roundabout",
    "Station",
    "Stop",
    "Traffic_Calming",
    "Traffic_Signal",
    "Turning_Loop"
]

road_data = df[road_columns].sum().sort_values(ascending=False)

plt.figure(figsize=(10,6))
plt.bar(road_data.index, road_data.values)
plt.xticks(rotation=45)
plt.title("Road Features Near Accidents")
plt.tight_layout()
plt.savefig("road_features.png")
plt.show()

# ============================================
# Severity Distribution
# ============================================

severity = df["Severity"].value_counts().sort_index()

plt.figure(figsize=(6,5))
plt.bar(severity.index.astype(str), severity.values)
plt.title("Accident Severity")
plt.xlabel("Severity")
plt.ylabel("Count")
plt.savefig("severity_distribution.png")
plt.show()

# ============================================
# Accident Hotspots
# ============================================

plt.figure(figsize=(10,8))
plt.scatter(
    df["Start_Lng"],
    df["Start_Lat"],
    s=1,
    alpha=0.3
)

plt.title("Accident Hotspots")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.savefig("accident_hotspots.png")
plt.show()

# ============================================
# Top 10 States
# ============================================

states = df["State"].value_counts().head(10)

plt.figure(figsize=(10,5))
plt.bar(states.index, states.values)
plt.title("Top 10 States with Most Accidents")
plt.xlabel("State")
plt.ylabel("Number of Accidents")
plt.savefig("top_states.png")
plt.show()

# ============================================
# Summary
# ============================================

print("\n========== SUMMARY ==========")
print("Total Records :", len(df))
print("Highest Severity :", df["Severity"].mode()[0])
print("Most Common Weather :", df["Weather_Condition"].mode()[0])
print("Peak Accident Hour :", hourly.idxmax())