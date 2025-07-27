# Copyright 2024 Daniel Nicholson
# If using my code, please credit me

import numpy as np
import matplotlib.pyplot as plt

#N is the number of iterations the logistic function
#performs before stopping. res is the amount of data points
#being plotted. progress stores a string acting as a progress
#bar for generating the plot
N = 1000
res = 2000
progress = ""

#creating an array for the x and y axis (where y is blank, and
#x/r linearly increases from -2 to 4)
r = np.linspace(-2, 4, res)
y = np.zeros(res)

#iterates over every r value and computes corresponding y value
for i in range(res):
    
    #performing the logistic map and then finding the lambda value
    #(lyapunov exponent) by averaging a modified version of the
    #logistic map over all x values
    l = 0.0
    x = np.random.random()
    for j in range(N):
      x = (r[i] * x) * (1 - x)
      l += np.log( np.abs( r[i] * ( 1 - 2*x ) ) )
    l = l / N

    #setting y to the calculated lyapunov exponent
    y[i] = l

    #generating progress bar string
    temp = f"{round(i / res * 100)}% done"

    #comparing progress bar to the progress bar of prev. frame
    #and only update it if it has changed
    if temp != progress: print(temp)

    progress = temp

#turning the data into a plot
fig, ax = plt.subplots()
ax.plot(r, y, color="black", lw=0.5)

#displaying the plot
plt.show()
