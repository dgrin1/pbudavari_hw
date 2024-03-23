#Code relaxtion method for solving unsolvable systems of equations. 
#Petra Budavari
#3/30/2024

import numpy as np
import math
from math import exp
import matplotlib.pyplot as plt

#adjust Latex fonts for figures
plt.ion()
plt.rcParams['backend']='TkAgg'
plt.rcParams['font.family']='serif'
plt.rcParams['font.serif']='Times New Roman'



#actual value
# X=1-exp(-2*X)

#PART (A)

#let initial x be 1

def relax(c):
    x=1.0
    for k in range(40): #check iterations are enough
        x=1-exp(-c*x)
        # if x[k-1] - x[k] < 0.000001:
        return(x)

print(relax(2))

#PART (B)

relaxvec = np.vectorize(relax)

c=np.arange(0,3,0.01)

#Show percolation transition
plt.plot(relaxvec(c),c, label = 'x as a function of c')
plt.title("Relaxation method")
plt.xlabel("x")
plt.ylabel("c")
plt.legend(loc = 4)
plt.savefig("/Users/petra/OneDrive/Documents/PHYS304/pbudavari_hw/"+ str("relax") + ".png")
plt.close()





