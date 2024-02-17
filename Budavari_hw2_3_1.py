#exercise 3.1 Plotting experimental data in book

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


data=loadtxt("sunspots.txt", float)

#(a) plot all data
month = data[:,0]
sunspot = data[:,1]

plt.plot(month,sunspot, label = "sunspots")
plt.show()
plt.title("Sunspots as fucntion of time")
plt.xlabel("Month")
plt.ylabel("Sunspot number")
plt.legend(loc = 1)
plt.savefig("/Users/petra/OneDrive/Documents/PHYS304/HW/"+ str("Sunspots as function of time") + ".png")
plt.close()

#(b) only first 1000 data points
month2 = data[:1000,0]
sunspot2 = data[:1000,1]

plt.plot(month2, sunspot2, label = "first 1000 sunspots")
plt.title("First 1000 Sunspots as fucntion of time")
plt.xlabel("Month")
plt.ylabel("Sunspot number")
plt.legend(loc = 1)
plt.show()
plt.savefig("/Users/petra/OneDrive/Documents/PHYS304/HW/"+ str("Thousand sunspots as function of time") + ".png")
plt.close()



#(c) running 

r = 5

l =len(sunspot)
print(l)

l2 =np.array([])

for k in range(l):
    l2 = np.append(l2, k)
print(l2)

y=np.array([])

#create for loop for running average
for i in range(l):
    length = l2[i]
    sunspots = sunspot[i]
    if length < 5: # is there is not enough
        fromIndex2 = i
        toIndex2 = i+5
        avg2 = np.sum(sunspot[fromIndex2:toIndex2])
        y = np.append(y, (1/(2*r +1))*(avg2))
    else:
        fromIndex = i-5
        toIndex = i+5
        avg = np.sum(sunspot[fromIndex:toIndex])
        y = np.append(y, (1/(2*r +1))*(avg))

#Plot!

plt.plot(month, y, label = "running average")
plt.title("Running average")
plt.xlabel("Month")
plt.ylabel("Sunspot number")
plt.legend(loc = 1)
plt.show()
plt.savefig("/Users/petra/OneDrive/Documents/PHYS304/HW/"+ str("Running average") + ".png")
plt.close()



plt.plot(month,sunspot, label = "sunspots")
plt.plot(month, y, label = "running average")
plt.show()
plt.title("Sunspots as fucntion of time")
plt.xlabel("Month")
plt.ylabel("Sunspot number")
plt.legend(loc = 1)
plt.savefig("/Users/petra/OneDrive/Documents/PHYS304/HW/"+ str("Original and Running Average Overlapped") + ".png")
plt.close()



y2 =np.array([])
for i in range(0,1000):
    length = l2[i]
    sunspots = sunspot[i]
    if length < 5:
        fromIndex2 = i
        toIndex2 = i+5
        avg2 = np.sum(sunspot[fromIndex2:toIndex2])
        y2 = np.append(y2, (1/(2*r +1))*(avg2))
    else:
        fromIndex = i-5
        toIndex = i+5
        avg = np.sum(sunspot[fromIndex:toIndex])
        y2 = np.append(y2, (1/(2*r +1))*(avg))

        
plt.plot(month2,sunspot2, label = "sunspots")
plt.plot(month2, y2, label = "running average")
plt.show()
plt.title("Sunspots as fucntion of time")
plt.xlabel("Month")
plt.ylabel("Sunspot number")
plt.legend(loc = 1)
plt.savefig("/Users/petra/OneDrive/Documents/PHYS304/HW/"+ str(" Thousand Original and Running Average Overlapped") + ".png")
plt.close()