# imports
import json
import matplotlib.pyplot as plt
import pandas as pd

class GenerateReport:

    def __init__(self):
        return

    def invoke(self):
        self.generate_sales_report()
    
    def generate_sales_report():
       # Markdown content for the report
        report_md = """
        # Skyline Report

        ## 1. Quick Summary
        This report aggregates data from different sources to generate a real-time summary for incoming threats warning from military-grade vehicles.

        ## 2. Asset Overviews
        ### 2.1. Data Sources
        The sales data is sourced from the company's internal database, which includes transaction records, customer information, and product details.

        ### 2.2. Data Description
        The dataset comprises the following columns:
        - **Transaction ID**: Unique identifier for each transaction
        - **Date**: Date of the transaction
        - **Product ID**: Unique identifier for each product
        - **Product Category**: Category to which the product belongs
        - **Quantity**: Number of units sold
        - **Price**: Price per unit
        - **Total Sales**: Total sales value (Quantity x Price)
        - **Region**: Geographical region of the sale

        ## 3. Sales Performance Analysis
        ### 3.1. Overall Sales Trends
        #### 3.1.1. Monthly Sales
        ![Monthly Sales in Q1 2024](monthly_sales.png)
        
        #### 3.1.2. Sales by Product Category
        ![Sales by Product Category in Q1 2024](sales_by_category.png)

        ### 3.2. Top-Performing Products
        ![Top-Performing Products](top_products.png)

        ## 4. Regional Sales Analysis
        ### 4.1. Sales by Region
        ![Sales by Region in Q1 2024](sales_by_region.png)

        ## 5. Conclusion
        The analysis highlights that the Electronics category is the top performer in sales, with significant contributions from the North and East regions. It is recommended to focus marketing efforts on these regions and product categories to further boost sales in the upcoming quarters.
        """
        
        # Display Markdown content (for console or saving to a file)
        print(report_md)
        
        # Generate plots and save them
        months = ['January', 'February', 'March']
        sales = [25000, 30000, 28000]

        plt.figure(figsize=(10, 5))
        plt.bar(months, sales, color='skyblue')
        plt.xlabel('Month')
        plt.ylabel('Total Sales ($)')
        plt.title('Monthly Sales in Q1 2024')
        plt.savefig('monthly_sales.png')
        plt.close()
        
        categories = ['Electronics', 'Clothing', 'Home & Kitchen', 'Books']
        sales_by_category = [50000, 35000, 40000, 15000]

        plt.figure(figsize=(8, 8))
        plt.pie(sales_by_category, labels=categories, autopct='%1.1f%%', startangle=140)
        plt.title('Sales by Product Category in Q1 2024')
        plt.savefig('sales_by_category.png')
        plt.close()
        
        # Display top-performing products table
        data = {
            'Product ID': [101, 102, 103, 104, 105],
            'Product Name': ['Laptop', 'Smartphone', 'Tablet', 'Headphones', 'Smartwatch'],
            'Total Sales ($)': [15000, 14000, 13000, 12000, 11000]
        }
        df = pd.DataFrame(data)
        print("Top-Performing Products:")
        print(df.sort_values(by='Total Sales ($)', ascending=False).to_string(index=False))
        
        # Plot Sales by Region
        regions = ['North', 'South', 'East', 'West']
        sales_by_region = [40000, 30000, 35000, 25000]

        plt.figure(figsize=(10, 5))
        plt.bar(regions, sales_by_region, color='lightgreen')
        plt.xlabel('Region')
        plt.ylabel('Total Sales ($)')
        plt.title('Sales by Region in Q1 2024')
        plt.savefig('sales_by_region.png')
        plt.close()