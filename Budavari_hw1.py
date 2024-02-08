# Exercise 2.2 from the textbook
from math import pi

#(a)
G = 6.67e-11
M = 5.97e24
print(type(M))
R = 6371
T = float(input("How long should the satellite's orbit be in seconds?"))
# h is altitude in meters
h = ((G*M*(T**2))/(4*(pi**2)))**(1./3.) - R
print(h)


#Exercise 2.5
m = 9.11e-31
E = 10 #kinetic energy in eV
V = 9 #potential step of heigh in eV
hbar = 6.62607015e-34
k1 = (2*m*E)**(0.5)/hbar
k2 = (2*m*(E-V))**(0.5)/hbar
T2 = (4*k1*k2)/(k1+k2)**2 #equation for transmision
R2 = ((k1-k2)/(k1+k2))**2 #equation for reflection
#print answers
print(T2)
print(R2)
print(T2+R2)



