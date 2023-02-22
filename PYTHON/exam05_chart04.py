import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd
# weather_file.csv 파일을 읽어서
# 서울, 인천, 대전, 대구, 광주, 부산, 울산 지역의 
# 기온, 습도를 선그래프로 표현

wdf = pd.read_csv('weather.csv',index_col='지역',encoding ='euc-kr')
# print(wdf)
city_df = wdf.loc[['서울','인천','대전','대구','광주','부산','울산']]


xdata = ['서울','인천','대전','대구','광주','부산','울산']
temp = city_df['온도']
hum = city_df['습도']
print(temp)

#font
# 그래프 그리기
# 한글
font_name = mpl.font_manager.FontProperties(
    fname='c:/Windows/fonts/malgun.ttf').get_name()
mpl.rc('font', family=font_name)

plt.figure(figsize=(10,6))
plt.plot(xdata, temp, label='기온')
plt.plot(xdata, hum, label='습도')
plt.legend()
plt.show()

##############################
# 막대 그래프

# figure = plt.figure()
# axex = figure.add_subplot(111)

# axex.bar(xdata,hum)
# axex.bar(xdata,temp)
# axex.legend(['습도','기온'])
# plt.show()

ax = city_df.plot(kind='bar', title='날씨',
                  figsize=(12,7), legend=True, fontsize=12)
ax.set_xlabel('도시',fontsize=12)
ax.set_ylabel('기온/습도',fontsize = 12)
ax.legend(['기온','습도'],fontsize = 12)
plt.show()
