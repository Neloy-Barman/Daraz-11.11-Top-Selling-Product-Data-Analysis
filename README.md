# Daraz-11.11-Top-Selling-Product-Data-Analysis #
## Objective
A 11.11 sale was going on daraz where discount was given on most of the products. From each category, we will go to the subcategories page. 
Then fetch the top selling products data from the first 3 pages and prepare a dataset. Henceafter, we will apply data transformation and do data analysis using tableau. 

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

## What [Analysis](https://public.tableau.com/app/profile/neloy.barman/viz/Daraz11_11TopSellingProductDataAnalysis/analysis_on_overall_data) to be found out: - ##
* How many subcategories does each category have? 
* Among all the products, how many of them are offered with standard delivery and free delivery? 
* How many Flagship and General Stores are there? 
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
