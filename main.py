#####################Smartphone Website Data Extraction Project##################

import requests
from bs4 import BeautifulSoup
import pandas as pd
from tqdm import tqdm

website_url = "https://anycallmobilemm.com/product-category/smartphone/"

def create_page_urls(main_url):
    """Create web page urls from the website url."""
    web_data = requests.get(main_url).text
    bsObj = BeautifulSoup(web_data, "html.parser")
    # Create web page urls
    # Find Max Page Number
    max_page_num = int(bsObj.find_all("a", "page-numbers")[-2].text)
    page_url_list = []
    for i in range(1, max_page_num+1):
        page_url = main_url + "page/" + str(i)
        page_url_list.append(page_url)
    return page_url_list
web_url_list = create_page_urls(website_url)

def extract_p_info_tags(web_url):
    response = requests.get(web_url)        
    web_data = response.text     
    bsObj =BeautifulSoup(web_data,"html.parser")
    p_info_tags = bsObj.find_all("div", "product-element-bottom") # tag, class name    
    return p_info_tags

def extract_p_name(p_info_tag):
    ## Extract product name tag
    p_name_tag = p_info_tag.find("h3", "wd-entities-title")  # tag, class name
    ## Extract product name text
    p_name = p_name_tag.text
    return p_name

def extract_p_price(p_info_tag):
    ## Extract product price tag 
    p_price_tag = p_info_tag.find("span", "woocommerce-Price-amount amount")  # tag, class name
    ## Extract product price text
    p_price = p_price_tag.text
    ## Transform product price
    p_price = p_price.replace(",", "").replace("\xa0Ks", "") 
    try:
        p_price = int(p_price) # change into float data type            
    except ValueError:
        # Handle the discount prices
        discount_price_list = p_price.split("\n")
        # get last value
        p_price = discount_price_list[-1]
        # remove spaces from the text
        p_price = p_price.strip()
        p_price = int(p_price) # change into float data type
    return p_price

final_df = pd.DataFrame() #Create an empty dataframe

for each_url in tqdm(web_url_list):
    product_info_tags = extract_p_info_tags(each_url)
    
    product_name_list =[]
    product_price_list =[]
    for product_info_tag in product_info_tags:
        product_name = extract_p_name(product_info_tag)
        product_price = extract_p_price(product_info_tag)        
            
        product_name_list.append(product_name)            
        product_price_list.append(product_price)                            
   
    #Create a pandas dataframe
    page_df = pd.DataFrame({"Product Name":product_name_list,"Product Price":product_price_list})
    
    #Export data from all web pages
    final_df = pd.concat([final_df,page_df])

#Export the final data into an Excel file
final_df.to_excel("Final Data.xlsx", index=False)

print("Project is completed successfully!")

    
