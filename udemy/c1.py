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
web =[
   ## 'https://www.udemy.com/zh-tw/courses/development/web-development/',
    'https://www.udemy.com/courses/development/data-science/',
    'https://www.udemy.com/courses/development/mobile-apps/',
    'https://www.udemy.com/courses/development/programming-languages/',
    'https://www.udemy.com/courses/development/game-development/',
    'https://www.udemy.com/courses/development/databases/',
    'https://www.udemy.com/courses/development/software-testing/',
    'https://www.udemy.com/courses/development/software-engineering/',
    'https://www.udemy.com/courses/development/development-tools/',
    'https://www.udemy.com/courses/development/no-code-development/'
]

web_temp = ['https://www.udemy.com/zh-tw/courses/development/web-development/']

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

    time.sleep(3)


    soup = BeautifulSoup(driver.page_source, "html.parser") 
    name = soup.find_all('h1') #找名稱
    price  = soup.find_all('li',class_="special") #找價格

  

    ## print(soup.prettify());
    ## print(price);

    product_name  = soup.find_all("div", class_="udlite-focus-visible-target")   
    print(product_name)

    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(3)
    driver.close()
    

            
## df1 = pd.DataFrame({'商品名稱':product_name,'商品價格':product_price})

## print(df1)
