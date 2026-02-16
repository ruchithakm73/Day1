import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("housing.csv")
df = df.dropna()

plt.figure(figsize=(12,5))

plt.subplot(1,2,1)
sns.scatterplot(x="Area_sqft", y="Price", data=df)
plt.title("Scatter Plot: Area vs Price")
plt.xlabel("Square Footage (Area_sqft)")
plt.ylabel("Price")

plt.subplot(1,2,2)
sns.boxplot(x="City", y="Price", data=df)
plt.title("Boxplot: City vs Price")
plt.xlabel("City")
plt.ylabel("Price")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

correlation = df["Area_sqft"].corr(df["Price"])
print("Correlation between Area and Price:", correlation)