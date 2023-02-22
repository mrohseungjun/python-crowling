# survey.csv 위에서 5개 출력
import pandas as pd
df = pd.read_csv('survey.csv',encoding='cp949',thousands=',')
print(df.head())
print(df.mean()) #mean 평균 구하는 메소드
print('==========================================')

# 수입 합계
print(df.income.sum())

print('==========================================')
# 수입 중앙 값
print('수입 중앙값 : ', df.income.median())
print(df.describe())
print(df.sex.value_counts())