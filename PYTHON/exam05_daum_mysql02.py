import requests
from bs4 import BeautifulSoup
import pymysql
import matplotlib.pyplot as plt
import matplotlib as mpl

dbURL = "127.0.0.1"
dbPort = 3306
dbUser = "root"
dbPass = "1234"

conn = pymysql.connect(host=dbURL, port=dbPort,
                       user=dbUser, passwd=dbPass, db='big9_db', charset='utf8',
                       use_unicode=True)

select_movie = "select grade from daum_movie"

cur = conn.cursor()
cur.execute(select_movie)
movies = cur.fetchall()
print(movies)
# print(type(movies))
movieDic = {'9점이상':0,'8점이상':0,'6점이상':0,'6점미만':0}

for movie in movies:
    movie = float(movie[0])
    #print(movie)
    if movie <= 9:
        movieDic['9점이상']+=1
    elif movie >=8:
        movieDic['8점이상']+=1
    elif movie >=6:
        movieDic['6점이상']+=1
    else:
        movieDic['6점미만']+=1

#font
font_name = mpl.font_manager.FontProperties(
    fname='c:/Windows/fonts/malgun.ttf').get_name()
mpl.rc('font', family=font_name)

figure = plt.figure()
axex = figure.add_subplot(111)
axex.pie(movieDic.values(), labels = movieDic.keys(),autopct = '%.1f%%')
plt.show()








