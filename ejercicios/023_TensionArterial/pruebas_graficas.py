import matplotlib.pyplot as plt
import math
xs=[i/10 for i in range(1,1001)]
ys=[]
zs=[]
for x in xs:
    ys.append(math.sin(x))
    zs.append(math.cos(x))
plt.plot(xs,ys,"red")
plt.plot(xs,zs,"green")
plt.show()