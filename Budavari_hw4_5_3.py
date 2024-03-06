#Exercise 5.3 in Newman
#Petra Budavari

import numpy as np
import math 
import matplotlib.pyplot as plt

#adjust Latex fonts for figures
plt.ion()
plt.rcParams['backend']='TkAgg'
plt.rcParams['font.family']='serif'
plt.rcParams['font.serif']='Times New Roman'

#create a function 
def E(x): #make two input variabes (x,N)
    sum1 =np.array([]) #create arrays to loop through for summations 
    sum2 = np.array([])
    N=50
    a=0
    b=x
    h = (b-a)/N
    for k in range(1,N//2): #first summation
        f = (np.exp(-(a+(2*k-1)*h)**2))
        sum1 = np.append(sum1, f)
        sumfirst = np.sum(sum1)


    for k in range(1,(N//2) -1): #second summation
        s = (np.exp(-(a+2*k*h)**2))
        sum2 = np.append(sum2, s)
        sumsecond = np.sum(sum2)
    
#add all components into Simpsons
    simpsons = (h/3)*((math.exp(-a**2) + math.exp(-b**2)+(4*sumfirst)+(2*sumsecond)))
    return simpsons


# part (B)
step=1000
#create a vector input 
x1 = np.arange(0,3,0.1)
size = len(x1)
N_array = np.ones(size)*step # you can ignore this

funcvec = np.vectorize(E) #vectorize so it can accept x array

plt.plot(x1, funcvec(x1),label = 'E(x) = integral of e^(-t)^2 from 0 to 3')

# plt.xlim(0, 150)
# plt.ylim(-20, 15)
plt.title("Using Simpsons to calculate E(x)")
plt.xlabel("x")
plt.ylabel("E(x)")
plt.legend(loc = 4)
plt.savefig("/Users/petra/OneDrive/Documents/PHYS304/pbudavari_hw/"+ str("Simpsons_v2") + ".png")
plt.close()
 

#error approximation for Simpson's rule- EQ 5.24 in Newman
def error(N): # make it a function of # of steps
    a=0
    b=3
     #this is an array of N
    h = (b-a)/N
    # use equation 5.24 from textbook for Simpson error
    f = ((h**4)/90)*(((-(8*a**2 -12*a))*np.exp(-(a**2)))+ ((8*b**2 +12*b)*np.exp(-(b**2))))

    return f

N = 15
n = np.arange(1,N+1)
print(n)
length = len(n)

x2 = np.arange(0,length)#ignore

#vectorize 
errvec = np.vectorize(error)

#plot error over # of steps (N)
plt.plot(n, errvec(n), label = 'Error as N increases')

plt.title("Simpson error")
plt.xlabel("N (number of steps)")
plt.ylabel("Total error")
plt.legend(loc = 1)
plt.savefig("/Users/petra/OneDrive/Documents/PHYS304/pbudavari_hw/"+ str("simpson_error") + ".png")
plt.close()