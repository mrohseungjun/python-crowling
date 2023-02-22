import matplotlib.pyplot as plt

#add_subplot('특정위치')
#add_subplot([총 행의 수],[총 열의 수])
figure = plt.figure()
axex1 = figure.add_subplot(2,2,1)
axex2 = figure.add_subplot(2,2,2)
axex3 = figure.add_subplot(2,2,3)
axex4 = figure.add_subplot(2,2,4)

axex1.plot([0,2]) # y축 데이터
axex2.plot([1,1]) # y축 데이터
axex3.plot([2,0]) # y축 데이터
axex4.plot([1,2]) # y축 데이터
# plt.show()
######################
# subplots() : figure 와 subplot 동시 생성
# subplots (생성 할 subplot행, 열)
figure, axex = plt.subplots(2,2)
axex[0][0].plot([1,1])
axex[1][1].plot([1,2])
# plt.show()
##################
figure = plt.figure()
axex = figure.add_subplot(224)
x = [0, 2, 4, 6]
y = [0, 4, 0, 2]
x2 = [0, 1, 2, 3, 4, 5, 6]
y2 = [1, 2, 3, 4, 5, 6, 7]
axex.plot(x,y)
axex.plot(x,y,color='r', linestyle = 'dotted',marker="^")
axex.plot(x2,y2,color='k', linestyle = 'dotted',marker="o")
# plt.show()
############################
figure = plt.figure()
axex = figure.add_subplot(111)
x = [1, 2, 3, 4]
y = [1, 4, 3, 2]
axex.bar(x,y)
# plt.show()

#############################
figure = plt.figure()
axex = figure.add_subplot(111)
x = [1, 2, 3, 4]
y = [1, 4, 3, 2]
x2 = [2, 5, 7, 11]
y2 = [2, 3, 4, 5]
axex.bar(x,y)
axex.bar(x2,y2)
# plt.show()
##############################
figure = plt.figure()
axex = figure.add_subplot(111)
x = [10, 15 , 30 ,20]
y = ['1a', '2b', '3c', '4d']
axex.pie(x, labels=y, autopct='%.1f%%')
plt.show()
