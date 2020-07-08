# -*- coding: utf-8 -*-
#!/usr/bin/env python

import scipy as sp

def Xmas(p):
	X=(1+sp.sqrt(p**2-3*p+3))/(p-2)
	return X

def Xmenos(p):
	X=(1-sp.sqrt(p**2-3*p+3))/(p-2)
	return X

def Rayleigh1(p,x):
	q = float(p/(p-1))	
	r = (p*(1-x)**2+q*(2+x)**2)/(1+x**2+(1+x)**2)	
	return r

print -1/2.0
print Rayleigh1(2,-1/2.0)


for m in range(21,31):
	k = float(m/10.0)
	print k
	print Rayleigh1(k,Xmas(k))
	print Rayleigh1(k,Xmenos(k))

	


