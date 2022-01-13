import requests
import selenium
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
from selenium import webdriver

import urlopen as uReq

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


###填入您的目標頁面

web_temp = ['https://www.cettire.com/collections/sale?q=&hPP=48&idx=dev_Cettire_date_desc&p=0&fR%5Bvisibility%5D%5B0%5D=YES&hFR%5Bdepartment%5D%5B0%5D=men&nR%5Bcompare_at_price_f%5D%5B%3E%5D%5B0%5D=0&is_v=1']

ec = [
    'https://www.udemy.com/zh-tw/courses/business/entrepreneurship/'
]



Chrome_driver_path = '/Users/hsujeihsien/Desktop/selenium/chromedriver'
chrome_options = webdriver.ChromeOptions()
## chrome_options.add_argument("--headless")
chrome_options.add_argument('User-Agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36"')




product_name = []
product_price = []


time.sleep(1)

for d in web_temp:
    driver = webdriver.Chrome(executable_path=Chrome_driver_path,chrome_options=chrome_options)

    driver.get(d)

    time.sleep(3) #必須要填 延遲讀取 page loaded


    soup = BeautifulSoup(driver.page_source, "html.parser") 
   
   
    ## find all Pages
    all_page  = soup.find_all("li", class_="current-of-page")[0].text.replace("1 of ", "")

    print(all_page)
    all_page  = int(all_page)
    print(all_page)

    for i in range(all_page):    
        print("======================================= No",i,"  ======================================= ")

        time.sleep(1)    
        product_r_price  = soup.find_all("div", class_="algolia-product__item")   
        

        for tag in product_r_price:

            link = tag.find_all("a", class_="algolia-product-card")
            print(link[0].get('href'))
        
            brand = tag.find_all("div", class_="algolia-product-card__brand")
            print(brand[0])

            product_name = tag.find_all("div", class_="algolia-product-card__name")
            print(product_name[0])        

            price = tag.find_all("s", class_="algolia-product-card__regular-price")
            print(price[0])

            sale_price = tag.find_all("span", class_="algolia-product-card__price--with-compare")
            print(sale_price[0])

            print("-----------------------------------")

        time.sleep(1)   
        element = driver.find_element_by_xpath("//li[@data-page='next']")
        element.click()

        





    """""

    soup = BeautifulSoup(driver.page_source, "html.parser") 
    name = soup.find_all('h1') #找名稱
    

    product_r_price  = soup.find_all("div", class_="algolia-product__item")   
    ## print(product_r_price)
    for tag in product_r_price:

        link = tag.find_all("a", class_="algolia-product-card")
        print(link[0].get('href'))
        
        brand = tag.find_all("div", class_="algolia-product-card__brand")
        print(brand[0])

        product_name = tag.find_all("div", class_="algolia-product-card__name")
        print(product_name[0])        

        price = tag.find_all("s", class_="algolia-product-card__regular-price")
        print(price[0])

        sale_price = tag.find_all("span", class_="algolia-product-card__price--with-compare")
        print(sale_price[0])

        print("-----------------------------------")
   """

   ## time.sleep(3)

   

   
   ## driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
   ## time.sleep(2)
    driver.close()
    

            
## df1 = pd.DataFrame({'商品名稱':product_name,'商品價格':product_price})

## print(df1)


