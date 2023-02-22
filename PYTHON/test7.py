import re
import csv

f = open('popSeoul.csv','r')
reader = csv.reader(f)
output = []
isput = []

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

# print(output)    

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
    print(i)    