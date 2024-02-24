import numpy as np
import math
import matplotlib.pyplot as plt
plt.ion()
plt.rcParams['backend']='TkAgg'
#plt.rcParams['text.usetex']='True'
plt.rcParams['font.family']='serif'
plt.rcParams['font.serif']='Times New Roman'


def psin(x):
#take arg mod 2pi
	x=x%(2.e0*np.pi)
#initialize iterator and sum
	i = 0
	s,sold = 0.e0,0.e0
#Keep at most 10000 terms in the Taylor series
	for i in range(10000):
		sold=s
		s+= float((((-1)**i) * (x**((2*i) + 1))))/float(math.factorial(((2*i) + 1)))

#If converged to machine precision then break out of loop
		if sold==s: break
	return s

psin_vec = np.vectorize(psin)



# my cos function
def pcos(x):
#take arg mod 2pi
	x=x%(2.e0*np.pi)
#initialize iterator and sum
	i = 0
	s,sold = 0.e0,0.e0

#Keep at most 10000 terms in the Taylor series
	for i in range(10000):
		sold=s
		s+= float((((-1)**i) * (x**((2*i)))))/float(math.factorial((2*i)))
#If converged to machine precision then break out of loop
		if sold==s: break
	return s
#vectorize for x arrays
pcos_vec = np.vectorize(pcos)

# my tan function
def ptan(x):
    return psin(x)/pcos(x)
#vectorize for x arrays
ptan_vec = np.vectorize(ptan)


x = np.arange(0, 1000)
print(x)

# Use if x is an array
print(psin_vec(x))
print(pcos_vec(x))
print(ptan_vec(x))

# Use if x is one element
# print(psin(x))
# print(pcos(x))
# print(ptan(x))

#Plot them!
plt.plot(x,psin_vec(x), label = "sin(x)")
plt.plot(x,pcos_vec(x), label = "cos(x)")
plt.plot(x,ptan_vec(x), label = "tan(x)")
plt.xlim(0, 150)
plt.ylim(-20, 15)
plt.title("Trig Functions")
plt.xlabel("x")
plt.ylabel("trig function")
plt.legend(loc = 1)
plt.savefig("/Users/petra/OneDrive/Documents/PHYS304/pbudavari_hw/"+ str("trig_lib") + ".png")
# plt.show()
plt.close()

def sinerror(x):
#take arg mod 2pi
	x=x%(2.e0*np.pi)
#initialize iterator and sum
	i = 0
	s,sold = 0.e0,0.e0
	for i in range(50):
		sold=s
		s+= float((((-1)**i) * (x**((2*i) + 1))))/float(math.factorial(((2*i) + 1)))
		if s==0:
			continue
#If difference is within some value - stop and caluclate error
		if np.abs((sold-s)/s)<=0.00000000001:
			# break 
			error = np.abs((sold-s)/s)
			return error
		
	

def coserror(x):
#take arg mod 2pi
	x=x%(2.e0*np.pi)
#initialize iterator and sum
	i = 0
	s,sold = 0.e0,0.e0

#Keep at most 10000 terms in the Taylor series
	for i in range(10000):
		sold=s
		s+= float((((-1)**i) * (x**((2*i)))))/float(math.factorial((2*i)))
		error = (sold-s)/s
#If difference is within some value - stop and caluclate error
		if np.abs((sold-s)/s)<=0.00000000001:
			 
			error = np.abs((sold-s)/s)
			return error
		

def tanerror(x):
#take arg mod 2pi
	x=x%(2.e0*np.pi)
#initialize iterator and sum
	error = math.sqrt((sinerror(x)/pcos(x))**2 + ((psin(x) * coserror(x))/(pcos(x))**2))
#If converged to machine precision then break out of loop
	return error

serr_vec = np.vectorize(sinerror)
cerr_vec = np.vectorize(coserror)
terr_vec = np.vectorize(tanerror)

x = np.arange(0, 1000)

sinerror_vec = np.array([])
for i in range(len(x)):
	error1 = sinerror(x[i])
	sinerror_vec = np.append(sinerror_vec, error1)
print(sinerror_vec)

coserror_vec = np.array([])
for i in range(len(x)):
	error2 = coserror(x[i])
	coserror_vec = np.append(coserror_vec, error2)
print(coserror_vec)

tanerror_vec = np.array([])	
for i in range(len(x)):
	error3 = sinerror(x[i])
	tanerror_vec = np.append(tanerror_vec, error3)
print(tanerror_vec)

# plt.figure().set_figwidth(100)

plt.plot(x, sinerror_vec, label = "sin error")
plt.plot(x, coserror_vec,':', label = "cos error")
plt.plot(x, tanerror_vec, ':',label = "tan error")

# plt.ylim(0, 150)
# plt.xlim(0.999999, 1.00001)
plt.title("Fractional error of calculated trig")
plt.xlabel("x")
plt.ylabel("fractional error")
plt.legend(loc = 1)
plt.savefig("/Users/petra/OneDrive/Documents/PHYS304/pbudavari_hw/"+ str("frac_err") + ".png")
plt.show()
plt.close()