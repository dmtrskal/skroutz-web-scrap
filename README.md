# skroutz-web-scrap
Skroutz Web Scraping

Returns the skroutz shops in a .csv file that sell  a product below client's desired price.  

Input .xlsx file contains rows with:  
-Description (Name of the product)  
-Price (Maximum desired price)  
-skroutz URL for the current product (Link for the current product)  

Install Python 3 along with the following libraries:  
$ pip install BeautifulSoup4  
$ pip install xlrd  
$ pip install requests  

Execution:  
$ python checkPrices.py Products.xlsx  
