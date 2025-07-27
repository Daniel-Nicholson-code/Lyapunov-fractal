import numpy as np
import matplotlib.pyplot as plt

#itr is the number of iterations the logistic function
#performs before stopping. res is the amount of data points
#being plotted. progress stores a string acting as a progress
#bar for generating the plot
itr = 1000
res = 5000
progress = ""

#creating an array for the x and y axis (where y is blank, and
#x/r linearly increases from -2 to 4)
r = np.linspace(-2, 4, res)
y = np.zeros(res)

#iterates over every r value and computes corresponding y value
for i in range(res):
    
    #performing the logistic map
    x = np.random.random()
    for n in range(itr):
      x = (r[i] * x) * (1 - x)

    #setting y to the converged value
    y[i] = x

    #generating progress bar string
    temp = f"{round(i / res * 100)}% done"

    #comparing progress bar to the progress bar of prev. frame
    #and only update it if it has changed
    if temp != progress: print(temp)

    progress = temp

#turning the data into a plot
fig, ax = plt.subplots()
plt.scatter(r, y, color='black', s=0.5)

#displaying the plot
plt.show()