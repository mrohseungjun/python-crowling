import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl

df = pd.DataFrame([[500, 450, 520, 610],[690, 700, 820, 900],
                 [1100, 1030, 1200, 1380],[1500, 1650, 1700, 1850],
                 [1990, 2020, 2300 ,2420],[1020, 1600, 2200, 2550]],
                  index=['2015','2016','2017','2018','2019','2020'],
                   columns=['1a','2b','3c','4d'])
# print(df)
######################
# DataFrame 그래프로 표현
df = df.transpose() # 행 열 전환
df.plot()
plt.show()

df.to_csv('sales.csv',header=False)


y1 = [500, 450, 520, 610]
y2 = [690, 700, 820, 900]
y3 = [1100, 1030, 1200, 1380]
y4 = [1500, 1650, 1700, 1850]
y5 = [1990, 2020, 2300 ,2420]
y6 = [1020, 1600, 2200, 2550]
df1 = pd.DataFrame([y1,y2,y3,y4,y5,y6],index=['2015','2016','2017','2018','2019','2020'],
                  columns=['1분기','2분기','3분기','4분기'])
df1.to_csv('sales.csv',header=True)

##########
x = range(len(y1))
xLabel = ['first','second', ' third', 'fourth']
plt.plot(x,y1, color = 'b')
plt.plot(x,y2, color = 'orange')
plt.plot(x,y3, color = 'green')
plt.plot(x,y4, color = 'red')
plt.plot(x,y5, color = 'purple')
plt.plot(x,y6, color = 'brown')

plt.title('2015~2020 Quarterly sales')
plt.xlabel('Quarters')
plt.ylabel('sales')
plt.xticks(x,xLabel, fontsize = 12)
plt.legend(['2015','2016','2017','2018','2019','2020'],loc = 'upper left')

plt.show()





