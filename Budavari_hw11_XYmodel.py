#Petra Budavari 
#PHYS 304, Homework 11
#4/23

from random import random,randrange, choice
from math import exp, pi
from numpy import ones
import numpy as np
from pylab import plot,ylabel,show
import random

import math

import matplotlib.pyplot as plt
plt.ion()
plt.rcParams['backend']='TkAgg'
plt.rcParams['font.family']='serif'
plt.rcParams['font.serif']='Times New Roman'


T = 0.2
N = 1000
steps = 100000
J= 1 # interaction constant 

# Create a 2D array to store the quantum numbers
# n = np.random.randint(-1,2, size=(20,20))

n=ones([20,20])

for i in range(0,20):
    for j in range(0,20):
       n[i,j] = math.cos(random.randrange(0, 100)*0.01 *2*pi)
print(n)


n = np.pad(n, ((0,1), (0,1)), mode="constant")


print(n) #add zeros with right-most colum and new bottom column. 

# Main loop
eplot = []
E = 0

magnitudes = np.array([])

for k in range(steps):

    if k%5000==0:
        print(k)

    # Choose the particle and the move
    i = randrange(20)
    j = randrange(20)
    theta = random.randrange(0, 100)*0.01 *2*pi
    
    #make eold and enew and then actually calculate dE, if dE<0 then keep Enew flip oterwise flip back
    if  i<19 and j<19:
        Eold = n[i,j]* (n[i,j+1]+ n[i+1,j]+ n[i,j-1]+ n[i-1,j])

    elif i==19 and j<19:
        Eold = n[i,j]*(n[i,j+1]+ n[-1,j]+ n[i,j-1]+ n[i-1,j])

    elif j==19 and i<19:
        Eold = n[i,j]*(n[i,-1]+ n[i+1,j]+ n[i,j-1]+ n[i-1,j])
        
    elif j==19 and i==19:
        Eold = n[i,j]* (n[i,-1]+ n[-1,j]+ n[i,j-1]+ n[i-1,j])
 

    #make eold and enew and then actually calculate dE, if dE<0 then keep Enew flip oterwise flip back
    if  i<19 and j<19:
        Enew = math.cos(theta)*(n[i,j+1]+ n[i+1,j]+ n[i,j-1]+ n[i-1,j])

    elif i==19 and j<19:
        Enew = math.cos(theta)*(n[i,j+1]+ n[-1,j]+ n[i,j-1]+ n[i-1,j])

    elif j==19 and i<19:
        Enew = math.cos(theta)*(n[i,-1]+ n[i+1,j]+ n[i,j-1]+ n[i-1,j])
        
    elif j==19 and i==19:
        Enew = math.cos(theta)*(n[i,-1]+ n[-1,j]+ n[i,j-1]+ n[i-1,j])
    

    dE = Enew-Eold
    # Decide whether to accept the move

    if dE < 0:
        n[i,j] = math.cos(theta)
    else:
        if math.cos(theta)<exp(-dE/T):
            n[i,j] = math.cos(theta)
            E += dE
  

    eplot.append(E)
  


plt.plot(eplot)
plt.legend('energy')
plt.xlabel('Step')
plt.ylabel('Energy')
plt.title("Energy using Metropolis-style Simulation in XY model")
plt.savefig("/Users/petra/OneDrive/Documents/PHYS304/pbudavari_hw/"+ str("MCS_XYmodel") + ".png")
plt.close()

