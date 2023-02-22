from bs4 import BeautifulSoup
import urllib.request as req

url = "https://ko.wikisource.org/wiki/%EC%A0%80%EC%9E%90:%EC%9C%A4%EB%8F%99%EC%A3%BC"
resq = req.urlopen(url)

soup = BeautifulSoup(resq,'html.parser')

value = soup.select('#mw-content-text > div.mw-parser-output > ul > li a')
print(value)
for i in value:
    print('-',i.string)
