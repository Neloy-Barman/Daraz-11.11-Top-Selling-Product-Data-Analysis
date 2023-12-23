import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By

columns = ['Category', "SubCategory Name", "SubCategory Link"]

subcategory_data = []

def parse_categories(categories) -> list:
    categories = [category.text.split() for category in categories]
    categories = [" ".join(category[1: len(category)]) for category in categories]
    return categories

def parse_subcategories(driver,item_no) -> list:
    
    sub_categories = driver.find_elements(by=By.XPATH, value=f"//ul[@class='lzd-site-menu-sub Level_1_Category_No{item_no}']/li[@class='lzd-site-menu-sub-item']/a")
    sub_categories = [data.get_attribute('href') for data in sub_categories]
    return sub_categories


def main():
    base_url = "https://www.daraz.com.bd/"
    driver = webdriver.Chrome()
    driver.get(base_url)

    # Extracting categories
    categories = driver.find_elements(by=By.XPATH,value= "//div[@class='lzd-site-nav-menu-dropdown']/ul/li/a")
    avaiable_categories =  parse_categories(categories=categories)

    # for i in range(0, len(avaiable_categories)):
    for i in range(0, 1):
    

        # Extracting sub categories
        sub_categories = parse_subcategories(driver=driver, item_no=i+1)

        for l in range(0,len(sub_categories)):

            driver.get(sub_categories[l])
            try: 
                header_text = driver.find_element(by=By.XPATH, value= "//h1[@class='title--Xj2oo']").text
            except:
                header_text = str(None)

            product_details = {}
            product_details['Category'] = avaiable_categories[i]
            product_details['SubCategory Link'] = sub_categories[l]
            product_details['SubCategory Name'] = header_text

            subcategory_data.append(product_details)

        df = pd.DataFrame(columns=columns, data=subcategory_data)
        df.to_csv("./Scraped_data/subcategories.csv", index=False)
        
    driver.close()


if __name__ == '__main__':

    main()