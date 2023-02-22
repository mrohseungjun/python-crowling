#apt_201910.csv 파일을 usecsv에 있는 함수를 사용하여 3개 출력
import useCSV as usecsv
import csv
import re

ap = usecsv.opencsv('apt_201910.csv')
apt = usecsv.switchcsv(ap)
new_list = [[]]

#print(apt[:3])

# apt_201910.csv 총 개수
#print(len(apt))
# 신군구 단지명 가격 ==> 6개 출력

# for i in apt[:6]:
#     print([i[0],i[4],i[-4]])

#강원도의 120 m2 이상의 3억 이하 검색하기 시군구 단지명 가격 출력   
for i in apt:
    try:
        if i[5] >= 120 and i[-4] <= 30000 and re.match('강원',i[0]):
            new_list.append([i[0], i[4], i[-4]])
    except:
        pass

#print(new_list[:4])

# with open("apt11.csv","w", newline='') as f:
#     a = csv.writer(f, delimiter=',')
#     a.writerow(new_list)

#############################################
# 첫번째 행에 컴퓨터, 노트북, 태블릿
# 두번째 행에 100,80,60
# 리스트 형태로 표현

test_list = [['컴퓨터','노트북','태블릿'],[100,80,60]]
with open("test.csv","w", newline='') as f:
    a = csv.writer(f)
    a.writerow(test_list)
