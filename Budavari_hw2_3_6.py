#Exercise 3.6

from __future__ import division,print_function
from scipy import constants as sc
from numpy import loadtxt,array,dot,sqrt,cos,sin,linspace,log

import numpy as np
from math import pi

import matplotlib.pyplot as plt
plt.ion()
plt.rcParams['backend']='TkAgg'
#plt.rcParams['text.usetex']='True'
plt.rcParams['font.family']='serif'
plt.rcParams['font.serif']='Times New Roman'

#logistic map interations 

#create an array of r for the range asked for
r = np.arange(1,4,0.01)
print(len(r))

#x = 1/2
xnext = np.array([]) #empty x array
xnext = np.append(xnext,.5) #starting x value is 1/2

# the 1000 iteration result of r and x 
finalr = np.array([])
finalx = np.array([])

for k in r: # loop through r array
    rarray=np.ones(1000)*k
    xnext = np.array([])
    xnext = np.append(xnext,.5) #restart xnext
    for i in range(0,2000): #nested for loop to loop through 2000 iterations for each r value
        x = xnext[i]
        xnext = np.append(xnext, k * (x*(1 - x)))
    finalr = np.append(finalr, rarray) #create array of 
    finalx = np.append(finalx, xnext[1000:2000]) # only take the second 1000 iterations
    print(k)

#plot!
plt.figure().set_figwidth(8)  
plt.scatter(finalr, finalx, s=6, label = "Fig Tree")
plt.show()
plt.title("Feigenbaum Tree Plot")
plt.xlabel("r")
plt.ylabel("x")
plt.legend(loc = 2)
plt.savefig("/Users/petra/OneDrive/Documents/PHYS304/HW/"+ str("Feigenbaum") + ".png")



