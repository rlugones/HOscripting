############
#Ej 1.a
############
mult3 = set(range(0,1000,3))
mult5 = set(range(0,1000,5))
mult3o5 = mult3 | mult5
suma = sum(mult3o5)
print 'Suma de multiplos de 3 o 5 menores a 1000 es',suma

############
#Ej 1.b
############
fibo = [1,2]
while fibo[-1]+fibo[-2] < 1e6 : 
    fibo.append(fibo[-1]+fibo[-2])

suma=0
for i in fibo : 
    if i%2!=0 : 
        suma+=i

print 'Suma de nros de Fibonacci impares hasta 1000000 es', suma



############
#Ej 1.c
############
nro=600851475143
a=nro
divisores=[]
while a!=1 : 
    for i in xrange(2,a+1) : 
        if a%i==0 :
            divisores.append(i)
            a/=i
            break

print 'Maximo divisor primo de',nro,'es',max(divisores)



############
#Ej 2
############
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

def fitFunc(x,a,b,c) : 
    return a*x**2+b*x+c

data_x=np.array([7.5,4.48,8.60,7.73,5.28,4.25,6.99,6.31,9.15,5.06])
data_y=np.array([28.66,20.37,22.33,26.35,22.29,21.74,23.11,23.13,24.68,21.89])
fitParams, fitCovariances = curve_fit(fitFunc, data_x, data_y)
x_aux=np.linspace(min(data_x),max(data_x),10*len(data_x))
f=plt.figure()
ax=f.add_subplot(111)
ax.plot(data_x, data_y, '.', \
        x_aux, fitFunc(x_aux, fitParams[0], fitParams[1], fitParams[2]))

plt.show()



############
#Ej 3
############
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

p=np.poly1d([1, 1, -4, 4])
dp=p.deriv()
x=np.arange(-10,10,0.1)

f1=plt.figure()
ax1=f1.add_subplot(111)
ax1.plot(x,p(x),color='red')
ax1.set_title('Funcion')
ax1.grid()

f2=plt.figure()
ax2=f2.add_subplot(111)
ax2.plot(x,dp(x),color='blue')
ax2.set_title('Derivada')
ax2.grid()

plt.show()

data2 = open('data2.txt', 'w')
vec= np.c_[np.arange(-10,10,0.1),p(np.arange(-10,10,0.1))]
np.savetxt(data2,vec,fmt='%f',delimiter='\t',header="x             # f(x)") 
data2.close()

data=open('data.txt','w')
print >> data, '#x       #p(x)'
for i in np.arange(-10,10,0.1) : print >> data, i,'   ',p(i)
data.close()
