# Import Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Dataset
df = pd.read_csv("air_quality_2024.csv")

# Overview of the Data
print(df.head())
print(df.info())

# Analyze Air Quality by Country
country_avg = df.groupby("Country")["PM2.5"].mean().sort_values()
print(country_avg)

# Visualize Top 10 Countries with Best Air Quality
country_avg.head(10).plot(kind='bar', title="Top 10 Countries with Best Air Quality")
plt.ylabel("Average PM2.5 Levels")
plt.show()

# Visualize Seasonal Trends
df['Month'] = pd.to_datetime(df['Date']).dt.month
monthly_avg = df.groupby("Month")["PM2.5"].mean()
sns.lineplot(x=monthly_avg.index, y=monthly_avg.values, marker="o")
plt.title("Monthly Average Air Quality in 2024")
plt.xlabel("Month")
plt.ylabel("PM2.5 Levels")
plt.show()