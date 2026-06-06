Smartphone Website Data Extraction Project

#Final Capstone Project

##Overview

This project is a Python-based web scraper that automatically extracts smartphone names and pricing data from the *Anycall Mobile* e-commerce website and exports the collected data into an Excel file.The script handles multi-page pagination, cleans up inconsistent currency formatting (including handling discounted prices),and exports the finalized dataset into an organized Excel spreadsheet for further analysis.

##Features

Automatically detects the total number of pages in the smartphone category.
Scrapes product names from each page.
Extracts product prices and converts them into numerical format.
Handles discounted products.
Compiles data across all pages into a unified Pandas DataFrame and exports it directly to an Excel file (`Final Data.xlsx`).
Uses `tqdm` to show a real-time progress bar in the terminal while scraping.

##Required Python Libraries

requests : For sending HTTP requests and retrieving HTML contents.
beautifulsoup4 : For parsing HTML and navigating the DOM tree to extract targeted web elements.
pandas : For structuring data, handling data frames, and exporting data to Excel.
tqdm : For displaying an interactive progress bar during loops.
openpyxl :To write files into the Excel (.xlsx) format.

##Code Architecture

The script is broken down into modular functions for clean maintenance and high readability:
* `create_page_urls(main_url)`: Scans the target directory, fetches the final page index, and generates an iterable list of page URLs.
* `extract_p_info_tags(web_url)`: Requests the raw HTML data of an individual page and returns a list of target product containers (`div.product-element-bottom`).
* `extract_p_name(p_info_tag)`: Isolates and extracts the product title text from the element container.
* `extract_p_price(p_info_tag)`: Extracts, cleans, and converts raw currency strings into structural database floats.  

##How It Works

Step 1: Generate Page URLs
The program first determines the maximum page number available in the smartphone category and automatically generates URLs for all pages.
Example:
https://anycallmobilemm.com/product-category/smartphone/page/1
https://anycallmobilemm.com/product-category/smartphone/page/2
https://anycallmobilemm.com/product-category/smartphone/page/3

Step 2: Extract Product Information
For each page, the scraper extracts:
Product Name
Product Price

Step 3: Data Cleaning
The extracted prices are cleaned by:
Removing commas
Removing currency symbols
Converting values into numeric format
Handling discounted products

Step 4: Export Results
All scraped data is combined into a Pandas DataFrame and exported to:Final Data.xlsx.

⚠️ Disclaimer
This script is designed purely for educational and data analysis purposes. Ensure you comply with the website's terms of service and robots.txt guidelines before running high-frequency requests.







