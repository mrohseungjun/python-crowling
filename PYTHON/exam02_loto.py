import urllib.request as req
from bs4 import BeautifulSoup
import pandas as pd

def select():
        url = 'https://dhlottery.co.kr/gameResult.do?method=byWin'
        resq = req.urlopen(url)
        soup = BeautifulSoup(resq,'html.parser')
        nums = soup.select('#article > div:nth-child(2) > div > div.win_result > div > div.num.win ')
        for i in nums:
              print(i.get_text(),end='\t')
        # print(nums)
 

##################################################################################
#find 방법으로
def find():
    url = 'https://dhlottery.co.kr/gameResult.do?method=byWin'
    resq = req.urlopen(url)
    soup = BeautifulSoup(resq,'html.parser')
    ballNum = soup.find_all('span',class_='ball')
    for i in ballNum:
          print(i.get_text(),end='\t') # i.string


select()



        
