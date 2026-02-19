import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(42)
heights = np.random.normal(loc=170, scale=7, size=1000)
incomes = np.random.exponential(scale=50000, size=1000)
scores = 100 - np.random.exponential(scale=15, size=1000)
df = pd.DataFrame({
    "Heights": heights,
    "Incomes": incomes,
    "Scores": scores
})
plt.figure(figsize=(15, 5))
plt.subplot(1, 3, 1)
sns.histplot(df["Heights"], kde=True)
plt.title("Human Heights (Normal)")
plt.subplot(1, 3, 2)
sns.histplot(df["Incomes"], kde=True)
plt.title("Household Incomes (Right-Skewed)")
plt.subplot(1, 3, 3)
sns.histplot(df["Scores"], kde=True)
plt.title("Easy Exam Scores (Left-Skewed)")

plt.tight_layout()
plt.show()

print("Heights -> Mean:", df["Heights"].mean(), 
      "| Median:", df["Heights"].median())

print("Incomes -> Mean:", df["Incomes"].mean(), 
      "| Median:", df["Incomes"].median())

print("Scores -> Mean:", df["Scores"].mean(), 
      "| Median:", df["Scores"].median())
