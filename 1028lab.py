import pandas as pd
import numpy as np

file_path = "AQI_Data.csv"
data = pd.read_csv(file_path)

# Display first 5 rows
print("\nFirst 5 rows:")
print(data.head())


# Display last 6 rows
print("\nLast 6 rows:")
print(data.tail(6))

print("\nSummary :")
print(data.describe())


cities = data["City"].unique()
print("\nMean AQI, PM2.5, and PM10 for each city:")
for city in cities:
    city_data = data[data["City"] == city]
    mean_aqi = np.mean(city_data["AQI"])
    mean_pm25 = np.mean(city_data["PM2.5"])
    mean_pm10 = np.mean(city_data["PM10"])
    print(f"{city}: AQI={mean_aqi:.2f}, PM2.5={mean_pm25:.2f}, PM10={mean_pm10:.2f}")

# Filter rows where PM2.5 > 100
high_pm25 = data[data["PM2.5"] > 100]
print("\nRows where PM2.5 exceeds 100:")
print(high_pm25)

# Count how many such rows exist for each city
city_counts = high_pm25["City"].value_counts()
print("\nCount of rows where PM2.5 > 100 for each city:")
print(city_counts)
