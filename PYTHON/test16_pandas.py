import pandas as pd

df = pd.read_csv('apt_201910.csv',encoding='cp949')
print(len(df))
print(type(df))
print(df.shape)
print(df.head())
print(df.tail())
print('-----------------')

# 면적이 130보다 큰 거 출력
print(df.면적)
print('==============')
print(df[df.면적>200])
print('==============')

# 10개만 단지명,가격
print(df.loc[:10,['단지명','가격']])
print('==============')

# 단지명 , 가격, 면적 출력 단, 면적 130다 큰 거 출력
print(df.loc[:,['단지명','가격','면적']][df.면적>130])