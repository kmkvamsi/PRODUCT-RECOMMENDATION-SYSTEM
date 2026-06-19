import pandas as pd
from sklearn.cluster import KMeans

# Load cleaned data
df = pd.read_csv("dataset/cleaned_retail.csv")

# Customer Features
customer_data = (
    df.groupby("CustomerID")
    .agg({
        "TotalPrice": "sum",
        "InvoiceNo": "nunique"
    })
)

customer_data.columns = [
    "TotalSpent",
    "NumOrders"
]

# KMeans Clustering
kmeans = KMeans(
    n_clusters=3,
    random_state=42,
    n_init=10
)

customer_data["Cluster"] = kmeans.fit_predict(customer_data)

# Calculate average spending per cluster
cluster_avg = (
    customer_data
    .groupby("Cluster")["TotalSpent"]
    .mean()
    .sort_values()
)

# Label clusters
mapping = {}

mapping[cluster_avg.index[0]] = "Low Value"
mapping[cluster_avg.index[1]] = "Regular"
mapping[cluster_avg.index[2]] = "VIP"

customer_data["CustomerType"] = (
    customer_data["Cluster"]
    .map(mapping)
)

print("\nCustomer Segment Summary:\n")

print(
    customer_data.groupby("CustomerType")
    .agg({
        "TotalSpent": "mean",
        "NumOrders": "mean"
    })
)

# Save CSV
customer_data.to_csv(
    "dataset/customer_segments.csv"
)

print("\ncustomer_segments.csv saved successfully!")