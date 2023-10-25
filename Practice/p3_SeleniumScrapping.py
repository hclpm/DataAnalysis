from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=webdriver.ChromeOptions())

driver.get("https://m.stock.naver.com/worldstock/stock/AAPL.O/total")
pList = driver.find_element(by=By.TAG_NAME, value='strong').find_element(by=By.CLASS_NAME, value='GraphMain_price__u2XyL')
if pList != None:  
    for p in pList:
        print(p.text)
else:
    print('No value found!')