# -*- coding: utf-8 -*-
#!/usr/bin/env python

import sys

import math 

from random import randint

import scipy as sp

from scipy import linalg as al

import numpy as np

import matplotlib as mp

from collections import deque


def tono_fundamental(A):
	ev=eigenvalores(A)
	
	print ev[0][1] 
	return ev[0][1]

def tono_fundamental_D(A):
	ev=eigenvalores(A)
	
	print ev[0][0] 
	return ev[0][0]


def eigenvalores(A):
	av=list(al.eigh(A))

	av[0]=av[0].astype(float)
	av[1]=av[1].astype(float)

	for i in range(len(av[0]-1)):
		av[0][i]=round(float(av[0][i]),7)

	for i in range(len(av[1]-1)):
		for j in range(len(av[1][i]-1)):	
			av[1][i][j]=round(float(av[1][i][j]),7)
	
	return av

#Las siguientes funcines son para hacer la descomposición de una matriz  
#con respecto al subespacio generado por los primeros k vectores "canónicos" 

def descomponer_Y (A,k):	
	if k>len(A):
		print('Fuera de rango')
	else:
		Y = A[:k]
		for j in range(k):
			Y[j]=Y[j][:k]
		return(sp.array(Y))

def descomponer_J (A,k):	
	if k>len(A):
		print('Fuera de rango')
	else:
		J = A[k:len(A)]
		for j in range(len(A)-k):
			J[j]=J[j][:k]
		return(sp.array(J))

def descomponer_X (A,k):	
	if k>len(A):
		print('Fuera de rango')
	else:
		X = A[k:len(A)]	
		for j in range(len(A)-k):
			X[j]=X[j][k:len(A)]	
		return(sp.array(X))


#En la siguiente función, L debe ser un laplaciano de una gráfica. Se considera la frontera
#de L a los primeros k vértices. La función regresa la matriz que dados los valores en la 
# frontera regresa los valores de la única función armónica en el interior de la gráfica.


def extension_armonica(L,k):
	X = descomponer_X(L,k)
	J = descomponer_J(L,k)
	U = -al.inv(X).dot(J)

	return U

# Dado un laplaciano L, se regresa el laplaciano L0 respecto a los primeros k vértices,
# de modo que L0 y L forman una secuencia compatible

def compatible(L,k):
	L = list(L)	
	X = descomponer_X(L,k)
	J = descomponer_J(L,k)
	Y = descomponer_Y(L,k)
	L0 = Y-(J.T.dot(al.inv(X))).dot(J)	
	return L0

#Calcular la distancia entre los primeros dos vértices, de acuerdo a la métrica de resistencia

def resistencia(L):
	r = 1/compatible(L,2)[0][0]
	return r


# Función genérica para el cociente de Rayleigh para una matriz y un vector

def rayleigh(A,v):
	numerador = sp.dot(sp.dot(A,v),v)
	denominador = sp.dot(v,v)
	S = numerador/denominador
	return S

#Función ad-hoc que dado un valor de p genera el laplaciano de una gráfica formada por un intervalo partido en cuatro pedazos, con conductancia autosimilar, métrica de resistencia constante 1 y condiciones de Dirichlet.

def lapo_4(p):
	p = float(p)
	q = p/(p-1)	
	L = [[p**2+p*q,-p*q,0],[-p*q,2*p*q,-p*q],[0,-p*q,q**2+p*q]]
	return L


"""
print lapo_4(2)
print rayleigh(lapo_4(2),[1,np.sqrt(2),1])


p=1

while (p<2):
	try:
		p=float(raw_input('Dame el valor de p> '))
	except:
		print ('El valor debe ser al menos 2') 
		print "\n"

L = lapo_4(p)
#print al.eigh(L)
tono_fundamental_D(L)
v0=[round(al.eigh(L)[1][0][0],4),round(al.eigh(L)[1][1][0],4),round(al.eigh(L)[1][2][0],4)]
print v0
print [round(j/v0[0],4) for j in v0]


for k in range(3*71,3*88,3):
	L = lapo_4(k)	
	tono_fundamental_D(L) 
	#v0=[round(al.eigh(L)[1][0][0],8),round(al.eigh(L)[1][1][0],8),round(al.eigh(L)[1][2][0],8)]
	#print v0
"""

