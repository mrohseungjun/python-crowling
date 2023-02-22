from bs4 import BeautifulSoup
import urllib.request as req

url = "https://finance.naver.com/marketindex/"
resq = req.urlopen(url)

soup = BeautifulSoup(resq,'html.parser')

val = soup.select_one('span.value').string
print('환율:',val)

blined = soup.select_one('#exchangeList > li.on > a.head.usd > div > span.blind').string
print(blined)

print('#############################')
value1 = soup.select(
    '#exchangeList > li.on > a.head.usd > div > span')
print('환율 1 value :' , value1[0].string)
print('환율 1 value :' , value1[1].string)
print('환율 1 value :' , value1[3].string)
