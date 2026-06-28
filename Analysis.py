import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

os.makedirs("outputs", exist_ok=True)

df = pd.read_csv("data/regional_climate_data.csv")

print(df.head())
print(df.describe())

sns.set_theme(style="whitegrid")

# Temperature Trend
plt.figure(figsize=(8,5))
sns.lineplot(data=df, x="Year", y="AvgTemp", marker="o", color="red")
plt.title("Temperature Trend (2000–2021)")
plt.savefig("outputs/temp_trend.png")
plt.show()

# Rainfall Trend
plt.figure(figsize=(8,5))
sns.barplot(data=df, x="Year", y="Rainfall", color="skyblue")
plt.xticks(rotation=90)
plt.title("Rainfall Variation")
plt.savefig("outputs/rainfall_trend.png")
plt.show()

# Humidity Trend
plt.figure(figsize=(8,5))
sns.lineplot(data=df, x="Year", y="Humidity", marker="o", color="green")
plt.title("Humidity Trend")
plt.savefig("outputs/humidity_trend.png")
plt.show()

# Correlation
plt.figure(figsize=(5,4))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Matrix")
plt.savefig("outputs/correlation.png")
plt.show()

print("Analysis Completed Successfully")
