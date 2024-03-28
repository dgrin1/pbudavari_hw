import numpy as np
from math import sin, cos,sqrt
from numpy import array,arange
#from pylab import plot,xlabel,show
import matplotlib.pyplot as plt

def f(r,t):
#read in x and y positions of particle
    x = r[0]
    y = r[1]
    g=9.8
    l=0.1
    C=2
    Omega=9.63636
#compute derivatives using from the board
    fx = y
    fy = -(g/l)*sin(x)+C*cos(x)*sin(Omega*t)
#return the array of derivatives
    return array([fx,fy],float)

#set left and right initial and final times
a = 0.0
b = 1000.0
#set a large number of steps
N = 100000
h = (b-a)/N

#create array of indepdendent variable
tpoints = arange(a,b,h)

#create empty lists of x and y variables
xpoints = []
ypoints = []

#initial conditions
#r is an array containing instantenous positions of particle
# x and y coordinates
r = array([0,0],float)

#run a loop over all times
for t in tpoints:

#using x and y components of last step
#grow the x and y arrays
    xpoints.append(r[0])
    ypoints.append(r[1])
    
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
plt.plot(tpoints,xpoints, label = 'Theta as function of time in pendulum')
# plt.plot(tpoints,ypoints)
plt.title("Runge-Kutta method on driven pendulum at resonance")
plt.xlabel("time (seconds)")
plt.ylabel("theta (radians)")
plt.legend(loc = 4)
plt.savefig("/Users/petra/OneDrive/Documents/PHYS304/pbudavari_hw/"+ str("8_5b") + ".png")
plt.close()