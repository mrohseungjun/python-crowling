import requests
from bs4 import BeautifulSoup
import pymysql


dbURL = "127.0.0.1"
dbPort = 3306
dbUser = "root"
dbPass = "root"

conn = pymysql.connect(host=dbURL, port=dbPort,
                       user=dbUser, passwd=dbPass, db='big9_db', charset='utf8',
                       use_unicode=True)
insert_weather = "insert into forecast(city,tmef,wf,tmn,tmx) values(%s,%s,%s,%s,%s)"

req = requests.get(
    "http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108")
html = req.text
soup = BeautifulSoup(html, 'lxml')
# print(soup.find_all('location'))


select_data = "select tmef from forecast order by tmef desc limit 1"
cur = conn.cursor()
cur.execute(select_data)
# select 한 결과 가져옴 : fetchone() , fetchall()
last_date = cur.fetchone()  # db  에 있는 최신날짜
print("type(last_date) : ", type(last_date))
print("last_date : ", last_date)


weather = {}
for i in soup.find_all('location'):
    weather[i.find('city').text] = []
    # print(i.find_all('data'))
    for j in i.find_all('data'):
        tmp = []
        if (last_date is None) or (last_date[0] < j.find('tmef').text):
            tmp.append(j.find('tmef').text)
            tmp.append(j.find('wf').text)
            tmp.append(j.find('tmn').text)
            tmp.append(j.find('tmx').text)
            weather[i.find('city').text].append(tmp)


# print(weather)
# 1. 연결 : connect
# 2. 데이터베이스 작업 위한 객체 cursor()
# 3. 질의문 전달 : execute()
# 4. 실행 : commit()

# dict 에 내용을  forecast 테이블에 저장
for i in weather:
    for j in weather[i]:
        cur = conn.cursor()
        cur.execute(insert_weather, (i, j[0], j[1], j[2], j[3]))
        conn.commit()
