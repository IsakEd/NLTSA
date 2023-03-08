import numpy as np
import matplotlib.pyplot as plt

do_plot = 1

data = np.loadtxt("lff.dat")
plt.plot(data)
if do_plot == 1:
    plt.show()

intervals = np.diff([x for x in range(len(data)-2) if np.sign(data[x]) != np.sign(data[x+1])])

plt.hist(intervals, 30)
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram of Data')
if do_plot == 1:
    plt.show()

def ACF(data, tau):

    ACF = np.zeros(len(data))
    for x in range(len(data)-(tau+1)):
        ACF[x] = (data[x] - np.mean(data)) * (data[x+tau] - np.mean(data)) / np.std(data)**2
    plt.plot(data, ACF)
    plt.title("ACF of timeseries: tau = " + str(tau))
    plt.show()
    return ACF

for tau in [1, 5, 10, 20, 100, 500]:
    ACF(data, tau)

