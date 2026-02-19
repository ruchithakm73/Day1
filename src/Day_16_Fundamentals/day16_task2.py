import pandas as pd
import numpy as np

np.random.seed(42)
data = pd.DataFrame({
    "score": np.random.normal(loc=70, scale=10, size=1000)
})

data.loc[1001] = 150
data.loc[1002] = 5

mu = data["score"].mean()
sigma = data["score"].std()

print("Mean (μ):", mu)
print("Standard Deviation (σ):", sigma)

data["z_score"] = (data["score"] - mu) / sigma

outliers = data[np.abs(data["z_score"]) > 3]

print("\nStatistical Outliers (|Z| > 3):")
print(outliers)
