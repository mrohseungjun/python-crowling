import matplotlib.pyplot as plt
import matplotlib as mpl
from selenium import webdriver as wd
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import pandas as pd
import re
import time
from selenium.webdriver.common.keys import Keys
# 조회수 #시간 #이름
path = "D:\\JUNG\\util\\chromedriver_win32\\chromedriver.exe"
options = wd.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_experimental_option("detach", True)
driver = wd.Chrome(path, options=options)
driver.get('https://tour.interpark.com/?mbn=tour&mln=tour')

time.sleep(1)
driver.find_element(By.ID, 'spHeaderInput').click()
input_text = driver.find_element(By.ID, "txtHeaderInput")
input_text.send_keys('제주도')
driver.find_element(By.ID, 'btnHeaderInput').click()
driver.find_element(
    By.XPATH, '//*[@id="app"]/div/div[1]/div[2]/div[2]/div/ul/li[2]').click()
time.sleep(3)
all_info = driver.find_elements(By.CSS_SELECTOR, '.productInfo')
time.sleep(5)
datas = []

# app > div > div:nth-child(1) > div.resultAtc > div.contentsZone > div.panelZone > div.pageNumBox > ul
pageNum_list = driver.find_elements(
    By.CSS_SELECTOR, 'div.pageNumBox > ul > li')

print(len(pageNum_list))
# boxList > li:nth-child(1)
datas = []
for i in range(1, 5):  # range(1, len(pageNum_list)+1)
    product_list = driver.find_elements(By.CSS_SELECTOR, '#boxList > li')

    for info in product_list:
        try:
            title = info.find_element(By.CSS_SELECTOR, '.infoTitle').text
            price = info.find_element(By.CSS_SELECTOR, '.final').text
            price = re.sub(",", '', price)
            if len(title) > 0:
                datas.append([title, price])
        except:
            pass
    if i == len(pageNum_list):
        break
    pageNum_list[i].click()
    time.sleep(1)
print(datas)
df = pd.DataFrame(datas, columns=('호텔이름', '가격'))
hotel_dic = {'5만원이상': 0, '10만원이상': 0, '20만원이상': 0}
for item in datas:
    item = float(str(item).split('판매가\\n')[1].split('원~')[0].strip())
    if item > 200000:
        hotel_dic['20만원이상'] += 1
    elif item > 100000:
        hotel_dic['10만원이상'] += 1
    elif item > 50000:
        hotel_dic['5만원이상'] += 1
print(hotel_dic)
font_name = mpl.font_manager.FontProperties(
    fname='c:/Windows/fonts/malgun.ttf').get_name()
mpl.rc('font', family=font_name)

figure = plt.figure()
axes = figure.add_subplot(111)  # 몇개 그릴지 1행1열첫번째
axes.pie(hotel_dic.values(), labels=hotel_dic.keys(), autopct='%.1f%%')
plt.show()
