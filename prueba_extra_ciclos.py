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

def res_per4(C):
	numerador = 0.0
	denominador = 0.0
	for k in range(0,3):		
		for j in range(k+1,4):		
			sumando =  C[j]*C[k]
			numerador = numerador + sumando				
	for k in range(0,2):		
		for j in range(k+1,3):		
			for i in range(j+1,4):			
				sumando =  C[i]*C[j]*C[k]
				denominador = denominador + sumando		
	cociente = numerador/denominador
	return(cociente)

"""
#pruebas para la funcion que calcula r.p. para el 4-ciclo

#print(res_per4([1]*4))

for j in range(11,32):
	p = j/10.0
	q = round(p/(p-1),2)
	print ("p= " + str(p))
	print ("q= " + str(q))
	print("resistencia periferica: "+ str(res_per4([1,1,p,q])))

"""

print(genera_ciclo(4,[1,1,2,2]))
print((lg.eigenvalores(genera_ciclo(4,[1,1,2,2])))[0])
print((lg.eigenvalores(genera_ciclo(4,[1,1,2,2])))[1].transpose())


#eigenvector de la algebraic connectivity para ciclos sin pesos


for j in range(4,5):
	n = j
	C = [1]*n
	#D = np.random.rand(1,n)[0]
	basico = genera_ciclo(n,C)	
	#aleatorio = genera_ciclo(n,D)	
	print ("\n")
	print ("vertices: "+ str(n))
	eigenvalores = res_per4(C)*(lg.eigenvalores(basico)[0])	
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
	
	for j in range(5,23):	
		p = j/11.0
		q = (2*p-1)/p
		D = [1,1,p,q]
		alterado = genera_ciclo(n,D)
		print("\n")
		eigenvalores = (lg.eigenvalores(alterado)[0])	
		evectos = (lg.eigenvalores(alterado)[1]).transpose()
		noceros = evectos[1][evectos[1]<>0]	
		r = min(abs(noceros))	
		evectos_vis = evectos[1]/r
		print ("p igual a "+str(p))	
		print ("eigenvalores con pesos alterados: " + str(eigenvalores[eigenvalores>0]) + "\n")	
		print("tomando en cuenta RP: " + str(res_per4(D)*(eigenvalores[eigenvalores>0])))
		print ("eigenvector de su a.c.: " + str(evectos_vis))
		noceros = evectos[2][evectos[2]<>0]	
		r = min(abs(noceros))	
		evectos_vis = evectos[2]/r	
		print ("eigenvector del segundo eigenvalor: " + str(evectos_vis))

#print("resistencia basica: " + str(res_per4(basico)))



