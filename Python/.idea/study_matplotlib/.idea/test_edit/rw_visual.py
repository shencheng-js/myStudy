import matplotlib.pyplot as plt
from random_walk import RandomWalk

rw = RandomWalk(10000)
rw.fill_walk()
point_numbers = list(range(rw.num_points))

plt.scatter(0,0,c='red',s=20)
plt.scatter(rw.x_values,rw.y_values,c=point_numbers,cmap=plt.cm.Blues,edgecolors='none',s=15)
plt.scatter(rw.x_values[-1],rw.y_values[-1],c='red',s=20)
plt.show()