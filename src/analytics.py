import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dataset/cleaned_retail.csv")

top_products = (
    df.groupby("Description")["Quantity"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(12,6))
top_products.plot(kind="bar")
plt.title("Top 10 Selling Products")
plt.tight_layout()
plt.show()