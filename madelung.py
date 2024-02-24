import numpy as np
import math
import mpmath
import matplotlib.pyplot as plt

plt.ion()
plt.rcParams['backend']='TkAgg'
#plt.rcParams['text.usetex']='True'
plt.rcParams['font.family']='serif'
plt.rcParams['font.serif']='Times New Roman'


def Madelung(gridsize): #dimensins of lattice
    M = np.array([])  
    ijk = np.arange(-gridsize, gridsize+1,1) 
    # print(ijk) 
    for i in ijk:
        for j in ijk:
            for k in ijk:
                if ((ijk[k] != 0) or (ijk[j] != 0) or (ijk[i] != 0)):
                    
                    M = np.append(M, (-1.0)**(ijk[j]+ijk[k]+ijk[i]) / (math.sqrt(ijk[j]**2 + ijk[k]**2 + ijk[i]**2)))
                    
    sum = np.sum(M)
    return sum


# print(Madelung(10))


# # Compare to M constant where m,n >=1, odd


# M2 = 12*math.pi * np.sum(mpmath.sech((math.pi /2)*(math.sqrt(m**2 + n**2))^2))
def Madapprox(oddnum): #dimensins of lattice
    # oddnum = odd(x)
    M2 = np.array([])
    for n in range(1,oddnum,2):
        print(n) # make sure it's only odd
        for m in range(1, oddnum,2):
            M2 = np.append(M2,  (mpmath.sech((math.pi /2)*(math.sqrt(m**2 + n**2))))**2)
    sum = 12*math.pi * np.sum(M2)
    return sum
 


#Madelung constant for altered composition pattern where
# the distance between particles in the j direction is 10 times the orig. distance
# and the 2 times for the k direction
# and the particles in the j vector are of positive charge instead of negative
def Madnew(gridsize): #dimensins of lattice
    M = np.array([])  
    ijk = np.arange(-gridsize, gridsize+1,1) 
    # print(ijk) 
    for i in ijk:
        for j in ijk:
            for k in ijk:
                if ((ijk[k] != 0) or (ijk[j] != 0) or (ijk[i] != 0)):
                    
                    M = np.append(M, (-1.0)**(-ijk[j]+ijk[k]+ijk[i]) / (math.sqrt((10*ijk[j])**2 + (2*ijk[k])**2 + ijk[i]**2)))

    sum = np.sum(M)
    return sum


gridsize= np.arange(1, 20)

mad_vec = np.vectorize(Madelung)

plt.plot(gridsize, mad_vec(gridsize), label = "Madelung constant")
# plt.xlim(0, 150)
# plt.ylim(-20, 15)
plt.title("Madelung constant as a function of gridsize")
plt.xlabel("Gridsize")
plt.ylabel("Madelung constant")
plt.legend(loc = 1)
plt.savefig("/Users/petra/OneDrive/Documents/PHYS304/pbudavari_hw/"+ str("mad_const") + ".png")
plt.close()

approx_vec = np.vectorize(Madapprox)

#num=30
oddnum = 30
print(oddnum)
oddarray = np.arange(1, oddnum, 2)
print(oddarray)


plt.plot(oddarray, approx_vec(oddarray), label = "Madelung constant approximation")
# plt.xlim(0, 150)
# plt.ylim(-20, 15)
plt.title("Madelung constant Approximation using odd numbers")
plt.xlabel("numbers")
plt.ylabel("Calculated Madelung constant")
plt.legend(loc = 4)
plt.savefig("/Users/petra/OneDrive/Documents/PHYS304/pbudavari_hw/"+ str("mad_approx") + ".png")
plt.close()


# print(Madelung(10))

grid= np.arange(1, 20)

mnew_vec = np.vectorize(Madnew)

plt.plot(grid, mnew_vec(grid), label = "Madelung constant with altered variables")
# plt.xlim(0, 150)
# plt.ylim(-20, 15)
plt.title("Madelung constant as a function of gridsize with non-unifrom dimensions")
plt.xlabel("Gridsize")
plt.ylabel("Madelung constant")
plt.legend(loc = 1)
plt.savefig("/Users/petra/OneDrive/Documents/PHYS304/pbudavari_hw/"+ str("mad_new") + ".png")
plt.close()