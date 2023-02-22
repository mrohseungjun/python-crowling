from bs4 import BeautifulSoup
import urllib.request as req

url = open('C:/Users/admin/Desktop/PYTHON/Sample03.html', 'rt',encoding='utf-8').read()
# resq = req.urlopen(url)

soup = BeautifulSoup(url,'html.parser')
tag = soup.find('div',{'id':'myId1'})
print(tag.string)
tag = soup.find('div',{'class':'myClass1'})
print(tag.string)
tag = soup.findAll('div',{'class':'myClass1'})
for i in tag:
    print(i.string)




