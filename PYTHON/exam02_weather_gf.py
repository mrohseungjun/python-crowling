import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

df = pd.read_csv('weather.csv',encoding='euc-kr',index_col='지역')
# print(df)
print(df.loc[['서울','인천']])

#그래프 그리기
#한글 지원

font_name = mpl.font_manager.FontProperties(
    fname = 'c:/Windows/fonts/malgun.ttf').get_name()
mpl.rc('font',family = font_name)

# 차트종류 , 제목, 차트 크기 ,범례, 폰트 크기 설정
city_df = df.loc[['서울','인천','부산']]
print ( city_df)
ax = city_df.plot(kind = 'bar', title = '날씨',
             figsize=(12,7),legend=True,fontsize=12)

ax.set_xlabel('도시',fontsize = 12)
ax.set_ylabel('기온/습도',fontsize = 12)
ax.legend(['기온','습도'],fontsize=12)
plt.show()
