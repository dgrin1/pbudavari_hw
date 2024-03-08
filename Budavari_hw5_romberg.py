#Create Romberg fucntion
#Petra Budavari
#3/7/2024

import numpy as np
import math 
import matplotlib.pyplot as plt


#trapezoidal
def romberg(a,b,N):

    #some function f(x) inside integral
    def f(x):
        return (math.sin(x))
    
    I= np.array([]) #create array for trapezoidal results as N doubles
    x = np.arange(1,6) #the number of Ns we want to use
    #create array where N doubles each time
    N_array = np.array([])

#trapezoidal function
    for i in x:
        sum =np.array([])
        ndoubles = 2**(i)*N
        h = (b-a)/ndoubles
        N_array = np.append(N_array, ndoubles)
        for k in range(1,ndoubles): #first summation
            f1 = f(a+k*h)
            sum = np.append(sum, f1)
            sum1 = np.sum(sum)   
        #plug into final equation
        func = h*((1/2)*f(a)+(1/2)*f(b)+sum1)
        I = np.append(I, func)
    print(I)
    #now we have an array with trapezoidal results which will serve as Ri,1 s

    R= np.zeros((5,5)) #create an empty 5 by 5 matrix
    for j in range(1,len(I)):
        R[j,1] = I[j-1] #make the first column the trapezoidal values

    for m in range(2,len(I)): #nested for loops for indexing matrix
        for n in range(1,m): 
            R[m,n+1] = R[m,n] + (1/(4^n -1))*(R[m,n] - R[m-1,n]) #Equation 5.51 to calculate next R
    
    return R[m,n] #final Rn,n
    
    
print(romberg(0,2*math.pi,5))
    
            


