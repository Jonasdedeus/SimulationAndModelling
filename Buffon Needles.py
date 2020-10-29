#!/usr/bin/env python
# coding: utf-8

# In[1]:


'''
From Statistical Mechanics by Werner Krauth

Buffon's Needle Experiment
n = number of needles
r = number of trials
a = length of needle
b = distance between cracks
theta = angle needle makes to crack
rcenter = center of needles on floor
0  < theta < pi/2
0 < xcenter < b/2

nhits <===  number of hits of needle centered at x, with orientation theta
nhits = 1 if x < a/2 and abs(theta) < arcos(x/(a/2))
      = 0 otherwise
'''
import random
import math
#Jonas de Deus Guteres
#1301183615
def buffon(n,r,a,b):
    data=[]
    print ('Buffon Needle Experiment (Google it) ') 
    print ('Runs       Number Hits  estimate of pi')
    for jj in range(r):
        nhits = 0
        for ii in range(n):
            xcent = random.uniform(0,b/2.0)
            theta = random.uniform(0,math.pi/2)
            xtip  = xcent - (a/2.0)*math.cos(theta)  #use of cosine not historically accurate
            if xtip < 0 :
                nhits += 1
        c = 2.0*a*n
        d = b*nhits
        print (str(jj)+'    '+str(nhits)+'    '+str(c/d))
        data.append([jj,nhits])
    return data
        

r=5
n=4000
a = 2  #needle 2 inches
b = 2  #cracks 2 inch spacing

hits= buffon(n,r,a,b)    


# In[ ]:




