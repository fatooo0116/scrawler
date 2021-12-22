import requests
import selenium
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time

###填入您的目標頁面
web =['https://www.momoshop.com.tw/goods/GoodsDetail.jsp?i_code=7447745&osm=Ad07&utm_source=googleshop&utm_medium=department_house_zojirushi&utm_content=bn&gclid=Cj0KCQiA8ICOBhDmARIsAEGI6o29X0pryCxY_CrgTUVFH1bME0dLh5c9RdxPuFUcRv1C0QNi4ImkDWsaAoUEEALw_wcB']

Chrome_driver_path = '/Users/hsujeihsien/Desktop/selenium/chromedriver'
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('User-Agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36"')
driver = webdriver.Chrome(executable_path=Chrome_driver_path,chrome_options=chrome_options)
driver.maximize_window() ###最大化視窗

product_name = []
product_price = []



for d in web:
    driver.get(d)
    soup = BeautifulSoup(driver.page_source, "html.parser") 
    name = soup.find_all('h1') #找名稱
    price  = soup.find_all('li',class_="special") #找價格

  

   ##  print(name);
    ## print(price);

    for i in name:
           product_name.append(i.find('a').text)
    
    for g in price:
            product_price.append(g.find('span').text)


    print(product_name)
    print(product_price)

            
df1 = pd.DataFrame({'商品名稱':product_name,'商品價格':product_price})

print(df1)
