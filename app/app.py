import streamlit as st
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# --------------------------------
# PAGE CONFIG
# --------------------------------

st.set_page_config(
    page_title="SmartCart AI",
    page_icon="🛒",
    layout="wide"
)

# --------------------------------
# LOAD DATA
# --------------------------------

@st.cache_data
def load_data():
    return pd.read_csv("dataset/cleaned_retail.csv")


@st.cache_data
def load_model():

    df = load_data()

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

    return similarity_df


df = load_data()
similarity_df = load_model()

# --------------------------------
# HEADER
# --------------------------------

st.title("🛒 SmartCart AI")
st.caption("AI-Powered Product Recommendation & Customer Analytics Platform")

# --------------------------------
# KPI CARDS
# --------------------------------

total_revenue = round(df["TotalPrice"].sum(), 2)
total_customers = df["CustomerID"].nunique()
total_products = df["Description"].nunique()

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "💰 Revenue",
        f"${total_revenue:,.0f}"
    )

with col2:
    st.metric(
        "👥 Customers",
        total_customers
    )

with col3:
    st.metric(
        "📦 Products",
        total_products
    )

st.divider()

# --------------------------------
# RECOMMENDATION SYSTEM
# --------------------------------

st.header("🤖 AI Product Recommendations")

product = st.selectbox(
    "🔍 Search Product",
    similarity_df.index
)

if st.button("Recommend"):

    recommendations = (
        similarity_df[product]
        .sort_values(ascending=False)
        .iloc[1:6]
    )

    st.subheader("Recommended Products")

    for item in recommendations.index:
        st.success(item)

st.divider()

# --------------------------------
# BUSINESS ANALYTICS
# --------------------------------

st.header("📊 Business Analytics")

top_products = (
    df.groupby("Description")["Quantity"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

st.subheader("Top 10 Selling Products")

st.bar_chart(top_products)

# --------------------------------
# TOP COUNTRIES
# --------------------------------

top_countries = (
    df.groupby("Country")["TotalPrice"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

st.subheader("Top 10 Countries by Revenue")

st.bar_chart(top_countries)

st.divider()

# --------------------------------
# CUSTOMER SEGMENTS
# --------------------------------

st.header("👥 Customer Segments")

try:

    segments = pd.read_csv(
        "dataset/customer_segments.csv"
    )

    if "CustomerType" in segments.columns:

        segment_counts = (
            segments["CustomerType"]
            .value_counts()
        )

        st.subheader("Customer Distribution")

        st.bar_chart(segment_counts)

    else:

        segment_counts = (
            segments["Cluster"]
            .value_counts()
        )

        st.subheader("Customer Distribution")

        st.bar_chart(segment_counts)

    st.dataframe(
        segments.head(10),
        use_container_width=True
    )

except:
    st.warning(
        "Run customer_segmentation.py first."
    )

st.divider()

# --------------------------------
# TOP CUSTOMERS
# --------------------------------

st.header("🏆 Top Customers")

top_customers = (
    df.groupby("CustomerID")["TotalPrice"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

top_customers = top_customers.reset_index()

top_customers.columns = [
    "Customer ID",
    "Total Spending"
]

st.dataframe(
    top_customers,
    use_container_width=True
)

# --------------------------------
# FOOTER
# --------------------------------

st.markdown("---")

st.markdown(
    """
    ### 🚀 SmartCart AI
    
    Features:
    - Product Recommendation Engine
    - Customer Segmentation (K-Means)
    - Business Analytics Dashboard
    - Customer Insights
    - Retail Sales Analysis
    
    Built using:
    - Python
    - Pandas
    - Scikit-Learn
    - Streamlit
    """
)