import pandas as pd

df = pd.read_csv('apt_201910.csv',encoding='cp949',thousands=',')

# # 면적이 200보다 큰 거 출력
# print(df.loc[:,["면적"]][df.면적>200])

# # 지역에 강릉이 들어간 자료만 출력
# print(df[df['시군구'].str.find('강릉')>-1])

# # 지역이 강릉인 시군구, 가격, 면적 10행 출력
# print(df.loc[:10,['시군구','가격','면적']])

# # 면적이 130 넘는 아파트의 가격 출력
# print(df.가격[df.면적>130])

# 면적이 130 넘고 가격이 2억 미만인 아파트의 가격 출력
print(df.가격[(df.면적>130)&(df.가격<200000000)])
print('===========================================')
# 면적이 130 넘거나 가격이 2억 미만인 아파트의 가격 출력
print(df.가격[(df.면적>130)|(df.가격<200000000)])
print('===========================================')
dfAsc = df.sort_values(by='가격', ascending=False)
print(dfAsc.가격)

# df.loc[원하는 행 조건, 원하는 열의 조건]
# 9억원을 초과하는 가격으로 거래된 단지명(아파트), 가격출력
print(df.loc[:,['가격','단지명']][df.가격>900000])

# 단가 = 가격 / 면적
df['단가'] = df.가격 / df.면적 # 없는 컬럼 '단가' 만들어서 넣는 법

print(df.loc[:10,('시군구','면적','단가')])
print(df.단가)