# Get all unity store free assets 
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Unity asset store url.
StoreUrl = 'https://assetstore.unity.com/?free=true&orderBy=1'
# Number of pages for all free assets(one page per 24 assets).
pagelen = 384
# 'Add to my assets' XPATH.
addassetbuttonxpath = '//*[@id="hover-action-add-to-cart-button-v2"]/button'
# "Agree EULA" css selector
agreeEULAbuttonclassname = '_3UE3J pDJt- auto'
agreeEULAbuttoncsscelector = 'body > div:nth-child(7) > div > div._2aLNG.dark-mode > div > div > div._3Sq-B._31_4H > div > div > div.tePrq > button._3UE3J.pDJt-.auto'
# "Successful message" csss selector
successfulmessagebuttoncsscelector = 'body > div:nth-child(7) > div > div._2aLNG.dark-mode._2wU9z > div > div > div._3Sq-B._2OMxm > div > div > div.lHyJV > div.ifont.ifont-close._2R6dj'
# "Next page" XPATH
nextpagebuttonxpath = '//*[@id="main-layout-scroller"]/div/div[1]/div/div/div/div/div[2]/div/div[2]/div[4]/button[7]'

def getallasset(inurl):
    browser = webdriver.Edge()
    browser.get(inurl)
    input('Waiting for user login...')
    
    for page in range(1,pagelen):
        for asset in range(24):
            addassetbutton = browser.find_element(By.XPATH,addassetbuttonxpath)
            print('asset button:')
            print(addassetbutton)
            addassetbutton.click()
            # Waiting for network readiness.
            time.sleep(5)
            # This button XPATH is not static,so we use css selector to find agree button.
            agreeEULAbutton = browser.find_element(By.CSS_SELECTOR,agreeEULAbuttoncsscelector)
            print('agree EULA button:')
            print(agreeEULAbutton)
            agreeEULAbutton.click()
            # Waiting for network readiness.
            time.sleep(10)
            successfulmessagebutton = browser.find_element(By.CSS_SELECTOR,successfulmessagebuttoncsscelector)
            print('successful message button:')
            print(successfulmessagebutton)
            successfulmessagebutton.click()
            # Waiting for network readiness.
            time.sleep(5)

        # One page done,navigate to the next page
        nextpagebutton = browser.find_element(By.XPATH,nextpagebuttonxpath)
        nextpagebutton.click()
        # Waiting for network readiness.
        time.sleep(5)


#getallasset(StoreUrl)

browser2 = webdriver.Edge()
browser2.get(StoreUrl)
input('Wait user login')

agreebuttons = browser2.find_elements(By.CLASS_NAME,agreeEULAbuttonclassname)
print(agreebuttons)
input('wait...')
browser2.close()