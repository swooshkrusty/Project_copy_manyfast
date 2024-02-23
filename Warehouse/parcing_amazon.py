from amazon.api import AmazonAPI

amazon = AmazonAPI(
    "AKIA4YKSACLLQX7DS5QH", "KKF2YrnW9t6yC3XfU2FkSnilKo4pwAmUGxhfAin+", AMAZON_ASSOC_TAG
)
products = amazon.search(Keywords="kindle", SearchIndex="All")

for i, product in enumerate(products):
    print(f"{i+1}. {product.title}")
