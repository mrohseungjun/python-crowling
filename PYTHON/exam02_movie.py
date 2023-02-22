import urllib.request as req
from bs4 import BeautifulSoup

url = 'https://movie.daum.net/ranking/reservation'
resq = req.urlopen(url)

soup = BeautifulSoup(resq,'html.parser')
movie = soup.select('#mainContent > div > div.box_ranking > ol > li > div > div.thumb_cont ')

ol = soup.select_one('#mainContent > div > div.box_ranking > ol ')
lis = ol.select('li')

for i in movie:
    movieTitle = i.select_one("a.link_txt").get_text()
    moviegrade = i.select_one("span.txt_grade").get_text()
    movieReser = i.select_one("span.txt_num").get_text()
    print('영화 :',movieTitle, end = '/')
    print('평점 :',moviegrade, end = '/')
    print('예매율 :',movieReser)

print('--------------------------------------------')
# find 사용
for i in movie:
    movieTitle = i.find('a',class_='link_txt').get_text()
    moviegrade = i.select_one("span.txt_grade").get_text()
    movieReser = i.select_one("span.txt_num").get_text()
    print('영화 :',movieTitle, end = '/')
    print('평점 :',moviegrade, end = '/')
    print('예매율 :',movieReser)

