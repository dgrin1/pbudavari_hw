#Petra Budavari
#3/21/2024

import numpy as np
import numpy.linalg as la
import math
from math import exp, pi
import matplotlib.pyplot as plt

#adjust Latex fonts for figures
plt.ion()
plt.rcParams['backend']='TkAgg'
plt.rcParams['font.family']='serif'
plt.rcParams['font.serif']='Times New Roman'


def H(m,n):
    L=5.0E-10 #units in atomic lengths
    a=1.60218e-18 #joules
    # c=299792458 #m/s
    #M = 0.5109989461E6 #in ev
    M = 9.1094E-31
    # hbar = 	6.5821220E-16 # in ev
    hbar = 1.054571817E-34 #joules
    if n==m:
        ans1 =((hbar**2)/(2*M))*(((pi**2)*(n**2))/((L)**2))+(a/2)
        return ans1
    if n!=m and m%2==n%2:
        return 0
    else:
        ans2 =(2/L)*(a/L)*(-((2*L)/pi)**2)*((m*n)/((m**2 -n**2)**2))
        return ans2 
    
print(H(1,1))


#PART (C)

matrix1 = np.zeros((10,10))
print(matrix1)

for m in range(0,10):
    for n in range(0,10):
        matrix1[m,n] = H(m+1,n+1)
print("matrix")
print(matrix1)

eigenvalues1, egienvectors =la.eigh((matrix1))
print("eigenvalues for 10")
print(eigenvalues1/1.6022e-19)


#PART (D)

matrix2 = np.zeros((100,100))

for m in range(0,100):
    for n in range(0,100):
        matrix2[m,n] = H(n+1,m+1)
print("eigenvalues for 100")
eigenvalues2, egienvectors =la.eigh((matrix2))
print(eigenvalues2/1.6022e-19)

#PART(E)
def prob(x): #d is dimension of matrix
    d=20
    matrix = np.zeros((d,d))
    for m in range(0,d):
        for n in range(0,d):
            matrix[m,n] = H(n+1,m+1)
    values, vectors =la.eigh(matrix)
    print("eigenvalues for 50")
    print(values/1.6022e-19)

    def sinf(x,j):
        return math.sin((pi*j*x)/5.0E-10)

    wave = np.array([])

    for i in range(0,20):
        wave = np.append(wave, np.sum((vectors[:,i])*sinf(x,i)))
    
    print('probability densities for 3 eigen vectors')
    prob1 = np.abs((wave[1])**2)
    prob2 = np.abs((wave[2])**2)
    prob3 = np.abs((wave[3])**2)

    return prob1, prob2, prob3

print(prob(5))

probvec = np.vectorize(prob)


L=5.0E-10
x=np.linspace(0,L,50)
# d = (np.ones(50))*50

prob1, prob2, prob3 =probvec((x))

#Show percolation transition
plt.plot(x, prob1,label = 'ground state')
plt.plot(x, prob2,label = '1st excited state')
plt.plot(x, prob3,label = '2nd excited state')
plt.title("Probability Densities for first 3 states")
plt.xlabel("x")
plt.ylabel("pobability density")
plt.legend(loc = 4)
plt.savefig("/Users/petra/OneDrive/Documents/PHYS304/pbudavari_hw/"+ str("probden") + ".png")
plt.close()







