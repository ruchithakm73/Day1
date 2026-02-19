import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
np.random.seed(42)

population = np.random.exponential(scale=50000, size=100000)
plt.figure(figsize=(12,5))
plt.subplot(1,2,1)
sns.histplot(population, kde=True)
plt.title("Original Population (Right-Skewed)")
plt.xlabel("Income")

sample_means = []

for _ in range(1000):
    sample = np.random.choice(population, size=30)
    sample_means.append(np.mean(sample))

sample_means = np.array(sample_means)
plt.subplot(1,2,2)
sns.histplot(sample_means, kde=True)
plt.title("Distribution of Sample Means (n=30)")
plt.xlabel("Sample Mean")

plt.tight_layout()
plt.show()

print("Population Mean:", np.mean(population))
print("Mean of Sample Means:", np.mean(sample_means))
print("Population Std Dev:", np.std(population))
print("Std Dev of Sample Means:", np.std(sample_means))
