# -*- coding: utf-8 -*-
#!/usr/bin/env python

import sys

import scipy as sp

from scipy import linalg 

import matplotlib as mp

def T(r):
	t = sp.mat([[2.0*r, 0, 0],[0, r+1.0, 0],[0, 0, r+1.0]])
	return t

def X(r):
	t = sp.mat([[3.0*r+1, -1, -r],[-1, 3*r+1.0, -r],[-r, -r, 2*r+2.0]])
	return t

def J(r):
	t = sp.mat([[-r,-r,0],[-r, 0, -r],[0,-1, -1]])	
	return t

def energia(M,v):
	e = (v.T*(M*v))[0,0] 	
	return e



"""Este es un programa para calcular extensiones armonicas en las primeras graficas de aproximacion a SG""" 	 
         
""" En el nivel 1 se consideran conductancias iguales a un valor r en las diagonales, e iguales a 1 en las horizontales

Se calcularan las conductancias correxpondientes al nivel 0 para que la extension armonica del nivel 0 al nivel 1 mantenga la energia constante, asi como la matriz de extension armonica correspondiente"""

r=raw_input("\n \n Elige el valor de la conductancia r > ")

try:
	r=float(r)
except:
	print "La conductancia debe ser un numero positivo"
	exit(1)	

if (r>0):
	print " "
else:
	print "La conductancia debe ser un numero positivo"
	exit(1)

print "La matriz T de restriccion a la frontera es:\n "	
print T(r)
print "\n"

print "La matriz X para nodos de extension es:\n "
print X(r)
print "\n"

print "La matriz J que conecta los vertices a ambos niveles es:\n "
print J(r)
print "\n"

Y = X(r)
R = linalg.inv(Y)
EA = -R*J(r)

print "inversa\n"
print R

print "La matriz de extension armonica es:\n"
print EA
print "\n"

for i in range(3):
	for j in range(3):
		print ("Entrada %d %d es %r") % (i,j,round(EA[i,j],2))

L = [] 
L.append(T(r)-J(r).T*R*J(r))
L.append(sp.bmat([[T(r),J(r).T],[J(r),X(r)]]))

print "La matriz laplaciana al nivel 0 es:\n"
print L[0]
print "\n "

print "La matriz laplaciana al nivel 1 es:\n"
print (L[1])
print "\n " 

#Evaluar energias para compararlas

"""Se va a evaluar la energia al nivel 0 para un vector dado, y la energia al nivel 1 para su extension armonica. A ver si coinciden, como deberian"""

print "Dame los valores en la frontera\n "

v_0=[]
v_0.append(raw_input("Primera entrada > "))
v_0.append(raw_input("Segunda entrada > "))
v_0.append(raw_input("Tercera entrada > "))

try:
	for i in range(3):	
		v_0[i]=float(v_0[i])
except:
	print "Vector no valido"	
	exit(1)

v_0 = sp.mat(v_0).T

v_1 = EA*v_0

u = sp.bmat([[v_0],[v_1]])

print "Su extension armonica al nivel 1 es:\n" 
print u 

print "La energia al nivel 0 es %r\n\n" % round(energia(L[0],v_0),2)

print "La energia al nivel 1 es %r\n\n" % round(energia(L[1],u),2)



