import matplotlib.pyplot as plt
import matplotlib.animation
import numpy as np

fig, ax = plt.subplots()    

data = np.cumsum(np.random.normal(size=100)) #some list of data

ax.grid()
sc = ax.scatter(data[::2], data[1::2], c=data[1::2])
from time import sleep
def plot(a, data):
    data = np.cumsum([1,2,3,4,5,6,7,8,9,10])
    X = np.c_[data[::2], data[1::2]]
    print(X)
    print('_________________________________________')
    sc.set_offsets(X)
    sleep(1)

ani = matplotlib.animation.FuncAnimation(fig, plot, fargs=(data,),
            frames=4, interval=100, repeat=True) 
plt.show()