#Exercise 5.10 in Newman
#Petra Budavari
#3/7/2024

import numpy as np
import math 
import matplotlib.pyplot as plt
from gaussxw import gaussxwab


#adjust Latex fonts for figures
plt.ion()
plt.rcParams['backend']='TkAgg'
plt.rcParams['font.family']='serif'
plt.rcParams['font.serif']='Times New Roman'

#Do PART (A) by hand

#PART (B)
def period(a):
    V=a**4
    m=1
    N=20
    A=0 #integral start
    B=a #integral end

    def f(x): #function within the integral - in this case V(x) = x^4
        return 1/(math.sqrt(V-x**4))

    #from Newman p.171 Use gaussian to calculate integral 
    x,w = gaussxwab(N,A,B) #make sure that this file is in same folder as your code
    s=0.0
    for k in range(N):
        s+=w[k]*f(x[k])

    #final period equation
    result = math.sqrt(8*m) *s
    return result

#create array of amps from 0-2
a = np.arange(0.01, 2.01, 0.01)

T_vec = np.vectorize(period)

plt.plot(a, T_vec(a), label = 'Period (T)')
plt.title("The change in period over amplitude in anharmonic oscillator")
plt.xlabel("Amplitude")
plt.ylabel("Period")
plt.legend(loc = 1)
plt.savefig("/Users/petra/OneDrive/Documents/PHYS304/pbudavari_hw/"+ str("period") + ".png")
plt.close()

