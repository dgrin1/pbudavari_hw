#Petra Budavari 
#PHYS 304, Homework 11
#4/23

from random import random,randrange, choice
from math import exp,pi
from numpy import ones
import numpy as np
from pylab import plot,ylabel,show


import matplotlib.pyplot as plt
plt.ion()
plt.rcParams['backend']='TkAgg'
plt.rcParams['font.family']='serif'
plt.rcParams['font.serif']='Times New Roman'


T = 1
N = 1000
steps = 100000
J= 1 # interaction constant 

# Create a 2D array to store the quantum numbers
# n = np.random.randint(-1,2, size=(20,20))

n=ones([20,20],int)

for i in range(0,20):
    for j in range(0,20):
        n[i,j] = choice([-1, 1])

n = np.pad(n, ((1,1), (1,1)), mode="constant")


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
    
    
    # dn=1
    #make eold and enew and then actually calculate dE, if dE<0 then keep Enew flip oterwise flip back
    if  i<19 and j<19:
        Eold = n[i,j]* (n[i,j+1]+ n[i+1,j]+ n[i,j-1]+ n[i-1,j])

    elif i==19 and j<19:
        Eold = n[i,j]*(n[i,j+1]+ n[-1,j]+ n[i,j-1]+ n[i-1,j])

    elif j==19 and i<19:
        Eold = n[i,j]*(n[i,-1]+ n[i+1,j]+ n[i,j-1]+ n[i-1,j])
        
    elif j==19 and i==19:
        Eold = n[i,j]* (n[i,-1]+ n[-1,j]+ n[i,j-1]+ n[i-1,j])
    

    # dn=-1
    #make eold and enew and then actually calculate dE, if dE<0 then keep Enew flip oterwise flip back
    if  i<19 and j<19:
        Enew = -1*n[i,j]* (n[i,j+1]+ n[i+1,j]+ n[i,j-1]+ n[i-1,j])

    elif i==19 and j<19:
        Enew = -1*n[i,j]*(n[i,j+1]+ n[-1,j]+ n[i,j-1]+ n[i-1,j])

    elif j==19 and i<19:
        Enew = -1*n[i,j]*(n[i,-1]+ n[i+1,j]+ n[i,j-1]+ n[i-1,j])
        
    elif j==19 and i==19:
        Enew = -1*n[i,j]* (n[i,-1]+ n[-1,j]+ n[i,j-1]+ n[i-1,j])
    

    dE = Eold-Enew
    # Decide whether to accept the move

    if dE < 0:
        n[i,j] = n[i,j]*-1
    else:
        if random()<exp(-dE/T):
            n[i,j] = n[i,j]*-1
            E += dE

    sum = np.sum(n)   
    magnitudes = np.append(magnitudes, sum)

    eplot.append(E)

# Make the graph
# plot(eplot)
# ylabel("Energy")
# show()

plt.plot(magnitudes)
plt.legend('magnetizaytion')
plt.xlabel('Step')
plt.ylabel('Magnetization')
plt.title("Magnetization over steps")
plt.savefig("/Users/petra/OneDrive/Documents/PHYS304/pbudavari_hw/"+ str("MCS_c") + ".png")
plt.close()
