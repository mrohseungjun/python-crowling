import urllib.request as req
from bs4 import BeautifulSoup
import pandas as pd

def hollys_store(lis):
        url = 'https://www.weather.go.kr/w/obs-climate/land/city-obs.do'
        resq = req.urlopen(url)
        soup = BeautifulSoup(resq,'html.parser')
        body = soup.select('#weather_table > tbody > tr ')
        for i in body:
                area = i.select_one('td').string
                temp = i.select_one('td:nth-child(8)').string
                wet = i.select_one('td:nth-child(11)').string
                # print('지역 =',area)
                # print('온도 =',temp)
                # print('습도 =',wet)
                # print()
                lis.append([area,temp,wet])
lis = []
hollys_store(lis)
#데이터 프레임을 이용한 것
df = pd.DataFrame(lis,columns=('지역','온도','습도'))
df.to_csv('weather.csv',encoding='euc-kr',index=False)

wdf = pd.read_csv('weather.csv',encoding='euc-kr')
print(wdf)
######################
# 파일을 이용한 것
with open('weather_file.csv','w')as file:
        print('파일저장')
        file.write('지역, 온도, 습도\n')
        for item in lis:
                row = ','.join(item)
                file.write(row+'\n')

file_df = pd.read_csv('weather_file.csv',encoding='euc-kr')
print(file_df)


        
        
