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
1. Read guidelines to understand requirements.
2. Data Reading and Loading:
    Implemented the read_csv function to read product data from a CSV file.
    Used Python's csv.DictReader to load the data into a list of dictionaries for easy manipulation.
3. Error Handling:
    Implemented error handling for file not found errors and missing or malformed data.
    Ensured the script exits with appropriate error messages if issues are encountered.
4. Data Cleaning:
    Handled missing data for current_stock by converting "out of stock" entries to 0 and attempting to convert other
    entries to integers.
    Checked for empty values in restock_threshold and set them to None. Attempted to convert non-empty values to
    integers.
    Attempted to convert our_price to a float and printed a warning if conversion failed, setting the price to 0.
5. Data Validation:
    Checked for the presence of all required keys (product_name, our_price, category, current_stock, restock_threshold)
    in each product entry. Printed warnings and skipped products with missing keys.
6. Data Analysis:
    Calculated the average price of products in each category.
    Identified the category with the highest average price.
    Analyzed the distribution of product prices within each category.
7. Insights Generation:
    Generated insights based on the analysis, such as the most expensive category and average prices per category.
    Provided recommendations for strategic pricing and inventory management.


## Requirements
No external API keys or credentials are required for this product. 

Ensure Python is installed on your system, you can download it from python.org
This analyzer work with any CSV file as long as they contain the following headers:
    product_name,
    our_price,
    category,
    current_stock,
    restock_threshold.


## Issues / Limitations
restock_threshold does not currently do anything more than ensure the information is not blank.
Some information on the original pdf is missing and cut off and missing.
Original PDF instructions included for readability


## Time Spent Estimates
3 hours - Analysis,
1 hour - readme,
10m - System setup,
1 hour - Report Document,
30m - Approach


## TODO
Choose and integrate ONE external data source
 Could be pricing data, market trends, economic indicators, etc.
 Document why you chose this source
