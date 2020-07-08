# -*- coding: utf-8 -*-
#!/usr/bin/env python



def crea_Y(v): #forma la grafica Y con sus vertices, dejando las aristas y el centro sin valor
	vertice=range(4)
	arista=range(3)
	for i in range(3):
		try:
			vertice[i]=float(v[i])
			arista[i]=None
		except:
			print('Los valores tienen que ser numericos\n')
	vertice[3]=None
	return vertice, arista

def crea_vertices(): #pide valores de los vertices en la frontera
	vertice=range(3)
	for i in range(3):
		try:
			vertice[i]=float(raw_input('Valor de vertice %d> ' % i))	
		except:
			print('Se requiere un valor numerico. Intenta otra vez\n')
			vertice[i]=eval(raw_input('Valor de vertice  > '))
	print ('Los valores en los vertices son %r') % vertice
	return vertice



def minima_ext_Y(v,a): #devuelve el valor de los vertices en grafica Y, incluido el centro que minimiza energia
	vertices=range(4)
	aristas=range(3)	
	for i in range(3):
		vertices[i]=float(v[i])
		aristas[i]=float(a[i])
	numerador = 0	
	denominador = 0
	for i in range(3):
		numerador = numerador+vertices[i]*aristas[i] 	
	for i in range(3):
		denominador = denominador + aristas[i]			
	vertices[3]=numerador/denominador	
	return vertices


def Y_especial(a): #asigna el valor de las aristas en Y para el caso a-a-b
	aristas=range(3)
	aristas[0]=a*(3*a*a+6*a+1)/(2*(2*a+1)*(a+2))
	aristas[1]=a*(2*a+3)/((2*a+1)*(a+2))
	aristas[2]=a*(2*a+3)/((2*a+1)*(a+2))
	print ('Los valores de las resistencias en las aristas en T son %r') % aristas
	for i in range(3):
		aristas[i]=float(1/aristas[i])
	print ('Los valores de las conductancias en las aristas en T son %r') % aristas
	return aristas

def T_especial(a): #asigna el valor de las aristas en el triangulo para el caso a-a-b
	aristas=range(3)
	aristas[0]=a*(3*a+2)/(2*a+1)
	aristas[1]=a*(3*a+2)/(2*a+1)
	aristas[2]=2*a*(2*a+3)*(3*a+2)/((2*a+1)*(3*a*a+6*a+1))
	print ('Los valores de las resistencias en las aristas en T son %r') % aristas
	for i in range(3):
		aristas[i]=float(1/aristas[i])
	print ('Los valores de las conductancias en las aristas en T son %r') % aristas
	return aristas

def energia_T(v,a): #calculo ad-hoc para la energia en el triangulo
	energia=a[0]*(v[0]-v[1])*(v[0]-v[1])+a[1]*(v[0]-v[2])*(v[0]-v[2])+a[2]*(v[1]-v[2])*(v[1]-v[2])
	return energia

def energia_Y(v,a): #calculo ad-hoc para la energia en Y
	energia = 0	
	for i in range(3):	
		energia = energia + a[i]*(v[i]-v[3])*(v[i]-v[3])
	return energia

a = float(raw_input('Dar el valor de a > '))

extremos = crea_vertices()

# = crea_Y(extremos,aristas)

aristasT = T_especial(a)

aristasY = Y_especial(a)

verticesY = minima_ext_Y(extremos,aristasY)

print ('Los vertices en Y son %r') % verticesY

print ('El valor en el centro debe ser %r') % verticesY[3]

e0 = energia_T(extremos,aristasT)

print extremos
print aristasY

e1 = energia_Y(verticesY,aristasY)

print ('La energia en el triangulo es igual a %r') % e0
print ('La energia en la Y es igual a %r') % e1
