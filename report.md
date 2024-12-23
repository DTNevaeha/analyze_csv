## Summary of Data Cleaning
Handling Missing Data:
    Current Stock: Converted "out of stock" entries to 0. For other entries, attempted to convert to integers and set
    to 0 if conversion failed.

    Restock Threshold: Checked for empty values and set them to None. Attempted to convert non-empty values to integers
    and set to None if conversion failed.

Invalid Data Handling:
    Product Price: Attempted to convert the our_price field to a float. If conversion failed, printed a warning and set
    the price to 0.

Missing Keys:
    Checked for the presence of all required keys (product_name, our_price, category, current_stock, restock_threshold)
    in each product entry. If any key was missing, printed a warning and skipped the product.

Data Type Conversions:
    Ensured that numeric fields (our_price, current_stock, restock_threshold) were correctly converted to their
    respective data types (float or integer).

These steps helped to ensure that the data used for analysis was consistent, complete, and correctly formatted, thereby
improving the reliability of the insights derived from the data.


## Key insights discovered
Average Price per Category:
    Calculated the average price of products in each category. This helps in understanding the pricing distribution
    across different categories.

Most Expensive Category:
    Identified the category with the highest average price. This insight can be useful for strategic pricing and
    marketing decisions.

Product Price Distribution:
    Analyzed the distribution of product prices within each category. This can help in identifying outliers and
    understanding the range of prices offered.

Stock Levels:
    Evaluated the current stock levels of products. This can help in identifying products that are out of stock or need
    restocking.

Restock Thresholds:
    Assessed the restock thresholds for products. This can help in planning inventory management and ensuring that
    popular products are always available.

These insights provide a comprehensive understanding of the product data, helping in making informed business decisions
related to pricing, inventory management, and marketing strategies.

## Visualization
No visualizations have been created at this point.
Although if I were to add a visualization I could create a bar or pie chart that calculates the average prices or stock
of each product and create a chart based on the findings.


## Recommendations based on findings
Strategic Pricing Adjustments:
    Most Expensive Category: Consider reviewing the pricing strategy for the most expensive category. If the high prices
    are justified by high demand or premium quality, maintain the strategy. Otherwise, consider price adjustments to
    stay competitive.

    Average Price per Category: For categories with lower average prices, evaluate if there is room for price increases
    without affecting demand. This can help improve overall revenue.

Inventory Management:
    Stock Levels: Identify products that are frequently out of stock and consider increasing their inventory levels.
    This will help in meeting customer demand and avoiding lost sales.

    Restock Thresholds: Review and adjust restock thresholds to ensure that popular products are always available.
    Implement an automated restocking system to maintain optimal inventory levels.

Data-Driven Decision Making:
    Continuously monitor and analyze product data to identify trends and make informed decisions. Implement data
    visualization tools to track key metrics and gain real-time insights into product performance.

These recommendations aim to optimize pricing strategies, improve inventory management, and ultimately drive better
business outcomes based on the insights derived from the product data analysis.