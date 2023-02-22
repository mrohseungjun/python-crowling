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
# 부산의 날씨만 출력
select_data = "select * from forecast where city='부산' order by tmef desc"
cur = conn.cursor()
cur.execute(select_data)
result_busan = cur.fetchall()
print(result_busan)
# 부산의  최저기온 , 최고기온
select_data2 = "select max(tmn), min(tmn) from forecast where city='부산'"
cur.execute(select_data2)
result_busan2 = cur.fetchone()
print('최고기온 : ', result_busan2[0])
print('최저기온 : ', result_busan2[1])
#########
print('######')
result = []
for i in result_busan:  # 부산날씨
    result.append([i[2], i[4], i[5]])

print(result)
