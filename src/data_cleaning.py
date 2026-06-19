import pandas as pd

df = pd.read_excel("dataset/Online Retail.xlsx")

print("Original Shape:", df.shape)

print("\nMissing Values:")
print(df.isnull().sum())

# Remove missing values
df = df.dropna()

# Remove duplicates
df = df.drop_duplicates()

# Remove negative quantities
df = df[df["Quantity"] > 0]

# Remove negative prices
df = df[df["UnitPrice"] > 0]

print("\nCleaned Shape:", df.shape)

# Create TotalPrice column
df["TotalPrice"] = df["Quantity"] * df["UnitPrice"]

# Save cleaned dataset
df.to_csv("dataset/cleaned_retail.csv", index=False)

print("\ncleaned_retail.csv created successfully")