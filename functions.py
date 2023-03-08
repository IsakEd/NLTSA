import numpy as np
import tabulate


def logistic_map_no_transients(r: float, x0: float, depth: int = 11000, y_range_tolerance: int = 3) -> list:
    import numpy as np
    import matplotlib.pyplot as plt
    ser = [x0]*depth
    peaks =  []
    
    for xi in range (depth-1):
        ser[xi+1] = r*ser[xi]*(1-ser[xi]) #Logistic map formula

    series = ser[800:]
    
    return series


def logistic_map_asymptotes(r: float, x0: float, depth = 500, y_range_tolerance = 3) -> list:
    peaks =  []
    ser = [x0]*depth

    for xi in range (depth-1):
        ser[xi+1] = r*ser[xi]*(1-ser[xi]) #Logistic map formula

    peaks = set([round(x, y_range_tolerance) for x in ser[-100:]])
    # implicit rounding and uniquifying

    return peaks


def qck_table(names):
    names = names.split(",")
    print(names)