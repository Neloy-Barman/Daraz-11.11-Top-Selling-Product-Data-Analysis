import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By

columns = ['Category', "SubCategory", "Title", 'Original Price', 'Discount Price', "Discount", "Seller Name", "Number of Ratings", "Positive Seller Ratings", "Ship On Time", "Chat Response Rate", "Delivery Type", "Cash On Delivery", "Flagship Store"]

product_data = []

def parse_categories(categories) -> list:
    categories = [category.text.split() for category in categories]
    categories = [" ".join(category[1: len(category)]) for category in categories]
    return categories

def parse_subcategories(driver,item_no) -> list:
    
    sub_categories = driver.find_elements(by=By.XPATH, value=f"//ul[@class='lzd-site-menu-sub Level_1_Category_No{item_no}']/li[@class='lzd-site-menu-sub-item']/a")
    sub_categories = [data.get_attribute('href') for data in sub_categories]

    return sub_categories

def parse_lastpage(pagination) -> int:
     pagination = [list_element.get_attribute('title') for list_element in pagination]
     return  int(pagination[len(pagination)-2]) 

def scrape_product_data(category, sub_category, element):
    product_details = {}
    product_link = element.get_attribute('href')
    print(product_link)
    driver = webdriver.Chrome()
    driver.get(product_link)
    details = driver.find_elements(by=By.XPATH, value="//div[@id='container']/div[@id='root']/div[@id='block-Nh2N0D4pN7']/div[@id='block-u9PRYrhKq6']/div[@id='block-9NXWCpo7bI']/div")
    
    try:
        title = details[0].find_element(by=By.XPATH, value="./div[@id='module_product_title_1']/div/div").text
    except:
        try:
            title = driver.find_element(by=By.XPATH, value="//div[@id='module_product_title_1']/div/div").text
        except:
            title = str(None)
    try: 
        prices = details[0].find_element(by=By.XPATH, value="./div[@id='module_product_price_1']/div[@class='pdp-mod-product-price']/div[@class='pdp-product-price']")
    except:
        try:
            prices = driver.find_element(by=By.XPATH, value="//div[@id='module_product_price_1']/div[@class='pdp-mod-product-price']/div[@class='pdp-product-price']")
        except:
            pass
    try:
        discounted_price = prices.find_element(by=By.XPATH, value="./span").text.replace("৳","").replace(",","").strip()
    except:
        discounted_price = 0
    try:
        origin_block = prices.find_elements(by=By.XPATH, value="./div[@class='origin-block']/span")
    except:
        pass
    try:
        original_price = origin_block[0].text.replace("৳","").replace(",","").strip()
        discount = origin_block[1].text.replace("-","").replace("%","").strip()
    except:
        original_price = discounted_price
        discount = 0
    
    try:
        seller_info = details[1].find_element(by=By.XPATH, value="./div[@id='module_seller_info']/div[@class='seller-container']")
    except:
        seller_info = driver.find_element(by=By.XPATH, value="//div[@id='module_seller_info']/div[@class='seller-container']")
    try: 
        seller_name = seller_info.find_element(by=By.XPATH, value="./div[@class='seller-name-retail']/div[@class='seller-name__wrapper']/div[@class='seller-name__detail']/a").text
    except:
        seller_name = seller_info.find_element(by=By.XPATH, value="./div[@class='seller-name']/div[@class='seller-name__wrapper']/div[@class='seller-name__detail']/a").text

    try:
        flagship_element = seller_info.find_elements(by=By.XPATH, value="./div[@class='seller-name-retail']/div[@class='seller-name__wrapper']/div[@class='seller-name__detail']/a")
    except:
        flagship_element = seller_info.find_elements(by=By.XPATH, value="./div[@class='seller-name']/div[@class='seller-name__wrapper']/div[@class='seller-name__detail']/a")

    if len(flagship_element) > 1:
        flagship_store_or_not = "Yes"
    else:
        flagship_store_or_not = "No"

    rating_info = seller_info.find_elements(by=By.XPATH, value="./div[@class='pdp-seller-info-pc']/div[@class='info-content']")

    try:
        delivery_type = driver.find_element(by=By.XPATH, value="//div[@class='delivery-option-item__info']/div[@class='delivery-option-item__title']/span[@style='font-weight: 600;']").text.strip()
        try:
            if delivery_type != "Standard Delivery" or delivery_type != "Free Delivery":
                delivery_type = driver.find_elements(by=By.XPATH, value="//div[@class='delivery-option-item__info']/div[@class='delivery-option-item__title']/span[@style='font-weight: 600;']")[0].text.strip()
        except:
            delivery_type = "Standard Delivery"    
    except:
        delivery_type = "Standard Delivery"

    # Number of Ratings
    try:
        number_of_ratings = int(driver.find_elements(by=By.XPATH, value="//a[@class='pdp-link pdp-link_size_s pdp-link_theme_blue pdp-review-summary__link']")[0].text.split()[0])
    except:
        number_of_ratings = 0

    # Positive Seller Ratings
    try:
        positive_seller_ratings = int(rating_info[0].find_element(by=By.XPATH, value="./div[@class='seller-info-value rating-positive ']").text.replace("%", ""))
    except:
        positive_seller_ratings = 0 # New Seller


    # Cash On Delivery
    try:
        cash_on_delivery = driver.find_elements(by=By.XPATH, value="//div[@class='delivery-option-item__title']/span[@style='font-weight: 400;']")[0].text
        if cash_on_delivery != "Cash on Delivery Available":
            try:
                cash_on_delivery = driver.find_elements(by=By.XPATH, value="//div[@class='delivery-option-item__title']/span[@style='font-weight: 400;']")[1].text
            except:
                cash_on_delivery = "Not Available"
    except:
        cash_on_delivery = "Not Available"

    # Chat Response Rate
    try:
        chat_response_rate = int(rating_info[2].find_element(by=By.XPATH, value="./div[@class='seller-info-value ']").text.replace("%", ""))
    except:
        chat_response_rate = 0 # Not Enough Data

    # Ship On Time
    try:
        ship_on_time = int(rating_info[1].find_element(by=By.XPATH, value="./div[@class='seller-info-value ']").text.replace("%", ""))
    except:
        ship_on_time = 0

    product_details['Category'] = category
    product_details['SubCategory'] = sub_category
    product_details['Title'] = title
    product_details['Discount Price'] = discounted_price
    product_details['Original Price'] = original_price
    product_details['Discount'] = discount
    product_details['Seller Name'] = seller_name
    product_details['Positive Seller Ratings'] = positive_seller_ratings
    product_details['Ship On Time'] = ship_on_time
    product_details['Chat Response Rate'] = chat_response_rate
    product_details["Delivery Type"] = delivery_type
    product_details["Cash On Delivery"] = cash_on_delivery
    product_details["Number of Ratings"] = number_of_ratings
    product_details["Flagship Store"] = flagship_store_or_not

    print(product_details)

    return product_details

    
def main():
    base_url = "https://www.daraz.com.bd/"
    driver = webdriver.Chrome()
    driver.get(base_url)

    # Extracting categories
    categories = driver.find_elements(by=By.XPATH,value= "//div[@class='lzd-site-nav-menu-dropdown']/ul/li/a")
    avaiable_categories =  parse_categories(categories=categories)


    # For all categories
    for i in range(0,len(avaiable_categories)):
    
    # Mannually change i value here according to sub-categories index [0-11]
    # for i in range(0,1):

        # Extracting sub categories
        sub_categories = parse_subcategories(driver=driver, item_no=i+1)


        # For all categories
        for l in range(0, len(sub_categories)):
        
        # Mannually change subcategories value according to need 
        # for l in range(0, last_value+1):

            driver.get(sub_categories[l])
            pagination = driver.find_elements(by=By.XPATH, value="//div[@class='box--eTFFd']/div/div/ul/li")
            
            # Extracting last page
            last_page = parse_lastpage(pagination=pagination)
            print(f"Last page: {last_page}")
            
            if last_page >3:
                z = 3+1
            else:
                z = last_page+1

            for j in range(1, z):

                if "?" in sub_categories[l]:
                    base_url = sub_categories[l]+f"&page={j}&sort=order&from=filter"
                else:
                    base_url = sub_categories[l]+f"?page={j}&sort=order&from=filter"

                driver.get(base_url)

                total_elements = driver.find_elements(by=By.XPATH, value="//div[@class='box--ujueT']/div[@class='gridItem--Yd0sa']/div/div/div[@class='info--ifj7U']/div[@class='title--wFj93']/a")

                print(f"This is the category: {avaiable_categories[i]} >>>>>>>>>>> SubCategory: {sub_categories[l]}")
                print("======================================================================================")
                
                '''
                    The above 2 lines are to show where the scraper is scraping at.
                '''

                for k in  range(0,len(total_elements)):
                    product_data.append(scrape_product_data(category=avaiable_categories[i], sub_category = sub_categories[l],  element=total_elements[k]))
    
                    df = pd.DataFrame(columns=columns, data=product_data)
                    df.to_csv("file_name.csv", index=False)

                    '''
                        Change the 'file_name.csv' with own file_name. 
                    '''

                    '''
                        For Category -> 1 ; index -> 0 ; File Name: "./Scraped_data/women_&_girls_fashion.csv"
                        For Category -> 2 ; index -> 1 ; File Name: "./Scraped_data/health_&_beauty.csv"
                        For Category -> 3 ; index -> 2 ; File Name: "./Scraped_data/watches_bags_jewellery.csv"
                        For Category -> 4 ; index -> 3 ; File Name: "./Scraped_data/mens_&_boys_fashion.csv"
                        For Category -> 5 ; index -> 4 ; File Name: "./Scraped_data/mother_&_baby.csv"
                        For Category -> 6 ; index -> 5 ; File Name: "./Scraped_data/electronic_devices.csv"
                        For Category -> 7 ; index -> 6 ; File Name: "./Scraped_data/tv_&_home_appliances.csv"
                        For Category -> 8 ; index -> 7 ; File Name: "./Scraped_data/electronic_accessories.csv"
                        For Category -> 9 ; index -> 8 ; File Name: "./Scraped_data/groceries.csv"
                        For Category -> 10; index -> 9 ; File Name: "./Scraped_data/home_&_lifestyle.csv"
                        For Category -> 11 ; index -> 10 ; File Name: "./Scraped_data/sports_&_fitness.csv"
                        For Category -> 12 ; index -> 11 ; File Name: "./Scraped_data/automotive_&_motorbike.csv"
                    '''
                    

                    '''
                        For all categories -> File Name: "./Scraped_data/top_selling_product_data.csv"
                    '''


                    '''
                        Other than that you can also use and save in own different names.
                    '''


                    '''
                    Some points to keep in mind: - 
                        1. I collected the data individual catagory wise and put them in seperate .csv file.
                           It takes too long to scrape the webpage and fetch data. So, it was better in my perspective.
                           For this I had to set the looping value mannualy.
                        2. After running for a long time, there may raise some errors. But if that's restarted, then it gets solved.
                        3. There are some pages, that may be exceptional. But this scraper is meant to be used for the general cases.
                        4. This scraper is time-consuming. It will take a long to scrape sub-categorical 3 pages top-selling data.
                           So, it's better to stop, look at the data and then start another one.
                    '''
                    
    driver.close()


if __name__ == '__main__':

    main()