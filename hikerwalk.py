# -*- coding: utf-8 -*-
"""
This program used animWalk.py and Hiker.py to create a random path for the
lost hiker.  An animation of the random walk, the final coordinates of
the hiker and the distance of the hiker from the starting position are
provided for the user

"""
import math
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import random
#The user defines the number of steps in the random walk
n = int(input ('How many steps are in the random walk ? ---> '))
xLst = np.zeros(n)
yLst = np.zeros(n)
dist=0.0
def Hiker(n,xLst,yLst,dist):
    """
    Hiker is a function to generate lists of x and y
    coordinates of n steps for a random walk of  n steps
    along with distance between the first and last point
    """

    x0=0
    y0=0
    x=x0
    y=y0
    
    xLst[1] = x0
    yLst[1] = y0
    for i in range (n-1):
        rnum = random.random()
        if rnum <= 0.19:
            y=y+1
            x=x
        elif rnum <= 0.43:
            y=y+1
            x=x+1
        elif rnum <= 0.60:
            y=y
            x=x+1
        elif rnum <= 0.70:
            y = y-1
            x= x+1
        elif rnum <= 0.72:
            y = y-1
            x = x
        elif rnum <= 0.75:
            y = y-1
            x = x-1
        elif rnum <= 0.85:
            y = y
            x = x-1
        elif rnum <= 1.00:
            y = y+1
            x = x-1
        xLst[i+1] = x
        yLst[i+1] = y
    dist = math.sqrt ((x-x0)^2 + (y-y0)^2)
    return (xLst,yLst,dist)
[x_array,y_array,distance] = Hiker(n,xLst,yLst,dist)
print('The final coordinates for the hiker is  ',(x_array[n-1],y_array[n-1]))
print('The final distance of the hiker from the origin is ',distance)
plt.plot(x_array,y_array,'bo',x_array,y_array,'k')
xmin = min([min(x_array)]) 
xmax = max([max(x_array)])
plt.xlim(xmin, xmax)
plt.show()
                
                



