import csv
import sys

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

    # Iterate through products and print analysis
    for product in products:
        product_name = product['product_name']
        our_price = product['our_price']
        category = product['category']
        current_stock = product['current_stock']
        restock_threshold = product['restock_threshold']

        # Handle missing data
        if current_stock.lower() == 'out of stock':
            current_stock = 0
        else:
            try:
                current_stock = int(current_stock)
            except ValueError:
                current_stock = 0

        if restock_threshold == '':
            restock_threshold = None
        else:
            try:
                restock_threshold = int(restock_threshold)
            except ValueError:
                restock_threshold = None

        # Print information about the product/sub category
        print(f"Product: {product_name}")
        print(f"  Price: ${our_price}")
        print(f"  Category: {category}")
        print(f"  Current Stock: {current_stock}")
        if restock_threshold is not None:
            print(f"  Restock Threshold: {restock_threshold}")
        
        # Determine if restocking is needed
        if current_stock <= 0:
            print(f"  Status: OUT OF STOCK")
        elif restock_threshold and current_stock <= restock_threshold:
            print(f"  Status: Needs Restock")

def main():
    if len(sys.argv) < 2:
        print("Usage: python src/analysis.py <path_to_csv_file>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    products = read_csv(file_path)
    analyze_products(products)

if __name__ == "__main__":
    main()