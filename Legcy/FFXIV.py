#首先你得有python  https://www.python.org/doc/
#然后安装BeautifulSoup4一款解析html的库：WIN + R，运行CMD输入pip install beautifulsoup4
#再安装 selenium 一款不知道什么库，只知道可以拉动态网页：同上pip install selenium
#最后安装xlwt写入excel：同上pip install xlwt
#偶尔会出现版本号所支持的库不能用这些错误，首先升级pip：python -m pip install --upgrade pip

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import xlwt
from xlwt import *
import time

lvRange = []
for x in range(18):
    x0 = x * 5 + 1
    x1 = x0 + 4
    lvRange.append(str(x0) + '-' + str(x1))
# print(lvRange)

xpathRange = []
for y in range(2,18):
    xpathRange.append('//*[@id="mw-content-text"]/div/div/div[2]/div/ul[1]/li['+str(y)+']/div')
# print(xpathRange)

#打开浏览器》打开网页》按下按钮》获取数据》写入数据》保存文件》关闭浏览器
file = Workbook(encoding='utf-8')
key = ['物品名称', '材料', '数量']
font = Font()
font.name = u'微软雅黑'
style = XFStyle()
style.font = font
style.alignment.horz = xlwt.Alignment.HORZ_CENTER
style.alignment.vert = xlwt.Alignment.VERT_CENTER

def downloading(url,fn):
    browser = webdriver.Chrome()#声明浏览器
    browser.get(url)#打开网址
    
    #成品
    item = []

    #材料
    item_material = []
    item_material_num = []
    item_material_count = []

    #获取数据
    table = file.add_sheet(fn)
    col = 0
    raw = 0
    for c in range(len(key)):
        table.write(raw, col, key[c], style)
        col += 1

    raw = 1
    for b in range(len(xpathRange)):
        button = browser.find_element(By.XPATH,xpathRange[b])
        button.click()
        time.sleep(2)#等待网页加载！否则读不全！！
        soup = BeautifulSoup(browser.page_source, 'html.parser')
        for tr in soup.find_all('tr',class_='tabber-item'):
            for div in tr.find_all('div',class_='item-name rarity-common'):
                for a in div.find_all('a'):
                    item.append(a.string)
                    #time.sleep(0.1)
                    print(a.string)
                    #input('-')
            for div in tr.find_all('div',class_='item-name rarity-uncommon'):
                for a in div.find_all('a'):
                    item.append(a.string)
                    #time.sleep(0.1)
                    print(a.string)
                    #input('-')
            count01 = 0
            for td in tr.find_all('td',class_='table--dark-m'):
                for span in td.find_all('span',class_='item-name'):
                    for a in span.find_all('a'):
                        item_material.append(a.string)
                        #time.sleep(0.1)
                        print(a.string)
                        count01 += 1
                        #input('--')
                for span in td.find_all('span', class_='item-number'):
                    item_material_num.append(span.string)
                    #time.sleep(0.1)
                    print(span.string)
                    #input('---')
                item_material_count.append(count01)

    # 写入物品名
    col = 0
    row = 1
    n = 0

    for x in range(len(item)):
        row0 = row
        row += item_material_count[x]
        table.write_merge(row0, row-1, col, col, item[x], style)

    # 写入物品材料名称和数量
    col = 1
    row = 1
    for x in range(len(item_material)):
        table.write(row, col, item_material[x], style)
        table.write(row, col + 1, item_material_num[x], style)
        row += 1

    table.col(0).width = 5000
    table.col(1).width = 5000

    
    file.save('配方统计.xlsx')
    browser.close()


#'刻木匠',配方列表 'https://ff14.huijiwiki.com/wiki/%E5%88%BB%E6%9C%A8%E5%8C%A0%E9%85%8D%E6%96%B9%E5%88%97%E8%A1%A8',
#'锻铁匠',配方列表 'https://ff14.huijiwiki.com/wiki/%E9%94%BB%E9%93%81%E5%8C%A0%E9%85%8D%E6%96%B9%E5%88%97%E8%A1%A8',
#'铸甲匠',配方列表 'https://ff14.huijiwiki.com/wiki/%E9%93%B8%E7%94%B2%E5%8C%A0%E9%85%8D%E6%96%B9%E5%88%97%E8%A1%A8',
#'雕金匠',配方列表 'https://ff14.huijiwiki.com/wiki/%E9%9B%95%E9%87%91%E5%8C%A0%E9%85%8D%E6%96%B9%E5%88%97%E8%A1%A8',
#'制革匠',配方列表 'https://ff14.huijiwiki.com/wiki/%E5%88%B6%E9%9D%A9%E5%8C%A0%E9%85%8D%E6%96%B9%E5%88%97%E8%A1%A8',
#'裁衣匠',配方列表 'https://ff14.huijiwiki.com/wiki/%E8%A3%81%E8%A1%A3%E5%8C%A0%E9%85%8D%E6%96%B9%E5%88%97%E8%A1%A8',
#'炼金术士',配方列表 'https://ff14.huijiwiki.com/wiki/%E7%82%BC%E9%87%91%E6%9C%AF%E5%A3%AB%E9%85%8D%E6%96%B9%E5%88%97%E8%A1%A8',
#'烹调师'配方列表 'https://ff14.huijiwiki.com/wiki/%E7%83%B9%E8%B0%83%E5%B8%88%E9%85%8D%E6%96%B9%E5%88%97%E8%A1%A8'
    
url = ['https://ff14.huijiwiki.com/wiki/%E5%88%BB%E6%9C%A8%E5%8C%A0%E9%85%8D%E6%96%B9%E5%88%97%E8%A1%A8','https://ff14.huijiwiki.com/wiki/%E9%94%BB%E9%93%81%E5%8C%A0%E9%85%8D%E6%96%B9%E5%88%97%E8%A1%A8','https://ff14.huijiwiki.com/wiki/%E9%93%B8%E7%94%B2%E5%8C%A0%E9%85%8D%E6%96%B9%E5%88%97%E8%A1%A8','https://ff14.huijiwiki.com/wiki/%E9%9B%95%E9%87%91%E5%8C%A0%E9%85%8D%E6%96%B9%E5%88%97%E8%A1%A8','https://ff14.huijiwiki.com/wiki/%E5%88%B6%E9%9D%A9%E5%8C%A0%E9%85%8D%E6%96%B9%E5%88%97%E8%A1%A8','https://ff14.huijiwiki.com/wiki/%E5%88%B6%E9%9D%A9%E5%8C%A0%E9%85%8D%E6%96%B9%E5%88%97%E8%A1%A8','https://ff14.huijiwiki.com/wiki/%E7%82%BC%E9%87%91%E6%9C%AF%E5%A3%AB%E9%85%8D%E6%96%B9%E5%88%97%E8%A1%A8','https://ff14.huijiwiki.com/wiki/%E7%83%B9%E8%B0%83%E5%B8%88%E9%85%8D%E6%96%B9%E5%88%97%E8%A1%A8']
fn = ['刻木匠','锻铁匠','铸甲匠','雕金匠','制革匠','裁衣匠','炼金术士','烹调师']
for z in range(len(url)): 
    downloading(url[z],fn[z])
input('----------------------------完成~----------------------------')
exit()


