import urllib.request as req
from bs4 import BeautifulSoup
import re

url = "https://media.daum.net/economic/"
resq = req.urlopen(url)
soup = BeautifulSoup(resq,'html.parser')
# lis = soup.find_all(href=re.compile(r'^https://v'))
# for i in lis[:100]:
#      print(i.attrs['href'])

# 100개중에서 https://v 시작하는 기사 출력

# select로
links = soup.select('a[href]')
for i in links[:100]:
     # if re.search('https://v.\w+',i['href']): #\w 영문자 숫자 언더바(밑줄) [A-Za-z0-9]
     #      print(i.get_text().strip) #strip 공백제거
     if re.match('https://v.\w+',i['href']): #\w 영문자 숫자 언더바(밑줄) [A-Za-z0-9]
          print(i.string) #strip 공백제거     
