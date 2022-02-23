
# ax = plt.gca()
# ax.set_autoscale_on(True)
# line, = ax.plot(x, y)
# import random
# for i in range(100):
#     line.set_xdata(x)
#     ax.relim()
#     ax.autoscale_view(True,True,True)
#     plt.draw()
#     random.shuffle(x)
#     random.shuffle(y)
#     plt.pause(0.1)


import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import imread

img = plt.imread('/home/shivjeetbhullar/Projects/radr.jpeg')



im = plt.imread("/home/shivjeetbhullar/Projects/radr.jpeg")
theta = [x for x in range(5)]
r = np.sin(theta)

#plt.imshow(im, extent=[0, 200, 0, 150])
ax = plt.gca(polar=True)

ax.set_facecolor('tab:blue')
ax.set_autoscale_on(True)




c = ax.scatter(theta, ['10cm','30cm','60cm','90cm','100cm'], c=r, s=30, cmap='hsv', alpha=1)
x = [x for x in range(5)]

ax.set_thetamin(0)
ax.set_thetamax(180)
 

from time import sleep

n = 0
xlin = [1 for x in range(5)]

ax.plot([1,1,1,1,1],[0,1,2,3,4],color='red')
plt.show()
sleep(111)
while True:
 n+=0.3
 #line.set_xdata(xlin)
 ax.relim()
 ax.autoscale_view(True,True,True)
 xlin = [n,n,n,n,n]
 plt.draw()
 plt.pause(100)
 print(n)
 
 
