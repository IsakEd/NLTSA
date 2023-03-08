import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d


data = np.loadtxt("elNino.txt", usecols=range(1,13), dtype='float')
print(tempdiff := np.ndarray.flatten(data))

tau = 12

plt.plot(tempdiff[:-(tau)], tempdiff[tau:])
plt.show()

ax = plt.axes(projection='3d')

zline = tempdiff[:-(2*tau)]
xline = tempdiff[tau:-(tau)]
yline = tempdiff[2*tau:]

print(len(xline))
print(len(yline))

print(len(zline))

ax = plt.axes(projection='3d')
ax.scatter3D(xline, yline, zline, c=zline, cmap='Greens');
