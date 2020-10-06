import matplotlib.pyplot as plt
xsuqares = []
ysquares = []

for i in range(1,100):
    ysquares.append(i**0.5)

for i in range(1,100):
    xsuqares.append(i)

"""
for i in range(10000,1000000):
    squares.append(i**2)
    """
plt.plot(xsuqares,ysquares,linewidth=2)
plt.title("First num",fontsize = 24)
plt.xlabel("xvalue",fontsize = 10)
plt.ylabel("yvalue",fontsize = 10)
plt.tick_params(axis='both',labelsize = 10)
plt.show()