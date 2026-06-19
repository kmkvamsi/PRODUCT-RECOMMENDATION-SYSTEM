import pandas as pd

df = pd.read_csv("dataset/cleaned_retail.csv")

# Top 10 products
top_products = (
    df.groupby("Description")["Quantity"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\nTOP 10 PRODUCTS\n")
print(top_products)

# Top 10 countries
top_countries = (
    df.groupby("Country")["TotalPrice"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\nTOP 10 COUNTRIES BY REVENUE\n")
print(top_countries)