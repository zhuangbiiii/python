# for i in range(50):
#     print(i % 5)

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://www.baidu.com/'

def _testFunc_():
    browser = webdriver.Chrome()#声明浏览器
    browser.get(url)#打开网址
    
    button = browser.find_element(By.XPATH,'//*[@id="wrapper"]/div')
    print('output:')
    print(button)


_testFunc_()
