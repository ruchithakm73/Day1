import pandas as pd

df = pd.read_csv("locations.csv")

print("Before Cleaning:")
print(df["Location"].unique())

# Normalize text
df["Location"] = df["Location"].str.strip().str.title()

print("\nAfter Cleaning:")
print(df["Location"].unique())
