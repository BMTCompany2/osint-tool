# imports
import json
import matplotlib.pyplot as plt
import pandas as pd
from langchain.text_splitter import RecursiveCharacterTextSplitter


class GenerateReport:

    def __init__(self):
        return

    def invoke(self,data):
        #Split data into chunks
        splits = self._split_documents(data)

        # generate report
        self.generate_sales_report(splits)
    

    def _split_documents(self,docs):
        # Split documents into chunks.
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size = 1500,
            chunk_overlap = 150
        )

        splits = text_splitter.split_documents(docs)
        return splits
    
    def generate_sales_report(self,data):
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
        