# Daraz 11.11 Top Selling Product Data Analysis #
## Objective
11.11 sale was going on [daraz](https://www.daraz.com.bd/) where discount was given on most of the products. From each category, we will go to the subcategories page. 
Then fetch the top selling products data from the first 3 pages and prepare a dataset. Henceafter, we will apply data transformation and do data analysis using Tableau. 

## What [Analysis](https://public.tableau.com/app/profile/neloy.barman/viz/Daraz11_11TopSellingProductDataAnalysis/analysis_on_overall_data) to be found out: - ##
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

## Some Findings from the dashboards
* Daraz offered more products with free delivery facility than the ones with standard delivery. 
* There are more non-flagship stores than the flagship ones within Daraz.
* Categorywise the most and the least average discounts offered: - 
  * Men's & Boy's Fashion :- 52.17%
  * Groceries :- 22.32%
* Top 3 products with most nunber of ratings
  * Among all categories :-   
    * Diamond potato 1kg±25 gm -> 11914
    * S8 Ultra Smart Watch Series 8 Ultra Men Women Bluetooth Call Wireless Charging Fitness Bracelet 1.95/1.44 Inch HD Screen -> 8908
    * Local Onion 1 kg (± 25 gm) - onion -> 6280
* Top 3 sellers selling most numnber of distinct products: -
  * Daraz Fresh - 114
  * SWAP - 101
  * Well-being Distribution Ltd. - 66  
* There are many sellers who sells products in different categories.
* A seller's Avg.
  * Chat Response Rate(%)
  * Positive Seller Ratings(%)
  * Ship On Time(%) <br/>
           don't affect it on being a flagship seller.
    
## Snaps from analysis
|||
|---|---|
|![analysis_on_overall_data](https://github.com/Neloy-Barman/Daraz-11.11-Top-Selling-Product-Data-Analysis/assets/110896263/27b7df19-4322-4787-90a8-c4eceab536bb)|![product_data_analysis](https://github.com/Neloy-Barman/Daraz-11.11-Top-Selling-Product-Data-Analysis/assets/110896263/c59eeca2-c1fb-42ed-8a8a-4c05249113b0)|
|![seller_data_analysis](https://github.com/Neloy-Barman/Daraz-11.11-Top-Selling-Product-Data-Analysis/assets/110896263/ee988217-986c-443e-b725-fe29c9ca3b99)|![discount_ _break-even_point](https://github.com/Neloy-Barman/Daraz-11.11-Top-Selling-Product-Data-Analysis/assets/110896263/ca47c76c-5d37-44f0-83e3-2b2833887b3d)|

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
