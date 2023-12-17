# Daraz 11.11 Top Selling Product Data Analysis #
## Objective
11.11 sale was going on [daraz](https://www.daraz.com.bd/) where discount was given on most of the products. From each category, we will go to the subcategories page. 
Then fetch the top selling products data from the first 3 pages and prepare a dataset. Henceafter, we will apply data transformation and do data analysis using Tableau. 

## What [Analysis](https://public.tableau.com/app/profile/neloy.barman/viz/Daraz11_11TopSellingProductDataAnalysis/analysis_on_overall_data) to find out: - ##
* How many subcategories does each category have? 
* Among all the products, how many of them are offered with standard delivery and free delivery? 
* How many Flagship and General Stores are there? Which one is more in number ?
* Which category is offered with the most and the least discount?  
* Which product has the most discount? What was its original and discount price? How much the discount prices scatter from the original prices?
* Considering all types of ratings, which product has the highest number of ratings among all the categories and also subcategories? 
* How many unique products are sold by each seller? Which seller is selling the most number of products based on category and subcategories?
* Does one seller sell its products in different categories? 
* Does 3 factors: 
  * Chat Response Rate(%), 
  * Positive Seller Ratings(%) 
  * & Ship On Time(%)
    affects a seller on being a flagship store?
* Among the categories, which subcategories are offered with the most & the least discounts?
* As much as the discount is, the more the seller has to sell the products to reach a break-even point equal to the original price of 50 products. Is it true?
## You can find all the analysis within this [Tableau DashBoard](https://public.tableau.com/app/profile/neloy.barman/viz/Daraz11_11TopSellingProductDataAnalysis/analysis_on_overall_data)

## Analysis and Observations

### Overall Data Analysis
![analysis_on_overall_data](https://github.com/Neloy-Barman/Daraz-11.11-Top-Selling-Product-Data-Analysis/assets/110896263/27b7df19-4322-4787-90a8-c4eceab536bb)
* Number of sub-categories within the categories ranges from 7-12.
   * Mother & Baby
   * TV & Home Appliances
   * Watches, Bags & Jewellery<br/>
    have the most number of sub-categories.
* Daraz has more non-flagship stores than the flagship ones.
* This e-commerce website offered more products with free delivery facility than the ones with standard delivery.
* Categorically the most discount was offered in Men's & Boy's Fashion and the least discount was offered within Groceries.
### Product Data Analysis
![product_data_analysis](https://github.com/Neloy-Barman/Daraz-11.11-Top-Selling-Product-Data-Analysis/assets/110896263/c59eeca2-c1fb-42ed-8a8a-4c05249113b0)
* Top 3 most discounted products within all categories -
  * (11 Taka Deal) Dancing cactus talking cactus Stuffed Plush Toy Electronic toy with song plush cactus potted toy Early Education Toy For kids<br/>
    Discount offered - 98%
  * New Style Leather feragamo Belt For Men & Black Leather Formal Belt For Men<br/>
    Discount offered - 92%
  * Men's Pu Leather Wallet High Quality Men Long Wallet Male Business Pu Leather Purse & Black High quality Leather Long Wallet For Men<br/>
    Discount offered - 91%
* There were many products where no discount was offered.
* Top 3 products with most number of ratings among all categories -
  * Diamond potato 1kg ± 25 gm - 11914
  * S8 Ultra Smart Watch Series 8 Ultra Men Women Bluetooth Call Wireless Charging Fitness Bracelet 1.95/1.44 Inch HD Screen - 8908
  * Local Onion 1 kg (± 25 gm) - onion - 6280
* There are various types of products among all categories but potato and onion which are take place in the most number of ratings products.
### Seller Data Analysis
![seller_data_analysis](https://github.com/Neloy-Barman/Daraz-11.11-Top-Selling-Product-Data-Analysis/assets/110896263/ee988217-986c-443e-b725-fe29c9ca3b99)
* Top 3 sellers selling most number of distinct products: -
  * Daraz Fresh - 114
  * SWAP - 101
  * Well-being Distribution Ltd. - 66  
* There are many sellers who sells products in different categories and also in various sub-categories.
* A seller's Avg.
  * Chat Response Rate(%)
  * Positive Seller Ratings(%)
  * Ship On Time(%) <br/>
    $ ~~~~~~~~~~ $ don't affect it on being a flagship seller.
### Break-even point & sub-caterical average discount analysis 
![discount_ _break-even_point](https://github.com/Neloy-Barman/Daraz-11.11-Top-Selling-Product-Data-Analysis/assets/110896263/ca47c76c-5d37-44f0-83e3-2b2833887b3d)
* There is a relationship between the offered discount and the number of products to be sold to reach a break-even point. So, as much as the discount is, the more the products to be sold to reach the break-even point equal to the price of 50 products.<br/>
* Sub-categorical most discount -<br/>
  * Discount: 67.52<br/>
    Sub-category:  Accessories  <br/>
    Category: Men's & Boy's Fashion<br/>
  * Discount: 61.55<br/>
    Sub-category:  Shop Men's Bags Online in Bangladesh  <br/>
    Category: Watches, Bags, Jewellery<br/>
  * Discount: 51.18<br/>
    Sub-category:  Mobile Accessories <br/>
    Category: Electronic Devices <br/>
  * Discount: 49.89<br/>
    Sub-category:  Audio <br/>
    Category: Electronic Accessories<br/>
  * Discount: 46.18<br/>
    Sub-category: Sports & Outdoor Play <br/>
    Category: Mother & Baby<br/>
  * Discount: 46.36<br/>
    Sub-category: Shoes & Clothing <br/>
    Category: Sports & Outdoors<br/>
  * Discount: 44.84<br/>
    Sub-category: Interior Accessories<br/>
    Category: Automotive & Motorbike<br/>
  * Discount: 41.11<br/>
    Sub-category: TV & Video Accessories<br/>
    Category: TV & Home Appliances<br/>
  * Discount: 38.64<br/>
    Sub-category: Beauty Tools<br/>
    Category: Beauty Tools<br/>
  * Discount: 33.64<br/>
    Sub-category: Cooking Ingredents<br/>
    Category: Groceries<br/>

## How to use: - 
1. Clone the repo
```bash
git clone https://github.com/Neloy-Barman/Daraz-11.11-Top-Selling-Product-Data-Analysis.git
```
2. Create & activate virtual Environment
```
virtualenv --no-site-packages venv
source venv/bin/activate
``` 
3. Install dependencies
```
pip install -r requirements.txt
```
4. Run the product data scraper
```bash
python product_data_scraper.py
```
5. Run the subcategories data scraper
```bash
python subcategory_scraper.py
```

## Challenges faced
* The data scraper got stopped after running for hours. In that case, I had to restart the scraper and scrape from there mannualy.
* There are some unique data eleements, there it showed different characteristics. But this was written for the general case. For this, I again had to restart and scrape.
* As there are many categories, so, it takes a lot of time to scrape all the data.            
