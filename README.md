<h1>Daraz 11.11 Top Selling Product Data Analysis</h1>

<h2>Project Development Journal</h2>

<h3><code style="color:blue">Problem Statement</code></h3>

<strong>11.11 sale was going on <a href="https://www.daraz.com.bd/">Daraz</a> where discount was given on most of the products. From each category, we will go to the subcategories page. 
Then fetch the top selling products data from the first 3 pages and prepare a dataset. Henceafter, we will apply data transformation and do data analysis using Tableau.</strong> 

<h3><code style="color:blue"><a href="https://public.tableau.com/app/profile/neloy.barman/viz/Daraz11_11TopSellingProductDataAnalysis/analysis_on_overall_data">Analysis</a> Requirements Blueprint</code></h3>

* <strong>How many subcategories does each category have?</strong> 
* <strong>Among all the products, how many of them are offered with standard delivery and free delivery?</strong>
* <strong>How many Flagship and General Stores are there? Which one is more in number?</strong>
* <strong>Which category is offered with the most and the least discount?</strong>
* <strong>Which product has the most discount? What was its original and discount price? How much the discount prices scatter from the original prices?</strong>
* <strong>Considering all types of ratings, which product has the highest number of ratings among all the categories and also subcategories?</strong> 
* <strong>How many unique products are sold by each seller? Which seller is selling the most number of products based on category and subcategories?</strong>
* <strong>Does one seller sell its products in different categories?</strong> 
* <strong>Does 3 factors: 
  * Chat Response Rate(%), 
  * Positive Seller Ratings(%) 
  * & Ship On Time(%)
    affects a seller on being a flagship store?</strong>
* <strong>Among the categories, which subcategories are offered with the most & the least discounts?</strong>
* <strong>As much as the discount is, the more the seller has to sell the products to reach a break-even point equal to the original price of 50 products. Is it true?</strong>

<h3><code style="color:blue">DashBoard</code></h3>
<strong>You can find all the analysis within this <a href="https://public.tableau.com/app/profile/neloy.barman/viz/Daraz11_11TopSellingProductDataAnalysis/analysis_on_overall_data">Tableau DashBoard</a></strong>

<h3><code style="color:blue">Analysis and Observations</code></h3>

<h4>i. Overall Data Analysis</h4>
<img src="https://github.com/Neloy-Barman/Daraz-11.11-Top-Selling-Product-Data-Analysis/assets/110896263/01c6fa4b-3fdb-41d5-83f2-4c0cebff4700">

* <strong>Number of sub-categories within the categories ranges from 7-12.</strong>
   * <strong>Mother & Baby</strong>
   * <strong>TV & Home Appliances</strong>
   * <strong>Watches, Bags & Jewellery<br/>
     have the most number of sub-categories.</strong>
* <strong>Daraz has more non-flagship stores than the flagship ones.</strong>
* <strong>This e-commerce website offered more products with free delivery facility than the ones with standard delivery.</strong>
* <strong>Categorically the most discount was offered in Men's & Boy's Fashion and the least discount was offered within Groceries.</strong>

<h4>ii. Product Data Analysis</h4>
<img src="https://github.com/Neloy-Barman/Daraz-11.11-Top-Selling-Product-Data-Analysis/assets/110896263/3cef6608-4768-4cd2-8ac0-d3dcce3e1af5">

* <strong>Top 3 most discounted products within all categories -</strong>

     | <p align="center">Product Name</p> | <p align="center">Discount(%)</p> |
     | --------------------------------- | ----------------------------------- |
     | <p align="center">(11 Taka Deal) Dancing cactus talking cactus Stuffed Plush Toy Electronic toy with song plush cactus potted toy Early Education Toy For kids</p> | <p align="center">98</p> |
     | <p align="center">New Style Leather feragamo Belt For Men & Black Leather Formal Belt For Men</p> | <p align="center">92</p> |
     | <p align="center">Men's Pu Leather Wallet High Quality Men Long Wallet Male Business Pu Leather Purse & Black High quality Leather Long Wallet For Men</p> | <p align="center">91</p> |

* <strong>There were many products where no discount was offered.</strong>

* <strong>Top 3 products with most number of ratings among all categories -</strong>

     | <p align="center">Product Name</p> | <p align="center">Number of Ratings</p> |
     | --------------------------------- | ----------------------------------- |
     | <p align="center">Diamond potato 1kg ± 25 gm</p> | <p align="center">11914</p> |
     | <p align="center">S8 Ultra Smart Watch Series 8 Ultra Men Women Bluetooth Call Wireless Charging Fitness Bracelet 1.95/1.44 Inch HD Screen</p> | <p align="center">8908</p> |
     | <p align="center">Local Onion 1 kg (± 25 gm) - onion</p> | <p align="center">6280</p> |
  
* <strong>There are various types of products among all categories but potato and onion which are take place in the most number of ratings products.</strong>

<h4>iii. Seller Data Analysis</h4>
<img src="https://github.com/Neloy-Barman/Daraz-11.11-Top-Selling-Product-Data-Analysis/assets/110896263/98168bd5-1262-4d8a-bd5b-31ff4b7fc680">

* <strong>Top 3 sellers selling most number of distinct products: -</strong>

     | <p align="center">Seller Name</p> | <p align="center">Product Count</p> |
     | --------------------------------- | ----------------------------------- |
     | <p align="center">Daraz Fresh</p> | <p align="center">114</p> |
     | <p align="center">SWAP</p> | <p align="center">101</p> |
     | <p align="center">Well-being Distribution Ltd.</p> | <p align="center">66</p> |
  
* <strong>There are many sellers who sells products in different categories and also in various sub-categories.</strong>
  
* <strong>A seller's Avg.</strong>
  * <strong>Chat Response Rate(%)</strong>
  * <strong>Positive Seller Ratings(%)</strong>
  * <strong>Ship On Time(%) <br/>
    don't affect it on being a flagship seller.</strong>

<h4>iv. Break-even Point & Sub-caterical Average Discount Analysis </h4>
<img src="https://github.com/Neloy-Barman/Daraz-11.11-Top-Selling-Product-Data-Analysis/assets/110896263/da8fabf8-7cd2-4d1b-bc0d-49d04ab1c857"> 

* <strong>There is a relationship between the offered discount and the number of products to be sold to reach a break-even point. So, as much as the discount is, the more the products to be sold to reach the break-even point equal to the price of 50 products.</strong>

* <strong>Sub-categorical most discount -</strong>

| **Category** | **Sub-category** | **Discount** | 
| ------------ | ---------------- | ------------ |
| <p align="center">Men's & Boy's Fashion</p> | <p align="center">Accessories</p> | <p align="center">67.52</p> |
| <p align="center">Watches, Bags, Jewellery</p> | <p align="center">Shop Men's Bags Online in Bangladesh</p> | <p align="center">61.55</p> |
| <p align="center">Electronic Device</p> | <p align="center">Mobile Accessories</p> | <p align="center">51.18</p> |
| <p align="center">Electronic Accessories</p> | <p align="center">Audio</p> | <p align="center">49.89</p> |
| <p align="center">Mother & Baby</p> | <p align="center">Sports & Outdoor Play</p> | <p align="center">46.18</p> |
| <p align="center">Sports & Outdoors</p> | <p align="center">Shoes & Clothing</p> | <p align="center">46.36</p> |
| <p align="center">Automotive & Motorbike</p> | <p align="center">Interior Accessories</p> | <p align="center">44.84</p> |
| <p align="center">TV & Home Appliances</p> | <p align="center">TV & Video Accessories</p> | <p align="center">41.11</p> |
| <p align="center">Health & Beauty</p> | <p align="center">Beauty Tools</p> | <p align="center">38.64</p> |
| <p align="center">Groceries</p> | <p align="center">Cooking Ingredents</p> | <p align="center">33.64</p> |

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
