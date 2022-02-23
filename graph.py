import matplotlib.pyplot as plt
from time import sleep
import numpy as np

theta = [x+1 for x in range(5)]
r = np.sin(theta)

fig = plt.figure()

fig.set_facecolor('tab:blue')

ax = fig.add_subplot(111, polar=True)
ax.set_autoscale_on(True)
ax.set_facecolor('tab:blue')

c = ax.scatter(theta, ['0cm','10cm','30cm','60cm','90cm'], c=['green','green','blue','red','pink'], s=30, cmap='hsv', alpha=1)
x = [x for x in range(5)]

line, = ax.plot([1,1,1,1,1],[0,1,2,3,4],color='red')
ax.set_thetamin(0)
ax.set_thetamax(180)
n,forw,objectsx,objectsy,objectscol=0.1,True,[],[],[]

import random
while True:
    if forw:n+=0.1
    else:n=n-0.1
    distance = random.randint(5,100)
    if distance > 90:col,locy = 'green',4
    elif distance > 60:col,locy = 'pink',3
    elif distance > 30:col,locy = 'yellow',2
    else:col,locy='red',1
    objectsx.append(n);objectsy.append(locy);objectscol.append(col)
    
    c.set_offsets(np.c_[objectsx,objectsy])
    c.set_color(objectscol)
    if n >= 3:
        forw,objectsx,objectsy= False,[],[]
    elif n < 0 and not forw:
        forw,objectsx,objectsy= True,[],[]
    line.set_xdata([n for x in range(5)])
    ax.relim()
    plt.draw()
    plt.pause(5)

