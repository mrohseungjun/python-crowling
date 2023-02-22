from selenium import webdriver as wd
from bs4 import BeautifulSoup
import re
import pandas as pd

path = "C:\\Users\\admin\\Downloads\\chromedriver_win32\\chromedriver.exe"
options = wd.ChromeOptions()
# options.add_experimental_option('excludeSwitches',['enable-logging'])
options.add_experimental_option('detach',True)
driver = wd.Chrome(path,options=options)
driver.get('https://www.melon.com/chart/week/index.htm')
page = driver.page_source
#lst50 > td:nth-child(6) > div > div > div.ellipsis.rank01 > span > a
soup = BeautifulSoup(page,'html.parser')
# print(soup)

# 순위 곡 앨범 좋아요 수
chart = soup.select('tr#lst50')
# print(chart)
chartlis = []
for i in chart:
    
    num = i.select_one('td:nth-child(2) > div > span.rank').get_text()
    name = i.select_one('td:nth-child(6) > div > div > div.ellipsis.rank01 > span > a').get_text()
    singer =  i.select_one('div.ellipsis.rank02 > a').get_text()
    album =  i.select_one('div.rank03 > a').get_text()
    likes =  i.select_one('span.cnt').get_text()
    likes = re.sub('\n총건수\n','',likes)
    likes = re.sub(',','',likes)
#     print(num,name,singer,album,likes)
    chartlis.append([num,name,singer,album,likes])


# melon.csv

# with open : melone_file.csv
with open('melone_file.csv','w',encoding='utf-8-sig')as file:
    file.write('순위, 곡명 ,가수, 앨범, 좋아요\n')
    for item in chartlis:
        row = ','.join(item)
        file.write(row+'\n')

# pandas : melone_pandas.csv
df = pd.DataFrame(chartlis,columns=('순위','곡명','가수','앨범','좋아요'))
df.to_csv('melone_pandas.csv',encoding='utf-8-sig', index=False)

file_df = pd.read_csv('melone_pandas.csv',encoding='utf-8-sig')
print(file_df)
