# -*- coding: utf-8 -*-
"""parabolic_motion.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12-WTE2LHKjQZvVQej0Cwbby9-5w3cFGq
"""

import math
import matplotlib.pyplot as plt

def numeric_woHambatan(y,v,angle):
    dt = 0.01
    x = 0
    g = -9.8
    t = 0
    
    arrx = []
    arry = []

    vx = v * math.cos(math.radians(angle))
    vy = v * math.sin(math.radians(angle))

    while True :
        arrx.append(x)
        arry.append(y)

        t = t + dt
        vy = vy + (g * dt)
        x = x + (vx * dt)
        y = y + (vy * dt)

        if y < 0 :
            break
    return arrx,arry

arrx,arry = numeric_woHambatan(0,50,35)

plt.plot(arrx,arry)

def numeric_wHambatan(y,v,angle):
    dt = 0.01
    x = 0
    g = -9.8
    t = 0

    d = 0.0013
    m = 0.15

    arrx = []
    arry = []

    vx = v * math.cos(math.radians(angle))
    vy = v * math.sin(math.radians(angle))

    while True :
        arrx.append(x)
        arry.append(y)

        t = t + dt
        ax = -(d/m) * v * vx
        ay = g - (d/m) * v * vy
        vx = vx + (ax*dt)
        vy = vy + (ay*dt)
        y = y + (vy * dt)
        x = x + (vx * dt)
        v = math.sqrt(vx**2+vy**2)

        if y < 0:
            break
    return arrx,arry
    
    
arrx,arry = numeric_wHambatan(0,50,35)

plt.plot(arrx,arry)

import math
import matplotlib.pyplot as plt

def analitic_woHambatan(y,v,angle):
    dt = 0.01
    x = 0
    g = -9.8
    t = 0
    
    arrx = []
    arry = []

    vx = v * math.cos(math.radians(angle))
    vy = v * math.sin(math.radians(angle))

    while True :
        arrx.append(x)
        arry.append(y)

        t = t + dt
        x = x + (vx * dt)
        y = (0.5 * g * t**2) + (vy * t)

        if y < 0 :
            break
    return arrx,arry

arrx,arry = analitic_woHambatan(0,50,35)

plt.plot(arrx,arry)

import math

#analytic
def woHambatan_analytic():
    sudut = 35
    y = 0
    v = 50
    deltat = 0.01
    x = 0
    g = -9.8
    t = 0

    vx = v * math.cos(math.radians(sudut))
    vy = v * math.sin(math.radians(sudut))

    while True :
        print(t,x,y)
        t = t + deltat
        x = x + (vx * deltat)
        y = (0.5 * g * t**2) + (vy *t)
        
        if y < 0 :
            break

#numeric

def woHambatan_numeric():
    sudut = 35
    y = 0
    v = 50
    deltat = 0.01
    x = 0
    g = -9.8
    t = 0

    vx = v * math.cos(math.radians(sudut))
    vy = v * math.sin(math.radians(sudut))

    while True :
        print(t,x,y)
        t = t + deltat
        vy = vy + (g*deltat)
        x = x + (vx * deltat)
        y = y + (vy * deltat)
        
        if y < 0 :
            break

def wHambatan_numeric():
    y = 0
    v = 50
    sudut = 35
    deltat = 0.01
    x = 0
    g = -9.8
    t = 0

    d = 0.0013
    m = 0.15
    vx = v * math.cos(math.radians(sudut))
    vy = v * math.sin(math.radians(sudut))

    while True :
        print(t,x,y)

        t = t + deltat
        ax = -(d/m) * v * vx
        ay = g - (d/m) * v * vy
        vx = vx + (ax*deltat)
        vy = vy + (ay*deltat)
        y = y + (vy * deltat)
        x = x + (vx * deltat)
        v = math.sqrt(vx**2+vy**2)

        if y < 0:
            break

#wHambatan_analytic()
woHambatan_numeric()
#wHambatan_numeric()