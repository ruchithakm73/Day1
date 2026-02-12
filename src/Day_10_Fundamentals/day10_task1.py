import pandas as pd

df = pd.read_csv("customer_orders.csv")

print("Shape before cleaning:", df.shape)

print("\nMissing Values Report:")
print(df.isna().sum())

# Fill missing numeric values safely
numeric_cols = df.select_dtypes(include=['number']).columns

for col in numeric_cols:
    df[col] = df[col].fillna(df[col].median())

# Remove duplicates
df = df.drop_duplicates()

print("\nShape after cleaning:", df.shape)
