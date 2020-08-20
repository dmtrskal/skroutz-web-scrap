# skroutz-web-scrap
[Skroutz](https://www.skroutz.gr/) Web Scraping

:small_red_triangle: This version is **deprecated** since Skroutz webpages are now implemented with Javascript.  
:heavy_check_mark: Check [Web Scraping using *Selenium*](https://github.com/dmtrskal/skroutz-web-scrap-selenium) .

Returns the skroutz shops in a .csv file that sell  a product below client's desired price.  

**Execution**:  
```
$ python checkPrices.py Products.xlsx  
```

Input .xlsx file(e.g Products.xlsx) contains rows with:  
-Description (Name of the product)  
-Price (Maximum desired price)  
-skroutz URL for the current product 


**Requirements**:  
Install *Python 3* along with the following libraries:  
```
$ pip install BeautifulSoup4  
$ pip install xlrd  
$ pip install requests 
```


