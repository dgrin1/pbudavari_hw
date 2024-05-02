#Petra Budavari 
#PHYS 304, Homework 11
#4/23

from random import random,randrange, choice
from math import exp,pi
from numpy import ones
import numpy as np
from pylab import plot,ylabel,show
import matplotlib as mpl
from matplotlib.pyplot import matshow

from itertools import count
import matplotlib.animation as animation

import matplotlib.pyplot as plt
plt.ion()
plt.rcParams['backend']='TkAgg'
plt.rcParams['font.family']='serif'
plt.rcParams['font.serif']='Times New Roman'

T = 3
N = 1000
steps = 1000
J= 1 # interaction constant 

# Create a 2D array to store the quantum numbers
n=ones([20,20],int)

for i in range(0,20):
    for j in range(0,20):
        n[i,j] = choice([-1, 1])*n[i,j]

# n = random.choice([-1, 1])
# n = random.shuffle(n)
n = np.pad(n, ((0,1), (0,1)), mode="constant")


print(n) #add zeros with right-most colum and new bottom column. 

# Main loop
eplot = []
E = 0

magnitudes = np.array([])
narray = []

#Initializing subplots for animation
fig, ax = plt.subplots()

artists = []


for k in range(steps):

    if k%5000==0:
        print(k)

    # Choose the particle and the move
    i = randrange(20)
    j = randrange(20)
    
    dn=1
    #make eold and enew and then actually calculate dE, if dE<0 then keep Enew flip oterwise flip back
    if  i<19 and j<19:
        Eold = n[i,j]* (n[i,j+1]+ n[i+1,j]+ n[i,j-1]+ n[i-1,j])

    elif i==19 and j<19:
        Eold = n[i,j]*(n[i,j+1]+ n[-1,j]+ n[i,j-1]+ n[i-1,j])

    elif j==19 and i<19:
        Eold = n[i,j]*(n[i,-1]+ n[i+1,j]+ n[i,j-1]+ n[i-1,j])
        
    elif j==19 and i==19:
        Eold = n[i,j]* (n[i,-1]+ n[-1,j]+ n[i,j-1]+ n[i-1,j])

    dn=-1
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
        if random()<exp(-dE/T):

            n[i,j] = n[i,j]*-1
            E += Enew

    sum = np.sum(n)   
    magnitudes = np.append(magnitudes, sum)

    eplot.append(E)

    print(n[i,j])

#Run Metropolis algorithm
#(Stuff to initialize s and calculate initial energy)

    container = ax.imshow(n)
    artists.append([container])

# Out of the simulation loop, I plot my animation
ani = animation.ArtistAnimation(fig=fig,artists=artists,interval=10)
plt.show()
ani.save('ISINGanimation.mp4')
