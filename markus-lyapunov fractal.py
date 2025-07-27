# Copyright 2024 Daniel Nicholson
# If using my code, please credit me

import numpy as np
import matplotlib.pyplot as plt

#N is the number of iterations the iterative function takes
#before stopping
#res is the width and height of the image produced
#S is the sequence of r values
#progress is a string acting as a progress bar for the render
N = 100
res = 200
S = np.zeros(N)
progress = ""

#generating 2D value array storing a value for each pixel
#which will be represented with a color
#lin is an array where the elements linearly increase from
#0 to 4 (storing the A and B/r values)
value = np.zeros([res, res])
lin = np.linspace(0, 3.9, res)

#computing the lyapunov exponent for each pixel of the image
for i in range(res): 
    for j in range(res):

        #resetting lambda value and x0
        l = 0.0
        x = 0.5

        #finding r values for the pixel coordinate
        A = lin[i]
        B = lin[j]

        #generating S, the sequence of r values
        for k in range(int(N / 2)):
            S[2*k] = A
            S[2*k+1] = B    

        #computing lyapunov exponent (lambda) for this pixel
        for k in range(N):
            r = S[k]
            x = (r * x) * (1 - x)
            l += np.log( np.abs( r * ( 1 - 2*x ) ) )
        l = l / N

        #Using sigmoid function on the result to make the final
        #color more legible (this step not necessary)
        l = 1 / (1 + np.exp( -1 * l))

        #Setting the color of the pixel
        value[i][j] = l

    #Calculating how much computation is left and displaying it if
    #there is an update
    temp = f"{round(i / res * 100)}% done"
    if temp != progress: print(temp)
    progress = temp

#Turning the data into an image
fig, ax = plt.subplots()
ax.pcolormesh(lin, lin, value)

#Outputing the final image
plt.show()
