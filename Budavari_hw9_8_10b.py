#Newman Exercise 8.10b
#Petra Budavari
#4/2/2024

import numpy as np
from math import sin, cos,sqrt
from numpy import array,arange
#from pylab import plot,xlabel,show
import matplotlib.pyplot as plt

plt.ion()
plt.rcParams['backend']='TkAgg'
plt.rcParams['font.family']='serif'
plt.rcParams['font.serif']='Times New Roman'



def f(r,t):
#read in x and y positions of particle
    x = r[0]
    n = r[1]
    y = r[2]
    m = r[3]
    G =6.674E-11
    M = 1.989E30
    R = (x**2+y**2)**(0.5)
#compute derivatives using from the board
    fx = n
    fn = -G*M*(x/(R**3))
    fy = m
    fm = -G*M*(y/(R**3))
#return the array of derivatives
    return array([fx,fn,fy,fm],float)

#set left and right initial and final times
a = 0.0
b = 2000000000.0
#set a large number of steps
N = 1000000
h = (b-a)/N

#create array of indepdendent variable
tpoints = arange(a,b,h)

#create empty lists of x and y variables
xpoints = []
npoints = []
ypoints = []
mpoints = []

#initial conditions
#r is an array containing instantenous positions of particle
# x and y coordinates
r = array([4000000000000,0,0,500],float)

#run a loop over all times
for t in tpoints:

#using x and y components of last step
#grow the x and y arrays
    xpoints.append(r[0])
    npoints.append(r[1])
    ypoints.append(r[2])
    mpoints.append(r[3])
    
#steps that are themselves vectors,
#k1 and k2 and k3 and k4 are steps that tell you how to
# step in x and y
# k1=[1,2]    
    k1 = h*f(r,t)
    k2 = h*f(r+0.5*k1,t+0.5*h)
    k3 = h*f(r+0.5*k2,t+0.5*h)
    k4 = h*f(r+k3,t+h)
    r += (k1+2*k2+2*k3+k4)/6




#plt.ion()
plt.plot(xpoints,ypoints, label = 'path')
# plt.plot(tpoints,ypoints)
plt.title("Trajectory of Comet")
plt.xlabel("x position")
plt.ylabel("y position")
plt.legend(loc = 4)
plt.savefig("/Users/petra/OneDrive/Documents/PHYS304/pbudavari_hw/"+ str("8_10b") + ".png")
plt.close()