import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("API_SP.POP.TOTL_DS2_en_csv_v2_38144.csv", skiprows=4)

print("Dataset Loaded Successfully!")
print(df.head())

population_2020 = df["2020"].dropna()

plt.figure(figsize=(10, 6))
plt.hist(population_2020, bins=20)
plt.title("Population Distribution Across Countries (2020)")
plt.xlabel("Population")
plt.ylabel("Number of Countries")
plt.grid(axis='y', alpha=0.3)
plt.show()

top_countries = df.sort_values("2020", ascending=False).head(10)

plt.figure(figsize=(12, 6))
plt.bar(top_countries["Country Name"], top_countries["2020"])
plt.title("Top 10 Most Populated Countries in 2020")
plt.xlabel("Country")
plt.ylabel("Population")
plt.xticks(rotation=45)
plt.show()

print("Task Completed Successfully!")
