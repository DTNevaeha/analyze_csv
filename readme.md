# Product Analysis
This project analyzes product data from a CSV file and provides insights such as current stock status and restock needs.

Reading CSV Data:
The read_csv function reads the CSV file and loads the product data into a list of dictionaries.
Calculates average prices for all products and lists the most expensive category.
It handles file not found errors and exits gracefully if the file is not found.
It handles missing or malformed data for fields like current_stock


## Setup Instructions
1. In the command prompt ensure that you are in the correct directory as the folder by using the cd *path* command.
2. Once in the correct directory use "python src/analysis.py data/products.csv"


## Approach
TODO


## Requirements
No external API keys or credentials are required for this product. 
Ensure Python is instaled on your system, you can download it from python.org
This can work with any CSV file with the headers:
    product_name,
    our_price,
    category,
    current_stock,
    restock_threshold.


## Issues / Limitations
restock_threshold does not currently do anything. Some information on the original pdf is missing and cut off.
Original PDF instructions included for readability


## Time Spent Estimates
3 hours - Analysis,
1 hour - readme,
10m - System setup,
1 hour - Report Document
In progress - Approach


## TODO
Choose and integrate ONE external data source
 Could be pricing data, market trends, economic indicators, etc.
 Document why you chose this source

Create report document