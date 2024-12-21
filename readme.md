# Product Analysis
This project analyzes product data from a CSV file and provides insights such as current stock status and restock needs.

Reading CSV Data:
The read_csv function reads the CSV file and loads the product data into a list of dictionaries.
It handles file not found errors and exits gracefully if the file is not found.
It handles missing or malformed data for fields like current_stock


## Setup Instructions
1. In the command prompt ensure that you are in the correct directory as the folder by using the cd *path* command.
2. Once in the correct directory use "python src/analysis.py data/products.csv"

## Requirements
No external API keys or credentials are required for this product. 
