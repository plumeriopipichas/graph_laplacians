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


x = []
y = []
z = []
x1 = []
x2 = []

for j in range(115,500):
	p = float(j)/100.0
	q = p/(p-1)
	menor = q*(p-np.sqrt(1+(p-2)*(p-1)))
	mayor = q*(p+np.sqrt(1+(p-2)*(p-1)))	
	equis1 = 1 - menor/p
	equis2 = 1 - mayor/p	

	x.append(p)
	y.append(menor)
	z.append(mayor)
	x1.append(equis1)
	x2.append(equis2)
'''		
fegurese = plt.figure()

plt.plot(x, y,'b-',label = ' ')
plt.show()

fegurese.savefig("menor.pdf",bbox_inches='tight')

fegurese2 = plt.figure()

plt.plot(x, z,'b-',label = ' ')
plt.show()

fegurese2.savefig("mayor.pdf",bbox_inches='tight')
'''

fegurese3 = plt.figure()

plt.plot(x, x1,'b-',label = 'para el menor')
#plt.plot(x, x2,'b+',label = 'para el mayor')
plt.show()

fegurese3.savefig("valor.pdf",bbox_inches='tight')


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

