from matplotlib import pyplot as plt
from functions import *

plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True

bifurcation_points = []

x_precision = 1000
xvals = [x/x_precision for x in range(2*x_precision,4*x_precision)]

dots_to_draw = []
for x in xvals:
    peaks = logistic_map_asymptotes(x, 0.1)
    [dots_to_draw.append((x, y)) for y in peaks]

delta = (bifurcation_points[3]-bifurcation_points[2])/(bifurcation_points[4]-bifurcation_points[3])
print("Delta: " + str(delta))

plt.xlim(2.5, 4)
plt.ylim(0, 1)
plt.grid()
for pair in dots_to_draw:
        #plt.plot(pair[0], pair[1], marker=",")
        plt.plot(pair[0], pair[1], marker="o", markersize=1, markeredgecolor="black")

plt.title("x[n+1] = r[n](1-x[n])")
plt.xlabel("r")
plt.ylabel("lim")
plt.show()


