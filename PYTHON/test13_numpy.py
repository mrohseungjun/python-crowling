import numpy as np
import useCSV

# listName = useCSV.switchcsv(useCSV.opencsv('quest.csv'))
def switchcsv(listName):
    for i in listName:
        for j in i:
            try:
                i[i.index(j)] = float(j)
            except:
                pass
    return listName  
              
listName = switchcsv(useCSV.opencsv('quest.csv'))
quest = np.array(listName)
print(quest)
# 5보다 큰 값
print(quest > 5)

# 5보다 큰 값은 5로 수정
quest[quest > 5] = 100
print(quest)