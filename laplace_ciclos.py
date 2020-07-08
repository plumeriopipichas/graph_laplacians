# -*- coding: utf-8 -*-
#!/usr/bin/env python

import sys

import scipy as sp

import math 

from random import randint

from scipy import linalg as al

import numpy as np

import matplotlib as mp

from collections import deque

import laplace_graficas as lg

from tipos_laplacianos_discretos import ciclo_basico 


#funcion exclusiva para ciclos, pide las conductancias de cada arista y regresa la suma de 
# las resistencias 

def genera_ciclo(n,C):	#n: vértices del ciclo C: conductancias. Regresa el laplaciano.
	L = []	
	for k in range(n): 
		L.append([0]*n)	
	for k in range(n-1): 				
		L[k][k+1] = -C[k]		
	for k in range(n-1):
		L[k+1][k] = -C[k]
	L[0][n-1] = - C[n-1]		
	L[n-1][0]=-C[n-1]
	for k in range(n):
		for j in range(n):
			if j<>k:
 				L[k][k] = L[k][k]-L[k][j]
	return(sp.array(L))


#genera el ciclo de n vértices y conductancias C y calcula la suma de las resistencias en cada arista

def resistencia_ciclo(n,C): 
	rt = 0	
	for j in range(n):
		C  = deque(C)
		C.append(C[0])		
		C.popleft()	
		L  = genera_ciclo(n,C)	
		rt = lg.resistencia(L)+rt
	return(rt)

#formulazo para el cociente de Schwarz en caso particular: conductancias b, 1 y 1/b

def provS(b,x0,x1):
	N = ((b**2+b+4)/b)*(x0**2)+((b*(2*b+1)+2*b**2+1)/b)*(x1**2)+((4*b**2-2*b+4)/b)*(x0*x1)
	D = x0**2+x1**2+(x0+x1)**2	
	S = N/D	
	return S



"""
#algebhraic connectivity de ciclos sin pesos

for j in range(3,15):
	n = j
	C = [1]*n

	probando=genera_ciclo(n,C)	

	print (n)
	print(lg.eigenvalores(probando))[0][1]
"""


#eigenvector de la algebraic connectivity para ciclos sin pesos

for j in range(4,5):
	n = j
	C = [1]*n
	#D = np.random.rand(1,n)[0]
	basico = genera_ciclo(n,C)	
	#aleatorio = genera_ciclo(n,D)	
	print ("\n")
	print ("vertices: "+ str(n))
	eigenvalores = lg.eigenvalores(basico)[0]	
	evectos = (lg.eigenvalores(basico)[1]).transpose()
	noceros = evectos[1][evectos[1]<>0]	
	r = min(abs(noceros))	
	evectos_vis = evectos[1]/r	
	print ("eigenvalores del equilibrado: " + str(eigenvalores[eigenvalores>0]) + "\n")	
	print ("un eigenvector de la a.c. del equilibrado: " + str(evectos_vis))
	noceros = evectos[2][evectos[2]<>0]	
	r = min(abs(noceros))	
	evectos_vis = evectos[2]/r	
	print ("otro eigenvector de la a.c. del equilibrado: " + str(evectos_vis))
	
	p = 3
	D = [1,1,p,p/(p-1)]
	alterado = genera_ciclo(n,D)
	print("\n")
	eigenvalores = lg.eigenvalores(alterado)[0]	
	evectos = (lg.eigenvalores(alterado)[1]).transpose()
	noceros = evectos[1][evectos[1]<>0]	
	r = min(abs(noceros))	
	evectos_vis = evectos[1]/r	
	print ("eigenvalores con pesos alterados: " + str(eigenvalores[eigenvalores>0]) + "\n")	
	print ("eigenvector de su a.c.: " + str(evectos_vis))
	noceros = evectos[2][evectos[2]<>0]	
	r = min(abs(noceros))	
	evectos_vis = evectos[2]/r	
	print ("eigenvector del segundo eigenvalor: " + str(evectos_vis))
	
"""
N=-1
while (N<1 or N<>int(N)):
	try:
		N=int(raw_input('Dame el numero de vértices del ciclo > '))
	except:
		print ('El valor deberia ser un entero positivo') 
		print "\n"


for N in range(3,8):
	C=[]	
	C.append([1]*N)
	print C
	
	print resistencia_ciclo(N,C[0])

#T = genera_ciclo(N,C)

#print T




for j in range(6,25):	
	j=float(j)	
	b=float(j/10)	
	a=(b*(b-2))/(1-2*b)
	print ('dos aristas iguales', b)	
	ciclo = genera_ciclo(3,[a,b,b])	
	# print resistencia_ciclo(3,[a,b,b])
	lg.tono_fundamental(ciclo)


for k in range(10):
	s = float(k)	
	b = 2-s/10
	c = 0.85

	a = (b*c-(b+c))/(1-(b+c))
	print('a= ',round(a,3))
	print('b= ',b)
	print('c= ', c)
	C = [a,b,c]
	T = genera_ciclo(3,C)

	#print('resistencia= ', resistencia_ciclo(3,C))
	print('menor eigenvalor: ', lg.eigenvalores(T)[0][1])
	print('mayor eigenvalor: ', lg.eigenvalores(T)[0][2])


c = 1.0
b = 1.0
a = 1.0

for j in range(1,11):
	c1 = c/j
	b1 = b/j
	a1 = a/j
	C = [a1,b1,c1]
	T = genera_ciclo(3,C)
	r = resistencia_ciclo(3,C)	
	#print lg.tono_fundamental(C)
	print r 





for j in range(1,19):	
	j=float(j)	
	b=float(j/10)
	a=(b*c-(b+c))/(1-(b+c))
	print b	
	print a
	C=[a,b,c]
	T=genera_ciclo(3,C)
	print T
	print lg.eigenvalores(T)


b = 3.0
c = 1/b
a = (b*c-(b+c))/(1-(b+c))

print('a= ',round(a,3))
print('b= ', b)
print('c= ', c)

C = [a,b,c]
T = genera_ciclo(3,C)

v = [2.0,1.0]
v.append(-v[0]-v[1])

print v

casos = []

casos.append(v)
casos.append([v[1],v[0],v[2]])
casos.append([v[0],-v[1],v[1]-v[0]])
casos.append([v[1],-v[0],-v[1]+v[0]])

for j in range(4):
	print casos[j]
	print ('Cociente de Schwarz = ', round(lg.schwarz(T,casos[j]),3))	
	print provS(b,casos[j][0],casos[j][1])

menor = lg.eigenvalores(T)[0][1]
mayor = lg.eigenvalores(T)[0][2]

eigenvector_1 = sp.transpose(lg.eigenvalores(T)[1])[1]
eigenvector_2 = sp.transpose(lg.eigenvalores(T)[1])[2]


print T

print('resistencia= ', resistencia_ciclo(3,C))
print('menor eigenvalor: ', menor)
print('mayor eigenvalor: ', mayor)

print ('eigenvector 1: ', eigenvector_1)
print ('eigenvector 2: ', eigenvector_2)

#print round(-eigenvector_1[1]/eigenvector_1[0],4)

#print lg.eigenvalores(T)

"""



