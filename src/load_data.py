import pandas as pd

df = pd.read_excel("dataset/Online Retail.xlsx")

print("Dataset Shape:", df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nFirst 5 Rows:")
print(df.head())