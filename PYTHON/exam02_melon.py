import requests
from bs4 import BeautifulSoup
import re

h = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"}

req = requests.get("https://www.melon.com/chart/week/index.htm",headers=h)
soup = BeautifulSoup(req.text,'html.parser')
#lst50 > td:nth-child(6) > div > div > div.ellipsis.rank01 > span > a
#lst50 > td:nth-child(6) > div > div > div.ellipsis.rank01 > span > a
chart = soup.select('#lst50 > td:nth-child(6) > div > div > div.ellipsis.rank01 > span > a')
# print(chart)
for idx,i in enumerate(chart,1):
    name = i.get_text()
    print(name)
    # print(idx,i.text)