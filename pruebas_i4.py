# -*- coding: utf-8 -*-
#!/usr/bin/env python

import numpy as np

from scipy import linalg as al

from sympy import *

import laplace_graficas as lg


#un cálculo de los cocientes de Rayleigh para los valores dados y para una transformación particular de ellos

def Schah(p,w,x,y):
	p = float(p)
	w = float(w)
	x = float(x)
	y = float(y)
	e=[]	
	n=[]
	e.append(p**2*w**2+(p**2/(p-1))*((x-w)**2+(y-x)**2)+y**2*(p/(p-1))**2)		
	n.append(x**2+y**2+w**2)
	e.append(p**2*w**2+(p**2/(p-1))*((y-w)**2+x**2)+(x+y)**2*(p/(p-1))**2)
	n.append(y**2+(x+y)**2+w**2)	
	e = np.array(e)
	n = np.array(n)	
	sw = e/n
	return sw

                         
def sime_1(w,y):
	s = np.sqrt((w**2+y**2)/2)	 
	return s


#En el caso p=3, la función f3 revisa que (x,y) esté en la curva de valores que hacen que el cociente de
# Schwarz de (1, ax, ay) se minimice cuando a=1. En particular, si (1,x,y) es eigenvector del tono fundamental,
# es necesario que (x,y) esté en esa curva. Revisar quiere decir que f3(x,y)=0.     


def f3(x,y):
	x=float(x)
	y=float(y)	
	return(4*x**3+4*x*(y**2-2*y-1)-4*x**2-6*y**2)	
	#return (2*x**3+2*x*y-2*x**2-3*y**2+4*x*y-2*x)

#revisar que pasa al simetrizar con sime_1 a los eigenvectores correspondientes al tono fundamental, para diversos
#valores de p


"""
for k in range(0,50):
	p = float(10+0.2*k)	
	print k
	L = lg.lapo_4(p)
	A = lg.lapo_4(2)
	v0=[round(al.eigh(L)[1][0][0],4),round(al.eigh(L)[1][1][0],4),round(al.eigh(L)[1][2][0],4)]
	#print v0
	v1=[sime_1(v0[0],v0[2]),v0[1],sime_1(v0[0],v0[2])]	
	#print("tono fundamental: ")
	#lg.tono_fundamental_D(L)	
	print ("original: ")
	print lg.schwarz(L,v0)
	print("simetrizado: ")
	print lg.schwarz(A,v1)
	if lg.schwarz(L,v0)<lg.schwarz(A,v1):
		break


for k in range (1,100):
	c0 = Schah(p,w,x,y)
	c1 = Schah(2,sime_1(w,y),x,sime_1(w,y))
	print (w,x,y)
	print ("original: ") 
	print np.round(c0[0],2)
	#print np.round(c0[1],2)
	print ("simetrizado: ") 
	print np.round(c1[0],2)
	print ("laderas: ")
	print sime_1(w,y)
	#print np.round(c1[1],2)
	y = y+0.1
	if c1[0]>c0[0]: 
#or c1[1]>c0[1]:
		break


for m in range(21):
	cocientes = Schah(39,1,x,y)	
	print [x,y]	
	print round(cocientes[0],2)
	x1 = y
	y = x+y
	x = x1


for m in range(71,88):
	cociente = Schah(3*m,1,m,m*(1+np.sqrt(5))/2)[0]		
	print round(cociente,4)



def fp3 (x):
	x = float(x)
	dis = np.sqrt(4*x**2-2*(x**3-x**2-x)**(2*x-3))
	num1 = 2*x+dis
	num2 = 2*x-dis
	den = 2*x-3	
	y1 = num1/den
	y2 = num2/den
	return [y1,y2]


def dfpp3(x,y,alpha):
	x = float(x)
	y = float (y)
	alpha = float(alpha)
	num=9*(6+alpha**2*(4*x**2+3*y**2-4*x*y)-alpha*4*x)
	den=4*(alpha**2*(x**2+y**2)+1)
	return num/den

print ("dfpp3", dfpp3(0,0,1)) 


for m in range(0,40):
	r = [(1+0.01*float(m))*2.4536,(1+0.01*float(m))*2.5713]	
	t = [(1-0.01*float(m))*2.4536,(1-0.01*float(m))*2.5713]	
	print dfpp3(r[0],r[1],1)
	print dfpp3(t[0],t[1],1)



def form_p3(x,y):
	res = 4*x*(x**2+y**2)-4*x**2-6*y**2-8*x*y-4*x
	return res

"""
L = lg.lapo_4(3)
lg.tono_fundamental_D(L)

v0=[round(al.eigh(L)[1][0][0],11),round(al.eigh(L)[1][1][0],11),round(al.eigh(L)[1][2][0],11)]
v = [round(j/v0[0],11) for j in v0]

print (v)
print ("f3", f3(v[1],v[2]))

"""
print form_p3(v[1],v[2])

def s3(x,y):
	x = float(x)
	y = float (y)
	a = Symbol('a')
	num=9*(6+a**2*(4*x**2+3*y**2-4*x*y)-a*4*x)
	den=4*(a**2*(x**2+y**2)+1)
	return num/den

print diff(s3(1,0))
"""
