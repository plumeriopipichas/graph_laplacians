# -*- coding: utf-8 -*-
#!/usr/bin/env python

import sys

import scipy as sp

import math 

from random import randint

from scipy import linalg as al

import numpy as np

import matplotlib as mp

import matplotlib.pyplot as plt

from collections import deque

import laplace_graficas as lg

import laplace_ciclos as lc

from tipos_laplacianos_discretos import ciclo_basico 

from laplace_ciclos import provS as schwarz


#en ese bloque se grafican los eigenvalores con conductancias b, 1/b y 1 en función de b>1 y también
#relaciones entre las entradas de los eigenvectores


x = []
y = []
z = []
w = []

for j in range(15,30):
	c = float(j)/10.0
	b = 3/2.0	
	a = (b*c-(b+c))/(1-(b+c))
	C = [a,b,c]
		
	T = lc.genera_ciclo(3,C)
	
	x.append(c) 
	
	menor = lg.eigenvalores(T)[0][1]
	mayor = lg.eigenvalores(T)[0][2]	

	#eigenvector_1 = sp.transpose(lg.eigenvalores(T)[1])[1]
	#eigenvector_2 = sp.transpose(lg.eigenvalores(T)[1])[2]

	y.append(round(menor,4))
	z.append(round(mayor,4))
	#w.append(round(-eigenvector_1[0]/eigenvector_1[1],4))
	
	#w.append(1.5)	
	
	

b_grande=plt.figure()

plt.plot(x, y,'b--',label = 'Smallest positive eigenvalue')
plt.plot(x,z,'b+',label = 'Largest eigenvalue')
plt.xlabel('3/2<r<3')
plt.ylabel('Eigenvalues')
plt.legend(loc = 'center right')
plt.show()

b_grande.savefig("b_grande.pdf",bbox_inches='tight')

"""

x = []
S = []

for j in range(100,115):
	b = float(j)/100.0
	x.append(b) 	
	S.append(schwarz(b,1.0,-1.00001))

grafica_prueba=plt.figure()
	
plt.plot(x,S,'gp')
#plt.show()

grafica_prueba.savefig("prueba2.pdf",bbox_inches='tight')


"""

