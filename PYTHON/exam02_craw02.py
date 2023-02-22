from bs4 import BeautifulSoup
import re

html ="""
    <ul>
        <li><a href="hoge.html"/>hoge</li>
        <li><a href="https://example.com.fuga"/>fuga*</li>
        <li><a href="https://example.com.foo"/>foo</li>
        <li><a href="shttps://example.com.foobbb"/>foobbb</li>
        <li><a href="http://example.com.aaa"/>aaa</li>
    </ul>
"""

soup = BeautifulSoup(html,'html.parser')
#print(soup)
lis = soup.find_all(href=re.compile(r'^https://'))
print(lis)
for i in lis:
    print(i.attrs['href'])


# tag= soup.select_one('ul > li:nth-of-type(2) a')['href']
# tag2= soup.select_one('ul > li:nth-of-type(3) a')['href']
# print(tag)
# print(tag2)