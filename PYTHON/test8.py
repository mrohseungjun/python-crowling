import csv
import re



def opencsv(filename):
    output = []
    isput = [] 
    f = open(filename,'r')
    reader = csv.reader(f)

    for i in reader:
        tmp=[]
        for j in i:
            try:
                if re.search('\d',j):
                    # print(j) # , 제거하고 출력
                    tmp.append(float(re.sub(',','',j)))
                else:
                    tmp.append(j)    
            except:
                pass
    output.append(tmp)

        #외국인 비율이 5프로가 넘는 것만 출력(구,한국인,외국인,외국인 비율(%))
    for i in output:
        try:
            foreign = round(i[2]/(i[1]+i[2])*100,1)
            if foreign > 5:
                # print(i[0],i[1],i[2],foreign)
                isput.append([i[0],i[1],i[2],foreign])  
        except:
            pass
    for i in isput:
       return i 

total = opencsv('popSeoul2.csv')
# print(total) #5개만 출력

test = [10,20,30,40,50]
# 50 의 위치  값
print(test.index(50))

j = '1,468,246'
print(float(re.sub(',','',j)))
print(int(re.sub(',','',j)))