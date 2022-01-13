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

queryKey = 'air%20max'
curPage = '1'
web =['https://www.momoshop.com.tw/search/searchShop.jsp?keyword='+queryKey+'&searchType=1&curPage='+curPage+'&_isFuzzy=0&showType=chessboardType']

Chrome_driver_path = '/Users/hsujeihsien/Desktop/selenium/chromedriver'
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")

chrome_options.add_argument('User-Agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36"')
driver = webdriver.Chrome(executable_path=Chrome_driver_path,chrome_options=chrome_options)
## driver.maximize_window() ###最大化視窗

product_name = []
product_price = []



for d in web:
    driver.get(d)
    soup = BeautifulSoup(driver.page_source, "html.parser") 
    name = soup.find_all('h3',class_="prdName") #找名稱
    price  = soup.find_all('span',class_="price") #找價格


 
    total  = soup.find('span', class_="totalTxt") #找價格
    total2 = total.find_next_siblings("span")
    total3 = total2[0].text.replace('頁數','').split('/')
    print(total3)



    ### page = soup.find_all(attrs={'pageidx': True})
    ## print(len(page))
    ### for i in page:
    ###    print(i["pageidx"])

    ## page_link = page.find("a")
   ##  pidx = page[0].find("a")["pageidx"]
    ## print(pidx)
    ## page_last = page[0].find_all("a")
    ## page_last_one = len(page_last-1)
    ## print(page_last)
    ## print(page_last[len(page_last)-1].get_attribute("pageidx"))
    ## pagidx = page_last[len(page_last)-1].pageidx
    ## print(pagidx)
    ## print(len(page_last)-1)



    for i in name:
           ## print(i.text)
           product_name.append(i.text)
    
    for g in price:
            product_price.append(g.find('b').text)


   ## print(product_name)
   ## print(product_price)

            
df1 = pd.DataFrame({'商品名稱':product_name,'商品價格':product_price})

## print(df1)
