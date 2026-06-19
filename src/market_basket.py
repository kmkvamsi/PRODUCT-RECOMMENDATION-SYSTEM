import pandas as pd
from itertools import combinations
from collections import Counter

df = pd.read_csv("dataset/cleaned_retail.csv")

basket = (
    df.groupby("InvoiceNo")["Description"]
    .apply(list)
)

pair_counter = Counter()

for products in basket:

    unique_products = list(set(products))

    for pair in combinations(unique_products, 2):
        pair_counter[pair] += 1


def customers_also_bought(product_name, top_n=5):

    recommendations = Counter()

    for (p1, p2), count in pair_counter.items():

        if p1 == product_name:
            recommendations[p2] += count

        elif p2 == product_name:
            recommendations[p1] += count

    return recommendations.most_common(top_n)


if __name__ == "__main__":

    product = "WHITE METAL LANTERN"

    print("\nCustomers Also Bought:\n")

    for item, score in customers_also_bought(product):
        print(item, "->", score)