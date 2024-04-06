#Newman Exercise 8.10d
#Petra Budavari
#4/2/2024


import numpy as np
from math import sin,cos,sqrt
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
    R = sqrt(x**2+y**2)
#compute derivatives using from the board
    fx = n
    fn = -G*M*(x/(R**3))
    fy = m
    fm = -G*M*(y/(R**3))
#return the array of derivatives
    return array([fx,fn,fy,fm],float)

#set left and right initial and final times
a = 0.0
b = 1.6e9
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
r = array([4e12,0,0,500],float)


#run a loop over all times
t=0.00001
while t < b:
#using x and y components of last step
#grow the x and y arrays

    r1 = np.copy(r)
    r2 = np.copy(r)


#steps that are themselves vectors,
#k1 and k2 and k3 and k4 are steps that tell you how to
# step in x and y
# k1=[1,2]    
    k1 = h*f(r1,t)
    k2 = h*f(r1+0.5*k1,t+0.5*h)
    k3 = h*f(r1+0.5*k2,t+0.5*h)
    k4 = h*f(r1+k3,t+h)
    r1 += (k1+2*k2+2*k3+k4)/6
    k1 = h*f(r1,t)
    k2 = h*f(r1+0.5*k1,t+0.5*h)
    k3 = h*f(r1+0.5*k2,t+0.5*h)
    k4 = h*f(r1+k3,t+h)
    r1 += (k1+2*k2+2*k3+k4)/6

    k1 = 2*h*f(r2,t)
    k2 = 2*h*f(r2+0.5*k1,t+0.5*2*h)
    k3 = 2*h*f(r2+0.5*k2,t+0.5*2*h)
    k4 = 2*h*f(r2+k3,t+(h*2))
    r2 += (k1+2*k2+2*k3+k4)/6

    x1 = r1[0]
    x2 = r2[0]
    y1 = r1[2]
    y2 = r2[2]

    ex = (1/30)*(x1-x2)
    ey = (1/30)*(y1-y2)

    e = sqrt(ex**2+(ey**2)) #error
    gamma = 3.17098e-5 #meters per second target accuracy
    # p = (h*gamma)/e #if p<1 then accuracy is poorer than target
    p = gamma*h/np.abs(ex)
    
    if p>=1:
        r=r1
        t+=(2*h)
        h=h*min(p**(1.4), 1.001)
        xpoints.append(r[0])
        npoints.append(r[1])
        ypoints.append(r[2])
        mpoints.append(r[3])
    else:
        h=h*p**(1/4)
        # k1 = h*f(r,t)
        # k2 = h*f(r+0.5*k1,t+0.5*h)
        # k3 = h*f(r+0.5*k2,t+0.5*h)
        # k4 = h*f(r+k3,t+h)
        # r += (k1+2*k2+2*k3+k4)/6

        # xpoints.append(r[0])
        # ypoints.append(r[2])
        continue
    

#plt.ion()
plt.scatter(xpoints,ypoints, label = 'path', s=0.5)
# plt.plot(tpoints,ypoints)
plt.title("Trajectory of Comet")
plt.xlabel("x position")
plt.ylabel("y position")
plt.legend(loc = 4)
plt.savefig("/Users/petra/OneDrive/Documents/PHYS304/pbudavari_hw/"+ str("8_10d") + ".png")
plt.close()