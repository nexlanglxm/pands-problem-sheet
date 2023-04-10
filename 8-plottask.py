'''Write a program called plottask.py that displays:

a histogram of a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2, 
and a plot of the function  h(x)=x3 in the range [0, 10], 
on the one set of axes.
Some marks will be given for making the plot look nice (legend etc).

'''
import numpy as np
from numpy import random
import matplotlib.pyplot as plt

x = random.normal(loc = 5, scale = 2, size=(1000))
plt.hist(x, color="c")
plt.show()

xpoints = np.array(range(0,10))
ypoints = xpoints*xpoints*xpoints
plt.plot(xpoints, ypoints, label="plot of the function", color="m")
plt.show()