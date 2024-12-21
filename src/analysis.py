import csv
import sys
from collections import defaultdict

def read_csv(file_path):
    products = []
    try:
        with open(file_path, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                products.append(row)
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        sys.exit(1)
    return products

def analyze_products(products):
    category_prices = defaultdict(list)

    # Iterate through products and print analysis
    for product in products:
        product_name = product["product_name"]
        our_price = product["our_price"]
        category = product["category"]
        current_stock = product["current_stock"]
        restock_threshold = product["restock_threshold"]

        # Handle missing data
        if current_stock.lower() == "out of stock":
            current_stock = 0
        else:
            try:
                current_stock = int(current_stock)
            except ValueError:
                current_stock = 0

        if restock_threshold == "":
            restock_threshold = None
        else:
            try:
                restock_threshold = int(restock_threshold)
            except ValueError:
                restock_threshold = None

        # Convert price to float
        try:
            our_price = float(our_price)
        except ValueError:
            print(f"Warning: Invalid price '{our_price}' for product '{product_name}'. Setting price to 0.")
            our_price = 0

        # Collect prices by category
        category_prices[category].append(our_price)

        # Print information about the product/sub category
        print(f"Product: {product_name}")
        print(f"  Price: {our_price:.2f} USD")
        print(f"  Category: {category}")
        print(f"  Current Stock: {current_stock}")

    # Calculate average price per category and find the most expensive category
    avg_category_prices = {category: sum(prices) / len(prices) for category, prices in category_prices.items()}
    most_expensive_category = max(avg_category_prices, key=avg_category_prices.get)

    print("\nCategory Price Analysis:")
    for category, avg_price in avg_category_prices.items():
        print(f"  Category: {category}, Average Price: {avg_price:.2f} USD")
    print(f"\nThe most expensive category is '{most_expensive_category}' with an average price of {avg_category_prices[most_expensive_category]:.2f} USD")

# Example usage
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python analysis.py <path_to_csv_file>")
        sys.exit(1)

    file_path = sys.argv[1]
    products = read_csv(file_path)
    analyze_products(products)