import csv
import re
import pandas as pd

# # singer2.csv 읽어 [이름 조회수] 300000 넘는 거 출력
# import useCSV
# sing = useCSV.opencsv('singer2.csv')
# sing_list = useCSV.switchcsv(sing)
# print(sing)

# new_list = [['이름','조회수']]
# for i in sing_list:
#     try:
#         if i[6]>300000:
#             # print(i[1],i[6])
#             new_list.append([i[1],i[6]])
#     except:
#         pass    
# print(new_list)

# # 파일로 내보내기 youtube30.csv    
# with open("youtube30.csv","w", newline='') as f:
#     a = csv.writer(f)
#     a.writerow(new_list)

# pandas read_csv
# 유튜브 조회수가 300000 넘는 것만 출력

df = pd.read_csv('singer2.csv',encoding='cp949',thousands=',')
df.columns = df.columns.str.replace(" ","")
print(df.loc[:,["이름","유튜브조회수"]][df.유튜브조회수>300000])