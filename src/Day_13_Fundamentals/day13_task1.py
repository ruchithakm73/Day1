import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("housing_data.csv")

plt.figure(figsize=(12,5))

plt.subplot(1, 2, 1)
sns.histplot(df["Price"], kde=True)
plt.title("Price Distribution")
plt.xlabel("Price")
plt.ylabel("Frequency")

plt.subplot(1, 2, 2)
sns.countplot(x=df["City"])
plt.title("City Distribution")
plt.xlabel("City")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()
print("Skewness:", df["Price"].skew())
print("Kurtosis:", df["Price"].kurt())