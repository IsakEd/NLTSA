# %%
from matplotlib import pyplot as plt
from functions import *
import matplotlib.ticker as mtick


# %%
plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True

x_precision = 1000
xvals = [x/x_precision for x in range(2*x_precision,4*x_precision)]

dots_to_draw = []
for x in xvals:
    peaks = logistic_map_asymptotes(x, 0.1)
    [dots_to_draw.append((x, y)) for y in peaks]

plt.xlim(2.5, 4)
plt.ylim(0, 1)
plt.grid()
for pair in dots_to_draw:
        #plt.plot(pair[0], pair[1], marker=",")
        plt.plot(pair[0], pair[1], marker=",")

plt.title("x[n+1] = r[n](1-x[n])")
plt.xlabel("r")
plt.ylabel("lim")
plt.show()


# %%


# %% [markdown]
# Test the “ordinal pattern” program with some “hand made”
# examples:

# %%
def ordinal_symbol(ts: list, lag=1):
    if ts[0]<ts[1]:
        symbol = 1 if ts[1]<ts[2] else (2 if ts[2]>ts[0] else 4)
    else:
        symbol = 6 if ts[1]>ts[2] else (3 if ts[2]>ts[0] else 5)
    return symbol

# %%
print(all([
ordinal_symbol([5,2,7]) == 3,
ordinal_symbol([2,3,1]) == 4,
ordinal_symbol([1,2,3]) == 1,
ordinal_symbol([10,2,5]) == 5]))

# %% [markdown]
# For the logistic map with r=3.99, calculate the probabilities of
# the 6 D=3 ordinal patterns and plot the distribution:

# %%
def logistic_map_no_transients(r: float, x0: float, depth: int = 11000, y_range_tolerance: int = 3) -> list:
    import numpy as np
    import matplotlib.pyplot as plt
    ser = [x0]*depth
    peaks =  []
    
    for xi in range (depth-1):
        ser[xi+1] = r*ser[xi]*(1-ser[xi]) #Logistic map formula

    series = ser[800:]
    
    return series

# %%
def ordinal_probability(ordinal: int, r: float):
    s = logistic_map_no_transients(r, 0.1)
    syms = [ordinal_symbol(s[xi:xi+3])for xi in range(len(s)-3)] 
    return syms.count(ordinal)/len(s)

# %% [markdown]
# For the logistic map with r=3.99, calculate the probabilities
# of the 6 D=3 ordinal patterns and plot the distribution.

# %%
series = logistic_map_no_transients(3.99, 0.1)
logistics_map_symbols = [ordinal_symbol(series[xi:xi+3])for xi in range(len(series)-3)] 
print("Probability of D=3: " + str(round(100*ordinal_probability(3, 3.99), 2)) + "%")
counts = np.bincount(logistics_map_symbols, minlength=7)[1:] #removing first position because of 0-idxing
probabilities = counts / len(logistics_map_symbols)
plt.bar(range(1,7), probabilities)
plt.title(f"Ordinal symbol histogram, r = 3.99")
plt.xlabel("ordinal")
plt.ylabel("probability")
# format the y-axis ticks as percentages
fmt = mtick.PercentFormatter(xmax=1)
plt.gca().yaxis.set_major_formatter(fmt)
plt.show()

# %% [markdown]
# Calculate the ordinal bifurcation diagram with r in (3.5,4):

# %%
r_values = np.linspace(3.5, 4.0, 201)
def ordinal_distribution(r):
    series = logistic_map_no_transients(r, 0.1)
    logistics_map_symbols = [ordinal_symbol(series[xi:xi+3])for xi in range(len(series)-3)] 
    counts = np.bincount(logistics_map_symbols, minlength=7)[1:] #removing first position because of 0-idxing
    probabilities = counts / len(logistics_map_symbols)
    return(probabilities)
ordinal_probabilities = np.transpose(np.array([ordinal_distribution(r) for r in r_values]))


# %%


# %%

plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True

for ord, ordinal_data in enumerate(ordinal_probabilities):
        plt.plot(r_values, ordinal_data, label=str(ord+1))
    
plt.xlim(3.5, 4)
plt.ylim(0, 0.5)
plt.grid()

# format the y-axis ticks as percentages
fmt = mtick.PercentFormatter(xmax=1)
plt.gca().yaxis.set_major_formatter(fmt)

plt.title("Ordinal bifurcation diagram")
plt.xlabel("r")
plt.ylabel("ordinal probability")
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))

plt.show()


# %%


# %%


# %%


# %%


# %%


# %%


# %%


# %%


# %%


# %%


# %%


# %%


# %%


# %%


# %%


# %%


# %%


# %%


# %%


# %%


# %%


# %%


# %%


# %%


# %%



# %%


# %%


# %%


# %%


# %%


# %%


# %%


# %%


# %%
plt.xlabel("r")
plt.ylabel("probability of ordinal")
plt.title("Ordinal bifurcation diagram")
for D in range(1,7):
    plt.plot(r_range,ordinal_diagram_data[D-1],label = 'D = %s'%D)
plt.legend()
plt.show()

# %%


# %%


# %%


# %%


# %%


# %%


# %%


# %%


# %%


# %% [markdown]
# Calculate the ordinal bifurcation diagram with r in (3.5,4):

# %%


# %%


# %%


# %%


# %%


# %%


# %%


# %%


# %%


# %%


# %%


# %%


# %%


# %%


# %%


# %%


# %%


# %%


# %%


# %%


# %%


# %%


# %%


# %%


# %%


# %%


# %%


# %%



