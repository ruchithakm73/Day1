import pandas as pd

df = pd.read_csv("sales_data.csv")

print("Before Conversion:\n")
print(df.dtypes)

# Clean Price column
df["Price"] = df["Price"].str.replace("$", "", regex=False).astype(float)

# Convert Date column
df["Date"] = pd.to_datetime(df["Date"])

print("\nAfter Conversion:\n")
print(df.dtypes)

print("\nAverage Price:", df["Price"].mean())
print("Latest Date:", df["Date"].max())
