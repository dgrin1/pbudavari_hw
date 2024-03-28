import numpy as np
from math import sin, cos,sqrt
from numpy import array,arange,linspace
#from pylab import plot,xlabel,show
import matplotlib.pyplot as plt

maxamps = np.array([])
for Omega in linspace(1, 20, 100):
    
    def f(r,t):
    #read in x and y positions of particle
        x = r[0]
        y = r[1]
        g=9.8
        l=0.1
        C=2
    #compute derivatives using from the board
        fx = y
        fy = -(g/l)*sin(x)+C*cos(x)*sin(Omega*t)
    #return the array of derivatives
        return array([fx,fy],float)

    #set left and right initial and final times
    a = 0.0
    b = 100.0
    #set a large number of steps
    N = 1000
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
    
        k1 = h*f(r,t)
        k2 = h*f(r+0.5*k1,t+0.5*h)
        k3 = h*f(r+0.5*k2,t+0.5*h)
        k4 = h*f(r+k3,t+h)
        r += (k1+2*k2+2*k3+k4)/6
        
    max = np.max(xpoints)
    maxamps = np.append(maxamps, max)

print(maxamps)

omega=np.linspace(1,20,100)

omega_max = omega[np.argmax(maxamps)]
print(omega_max)

#plt.ion()
plt.plot(omega,maxamps, label = 'Max amplitude')
# plt.plot(tpoints,ypoints)
plt.title("Max amplitude as function of driving frequency")
plt.xlabel("Driving freq")
plt.ylabel("Theta")
plt.legend(loc = 1)
plt.savefig("/Users/petra/OneDrive/Documents/PHYS304/pbudavari_hw/"+ str("resonancecheck") + ".png")
plt.close()