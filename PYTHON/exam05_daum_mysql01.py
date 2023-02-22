import requests
from bs4 import BeautifulSoup
import pymysql

dbURL = "127.0.0.1"
dbPort = 3306
dbUser = "root"
dbPass = "1234"

conn = pymysql.connect(host=dbURL, port=dbPort,
                       user=dbUser, passwd=dbPass, db='big9_db', charset='utf8',
                       use_unicode=True)
insert_movie = "insert into daum_movie(title,grade,reserve) values(%s,%s,%s)"

req = requests.get("https://movie.daum.net/ranking/reservation")
html = req.text
soup = BeautifulSoup(html,'lxml')

movies = soup.select('#mainContent > div > div.box_ranking > ol >li')
print(len(movies))
#title, grade, reserve insert 하기
cur = conn.cursor()
movie = []
for i in movies:
    title = i.select_one("a.link_txt").get_text()
    grade = i.select_one("span.txt_grade").get_text()
    reserve = i.select_one("span.txt_num").get_text()
    print(title,grade,reserve)
    cur.execute(insert_movie,(title,grade,reserve))
    conn.commit()
    # movie.append([title,grade,reserve])
# print(movie)




