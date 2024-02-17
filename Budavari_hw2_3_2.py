#Exercise 3.2 Curve plotting

from __future__ import division,print_function
from scipy import constants as sc
from numpy import loadtxt,array,dot,sqrt,cos,sin,linspace,log
import numpy as np
from math import pi, exp

import matplotlib.pyplot as plt
plt.ion()
plt.rcParams['backend']='TkAgg'
#plt.rcParams['text.usetex']='True'
plt.rcParams['font.family']='serif'
plt.rcParams['font.serif']='Times New Roman'

#(A) Deltoid Curve
#theta = range(0, 2*pi)
theta = np.arange (0, 2*pi, 0.1)

#create empty arrays
x=np.array([])
y=np.array([])

for i in theta:
    x = np.append(x, 2*cos(i)+cos(2*i))
    y = np.append(y, 2*sin(i) - sin(2*i))
#print(x,y)
#append new x and y values to arrays above

plt.plot(x,y, label = "deltoid curve")
plt.show()
plt.title("Deltoid Curve")
plt.xlabel("x")
plt.ylabel("y")
plt.legend(loc = 1)
plt.savefig("/Users/petra/OneDrive/Documents/PHYS304/HW/"+ str("DeltoidCurve") + ".png")
plt.close()

#(B)
theta2 = np.arange (0, 10*pi, 0.1)
#print(theta2)

#make r an array first
r=np.array([])

#new x and y arrays
x2=np.array([])
y2=np.array([])

#calculate rs for each theta in range
for k in theta2:
    r = np.append(r, k**2)
print(r)

#make sure r is the right length
n = len(r)
print(n)
print(len(theta2))

#use indices to loop through multiple arrays to calculate x and y
for j in range(n):
    rs = r[j]
    theta2s = theta2[j]
    x2 = np.append(x2, rs*cos(theta2s))
    y2= np.append(y2, rs*sin(theta2s))

print(x2,y2)

#Plot!
plt.plot(x2,y2, label = "polar converted to cartesian")
plt.show()
plt.title("Galilean spiral")
plt.xlabel("x")
plt.ylabel("y")
plt.legend(loc = 1)
plt.savefig("/Users/petra/OneDrive/Documents/PHYS304/HW/"+ str("GalileanSpiral") + ".png")
plt.close()


#(C)
r2=np.array([])
theta3 = np.arange (0, 24*pi, 0.1)
x3=np.array([])
y3=np.array([])

#same as in part B
for k in theta3:
    r2 = np.append(r2, exp(cos(k))- 2*cos(4*k) + (sin(k/12))**5)
#print(r2)

m = len(r2)
print(m)
print(len(theta3))

for f in range(m):
    r2s = r2[f]
    theta2s = theta3[f]
    x3 = np.append(x3, r2s*cos(theta2s))
    y3= np.append(y3, r2s*sin(theta2s))

#print(x3,y3)

plt.plot(x3,y3, label = "Fey's Function")
plt.show()
plt.title("Fey's Function")
plt.xlabel("x")
plt.ylabel("y")
plt.legend(loc = 1)
plt.savefig("/Users/petra/OneDrive/Documents/PHYS304/HW/"+ str("FeysFunc") + ".png")
plt.close()