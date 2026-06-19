import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv("dataset/cleaned_retail.csv")

customer_product_matrix = pd.pivot_table(
    df,
    index="CustomerID",
    columns="Description",
    values="Quantity",
    fill_value=0
)

product_similarity = cosine_similarity(
    customer_product_matrix.T
)

similarity_df = pd.DataFrame(
    product_similarity,
    index=customer_product_matrix.columns,
    columns=customer_product_matrix.columns
)

def recommend(product_name, top_n=5):

    similar_products = (
        similarity_df[product_name]
        .sort_values(ascending=False)
        .iloc[1:top_n+1]
    )

    return similar_products

while True:

    product = input("\nEnter Product Name: ")

    if product.lower() == "exit":
        break

    try:
        print("\nRecommended Products:\n")
        print(recommend(product))
    except:
        print("Product not found")