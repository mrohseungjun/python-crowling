import requests
from bs4 import BeautifulSoup
lis = []
code = ['252670','251340']
for i in code:
    url="https://finance.naver.com/item/main.naver?code="+i
    # print(url)
    r = requests.get(url)
    txt = r.text
    soup = BeautifulSoup(txt,'html.parser')
    invers = soup.select_one('#middle > div.h_company > div.wrap_company > h2 > a').string
    
    # print(soup.select_one('#middle > div.h_company > div.wrap_company > h2 > a').get_text())
    today = soup.select_one('#chart_area > div.rate_info > div > p.no_today')
    price = today.select_one('span.blind').string
    lis.append([invers,price])
print(lis)    
##################################################################################
[['KODEX 200 선물인버스2X','2,810'],['KODEX 코스닥150선물인버스','4,755']]


