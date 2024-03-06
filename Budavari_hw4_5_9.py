#Exercise 5.9 in Newman
#Petra Budavari

import numpy as np
import math 
import matplotlib.pyplot as plt
from gaussxw import gaussxwab

#adjust Latex fonts for figures
plt.ion()
plt.rcParams['backend']='TkAgg'
plt.rcParams['font.family']='serif'
plt.rcParams['font.serif']='Times New Roman'


#(A)
def f(x):
    return (x**4 *np.exp(x))/((np.exp(x)-1)**2)

def cv(T):
    p = 6.022*10**28
    V=1000
    theta = 428 #Debye temp
    kb = 1.380649*10**(-23) #Boltzman constant
    N =50
    a = 0
    b = theta/T
    #from Newman p.171
    x,w = gaussxwab(N,a,b) #make sure that this file is in same folder as your code
    s=0.0
    for k in range(N):
        s+=w[k]*f(x[k])
    #final Cv equation
    result = (9*V*p*kb*(T/theta)**3)*s
    return result


#(B)

T = np.arange(5, 501)

cv_vec = np.vectorize(cv)

#plot over temperature array
plt.plot(T, cv_vec(T), label = 'heat capacity')
plt.title("Heat capacity as function of temperature")
plt.xlabel("Temp (K)")
plt.ylabel("Heat capacity")
plt.legend(loc = 4)
plt.savefig("/Users/petra/OneDrive/Documents/PHYS304/pbudavari_hw/"+ str("heatcapacity") + ".png")
plt.close()



