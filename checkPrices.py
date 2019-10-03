## install Python3 (https://datascience.com.co/how-to-install-python-2-7-and-3-6-in-windows-10-add-python-path-281e7eae62a)
## pip install BeautifulSoup4
## pip install xlrd
## pip install requests


import os,sys
import requests
from bs4 import BeautifulSoup
import re
import csv
import xlrd 
import datetime

datetime_object = datetime.datetime.now()
timestampStr = datetime_object.strftime("%d-%b-%Y_%H-%M-%S")
##print('Current Timestamp : ', timestampStr)

out_filename = "skroutz-shops" + "__" + timestampStr + ".csv"


# Read input file and create the input lists
if len(sys.argv) < 2:
	print("Please give an excel file as argument!!")
	sys.exit()
	
wb = xlrd.open_workbook(sys.argv[1]) 
sheet = wb.sheet_by_index(0) 
sheet.cell_value(0, 0) 	
	
quote_page_list=[]  
price_limit_list=[]
no_url_products_list=[]
for i in range(1,sheet.nrows): 
	# only Products with URL are searched
	if not str(sheet.cell_value(i, 3)):
		no_url_products_list.append(str(sheet.cell_value(i, 0)))
	else:
		quote_page_list.append(str(sheet.cell_value(i, 3)))
		price_limit_list.append(sheet.cell_value(i, 2))


if len(no_url_products_list) != 0:
	print(30* "*")
	print("Prodcts without URL = " + str(no_url_products_list) + "\n")
	print(30* "*")

# Read HTML page and create output file
try:
	with open(out_filename, 'w', newline='\n', encoding='utf-8') as csv_file:
		writer = csv.writer(csv_file)
		for page, price_limit in zip(quote_page_list, price_limit_list):
			# query the website and return the html to the variable 'page'
			page = requests.get(page)
			
			# parse the html using beautiful soup and store in variable 'soup'
			soup = BeautifulSoup(page.content, 'html.parser')
			
			#print(soup.prettify())

			title = soup.title.text.strip() # strip() is used to remove starting and trailing
			title = title.replace(' - Skroutz.gr','')

			all_name_box = soup.find_all("div", attrs={"class": "shop-name"})
			all_price_box = soup.find_all("div", attrs={"class": "price"})
			all_url_box = soup.find_all("div", attrs={"class": "description"})
			
			writer.writerow([title, price_limit])
			for name_box, price_box,url_box in zip(all_name_box, all_price_box, all_url_box):
				#Parse Name 
				name = name_box.text.strip() # strip() is used to remove starting and trailing
				
				#Parse Price
				price = price_box.text.strip() # strip() is used to remove starting and trailing
				str_price = re.findall("\d+\,\d+", price) # Price with , as floating point
				str_price = str_price[0]
				
				# Price with . as floating point
				floatstr_price = str_price.replace(",",".")
				
				# Parse Url
				product_url = url_box.find('a')['href']
				url = "https://www.skroutz.gr" + product_url
				
				# Perform price check and print to excel file only info with 
				# prices BELOW Price limit variable 
				if float(floatstr_price) < float(price_limit):
					writer.writerow([name, str_price, url])
			writer.writerow(['\n'])
except Exception as e:
	print('ERROR FOUND: ' + str(e))
	print("HTTP status code  = {}({})".format(page.status_code, requests.status_codes._codes[page.status_code][0]))
	os.remove(out_filename)