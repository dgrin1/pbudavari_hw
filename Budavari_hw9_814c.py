#Newman Exercise 8.14c
#Petra Budavari
#4/3/2024

#Modify 'squarewell.py' from Newman Example 8.9

from numpy import array,arange
import numpy as np
import matplotlib.pyplot as plt
import math 

plt.ion()
plt.rcParams['backend']='TkAgg'
plt.rcParams['font.family']='serif'
plt.rcParams['font.serif']='Times New Roman'


# Constants
m = 9.1094e-31     # Mass of electron
hbar = 1.0546e-34  # Planck's constant over 2*pi
e = 1.6022e-19     # Electron charge
L = 5.2918e-11     # Bohr radius
N = 1000
h = L/N
a = 1E-11 #m
Vo = 50*e #eV


# Potential function
def V(x):
    return Vo*x**4/a**4

def f(r,x,E):
    psi = r[0]
    phi = r[1]
    fpsi = phi
    fphi = (2*m/hbar**2)*(V(x)-E)*psi
    return array([fpsi,fphi],float)

# Calculate the wavefunction for a particular energy
#vaue of the wave function Psi(L)

def g(wavefunction):
    return np.abs(wavefunction)**2

#create a function 
def simpson(g): #make two input variabes (x,N)
    sum1 =np.array([]) #create arrays to loop through for summations 
    sum2 = np.array([])
    N=50
    # A=-5*a
    A=0
    B=5*a
    # h = (B-A)/N
    for k in range(1,N//2): #first summation
        f = g((A+(2*k-1)*h))
        sum1 = np.append(sum1, f)
        sumfirst = np.sum(sum1)
    for k in range(1,(N//2)-1): #second summation
        s = g((A+2*k*h))
        sum2 = np.append(sum2, s)
        sumsecond = np.sum(sum2)
    #add all components into Simpsons
    simpsons = (h/3)*((g(A)) +g(B) +(4*sumfirst)+(2*sumsecond))
    return simpsons*2


def solve(E):
    psi = 0.0
    phi = 1.0
    r = array([psi,phi],float)
    wavefuncs=np.array([])

    for x in arange(-5*a,5*a, h):
        wavefuncs=np.append(wavefuncs, r[0])
        k1 = h*f(r,x,E)
        k2 = h*f(r+0.5*k1,x+0.5*h,E)
        k3 = h*f(r+0.5*k2,x+0.5*h,E)
        k4 = h*f(r+k3,x+h,E)
        r += (k1+2*k2+2*k3+k4)/6
        
    return r[0], wavefuncs


# Main program to find the energy using the secant method
E11 = 250*e
E21 = 350*e
psi4 = solve(E11)[0]
print(psi4)
target = e/1000

while abs(E11-E21)>target:
    psi1,psi4 = psi4,solve(E21)[0]
    E11,E21 = E21,E21-psi4*(E21-E11)/(psi4-psi1)
print("E =",E21/e,"eV")
ground = E21/e


E12 = 290*e
E22 = 390*e
psi2 = solve(E12)[0]
print(psi2)
target = e/1000
while abs(E12-E22)>target:
    psi1,psi2 = psi2,solve(E22)[0]
    E12,E22 = E22,E22-psi2*(E22-E12)/(psi2-psi1)
print("E =",E22/e,"eV")
first = E22/e


E13 = 280*e
E23 = 380*e
psi3 = solve(E13)[0]
print(psi3)
target = e/1000
while abs(E13-E23)>target:
    psi1,psi3 = psi3,solve(E23)[0]
    E13,E23 = E23,E23-psi3*(E23-E13)/(psi3-psi1)
print("E =",E23/e,"eV")
second = E23/e

normalize = simpson(g)
normalg = solve(E21)[1]/math.sqrt(normalize)
normal1 = solve(E22)[1]/math.sqrt(normalize)
normal2 = solve(E23)[1]/math.sqrt(normalize)
x=np.arange(-5*a, 5*a, h)


plt.plot(x,normalg, label = 'ground state')
plt.plot(x,normal1, label = '1st energy state')
plt.plot(x,normal2, label = '2nd energy state')
# plt.plot(tpoints,ypoints)
plt.title("Normalized energy states")
plt.xlabel("x")
plt.ylabel("Energy")
plt.legend(loc = 2)
plt.savefig("/Users/petra/OneDrive/Documents/PHYS304/pbudavari_hw/"+ str("8_14c") + ".png")
plt.close()

