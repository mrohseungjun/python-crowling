import urllib.request as req
from bs4 import BeautifulSoup
import pandas as pd


# for i in range(30):
# coff = soup.select('#contents > div.content > fieldset > div.tableType01')
# print(coff)
# for i in coff:
#     map = i.select_one('th.noline').get_text()
#     name = i.select_one('th:nth-child(2)').get_text()
#     addr = i.select_one('th:nth-child(4)').get_text()
#     number = i.select_one('th:nth-child(6)').get_text()
    
    # print(number)
# 지역 매장명 주소 전화번호

#url = "https://www.hollys.co.kr/store/korea/korStore.do"


# coffee_store = []
# print('=============================================================================================')
# for page in range(1,6):
#     url = 'https://www.hollys.co.kr/store/korea/korStore.do?pageNo=%d&sido=&gugun=&store=' %page
#     tag_tbody = soup.select_one('tbody')

#     for store in tag_tbody.select('tr'):
#         store_td = store.select('td')
#         store_sido = store_td[0].string
#         store_name = store_td[1].string
#         store_address = store_td[3].string
#         store_phone = store_td[-1].string
#         coffee_store.append([store_sido,store_name,store_address,store_phone])
# hollys_df = pd.DataFrame(coffee_store,columns=('지역','매장','주소','전화번호'))
# print(hollys_df)
############################
print('=============================================================================================')
def hollys_store(result):
    for page in range(1,6):
        url = 'https://www.hollys.co.kr/store/korea/korStore.do?pageNo=%d&sido=&gugun=&store=' %page
        resq = req.urlopen(url)
        soup = BeautifulSoup(resq,'html.parser')
        tag_tbody = soup.select_one('tbody')

        for store in tag_tbody.select('tr'):
            store_td = store.select('td')
            store_sido = store_td[0].string
            store_name = store_td[1].string
            store_address = store_td[3].string
            store_phone = store_td[-1].string
            result.append([store_sido,store_name,store_address,store_phone])
    hollys_df = pd.DataFrame(result,columns=('지역','매장','주소','전화번호'))
    print(hollys_df)
    return hollys_df        
    # return hollys_df
result = []
print('-- Holly store crawling >>>>>>>>>>>>>>>>>>')
hollys_store(result)

# https://www.weather.go.kr/w/obs-climate/land/city-obs.do