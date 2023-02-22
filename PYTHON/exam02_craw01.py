from bs4 import BeautifulSoup
import urllib.request as req

fp = open('C:/Users/admin/Desktop/PYTHON/fruits-vegetables.html',encoding='utf-8')
#print(fp)
soup = BeautifulSoup(fp,'html.parser')
#print(soup)
# 파프리카
tag = soup.select_one('#main-goods > ul#ve-list > li:nth-of-type(4)').string
print(soup.select('#ve-list > li[data-lo="us"]')[1].string)
print(soup.select_one('#ve-list > li.black').string)
print(soup.select_one('#ve-list > li.red').string)
print(soup.select_one('#main-goods > ul#ve-list > li:nth-of-type(2)').string)
print(soup.select_one('li:nth-of-type(5)').string) # 버전 때문에 루트설정을 잘해줘야함 tag변수랑 비교
print(tag)

condition = {'data-lo':'us','class':'black'}
print(soup.find("li",condition).string)
print(soup.find(id='ve-list').find("li",condition).string)