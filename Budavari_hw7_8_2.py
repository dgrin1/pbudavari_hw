from math import sin
from numpy import array,arange
#from pylab import plot,xlabel,show
import matplotlib.pyplot as plt

def f(r,t):
#read in x and y positions of particle
    x = r[0]
    y = r[1]
    a = 1
    b= 0.5
    gamma = 0.5
    delta = 2
#compute derivatives using from the board
    fx = a*x-b*x*y
    fy = gamma*x*y -delta*y
#return the array of derivatives
    return array([fx,fy],float)

#set left and right initial and final times
i = 0.0
e = 30.0
#set a large number of steps
N = 1000
h = (e-i)/N

#create array of indepdendent variable
tpoints = arange(i,e,h)

#create empty lists of x and y variables
xpoints = []
ypoints = []

#initial conditions
#r is an array containing instantenous positions of particle
# x and y coordinates
r = array([2,2],float)

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
# plt.figure(1)
# plt.plot(tpoints,xpoints)
# plt.plot(tpoints,ypoints)
# plt.figure(2)
# plt.plot(xpoints,ypoints)

# plt.xlabel("theta")
# plt.ylabel("omega")
# plt.show()


plt.plot(tpoints,xpoints, label = 'rabbits')
plt.plot(tpoints,ypoints, label = 'foxes')
plt.title("Runge-Kutta method for Lotka-Volterra equations")
plt.xlabel("Time")
plt.ylabel("Population")
plt.legend(loc = 4)
plt.savefig("/Users/petra/OneDrive/Documents/PHYS304/pbudavari_hw/"+ str("8_2") + ".png")
plt.close()