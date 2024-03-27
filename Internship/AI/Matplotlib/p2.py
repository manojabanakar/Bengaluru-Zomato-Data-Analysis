from matplotlib import style
from matplotlib import pyplot as plt

style.use('ggplot')
x1=[1,2,3,4,5]
y1=[5,10,15,20,45]
x2=[1,3,5,7,9]
y2=[3,6,9,12,15]
plt.plot(x1,y1,c='b')
plt.plot(x2,y2,c='r')
plt.xlabel("X")
plt.ylabel("Y")

plt.show()
