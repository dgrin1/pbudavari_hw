#Petra Budavari 
#PHYS 304, Homework 11
#4/23

from random import random,randrange
from math import exp,pi
from numpy import ones
import numpy as np
from pylab import plot,ylabel,show

import matplotlib.pyplot as plt
plt.ion()
plt.rcParams['backend']='TkAgg'
plt.rcParams['font.family']='serif'
plt.rcParams['font.serif']='Times New Roman'


T = 10.0
N = 1000
steps = 1000000
J= 10 # interaction constant 

# Create a 2D array to store the quantum numbers
n = ones([20,20],int)
n = np.pad(n, ((0,1), (0,1)), mode="constant")
   
print(n) #add zeros with right-most colum and new bottom column. 

# Main loop
eplot = []
E = 0

for k in range(steps):

    # Choose the particle and the move
    i = randrange(20)
    j = randrange(20)

      # dn=1
    #make eold and enew and then actually calculate dE, if dE<0 then keep Enew flip oterwise flip back

    if random()<0.5:
        dn = 1
        if  i<=19 and j<=19:
            dE = n[i,j]* (n[i,j+1]+ n[i+1,j]+ n[i,j-1]+ n[i-1,j])

        elif i==0 and j<=19:
            dE = n[i,j]*(n[i,j+1]+ n[i+1,j]+ n[i,j-1]+ n[-1,j])

        elif j==0 and i<=19:
            dE = n[i,j]*(n[i,j+1]+ n[i+1,j]+ n[i,-1]+ n[i-1,j])
            
        elif j==0 and i==0:
            dE = n[i,j]* (n[i,j+1]+ n[i+1,j]+ n[i,-1]+ n[-1,j])
        

    # dn=-1
    #make eold and enew and then actually calculate dE, if dE<0 then keep Enew flip oterwise flip back
    else:
        dn = -1
        if  i<19 and j<19:
            dE = -1*n[i,j]* (n[i,j+1]+ n[i+1,j]+ n[i,j-1]+ n[i-1,j])

        elif i==19 and j<19:
            dE = -1*n[i,j]*(n[i,j+1]+ n[-1,j]+ n[i,j-1]+ n[i-1,j])

        elif j==19 and i<19:
            dE = -1*n[i,j]*(n[i,-1]+ n[i+1,j]+ n[i,j-1]+ n[i-1,j])
            
        elif j==19 and i==19:
            dE = -1*n[i,j]* (n[i,-1]+ n[-1,j]+ n[i,j-1]+ n[i-1,j])
    


    if dE < 0:
        n[i,j] = n[i,j]*-1
    else:
        if random()<exp(-dE/T):
            n[i,j] = n[i,j]*-1
            E += dE
  
    eplot.append(E)


print(n)
# Make the graph
# plot(eplot)
# ylabel("Energy")
# show()

plt.plot(eplot)
plt.legend('energy')
plt.xlabel('Step')
plt.ylabel('Energy')
plt.title("Energy using Monte-Carlo Simulation")
plt.savefig("/Users/petra/OneDrive/Documents/PHYS304/pbudavari_hw/"+ str("testising") + ".png")
plt.close()
