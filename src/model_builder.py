import pandas as pd
import joblib
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv("dataset/cleaned_retail.csv")

matrix = pd.pivot_table(
    df,
    index="CustomerID",
    columns="Description",
    values="Quantity",
    fill_value=0
)

similarity = cosine_similarity(matrix.T)

similarity_df = pd.DataFrame(
    similarity,
    index=matrix.columns,
    columns=matrix.columns
)

joblib.dump(
    similarity_df,
    "models/product_similarity.pkl"
)

print("Model Saved!")