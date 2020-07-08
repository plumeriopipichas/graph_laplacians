# -*- coding: utf-8 -*-
#!/usr/bin/env python

import sys

import math 

from random import randint

import scipy as sp


def provN1(b,x0,x1):
	N = ((b**2+b+4)/b)*(x0**2)
	return N

def provN2(b,x0,x1):
	N = ((b*(2*b+1)+2*b**2+1)/b)*(x1**2)
	return N

def provN3(b,x0,x1):
	N = ((4*b**2-2*b+4.0)/b)*(x0*x1)
	return N

def D(x0,x1):
	D = x0**2+x1**2+(x0+x1)**2
	return D

b = 3.0

x0 = 1.0
x1 = -2.0

print round(provN1(b,x0,x1),3)
print round(provN2(b,x0,x1),3)
print round(provN3(b,x0,x1),3)

print round((provN1(b,x0,x1)+provN2(b,x0,x1)+provN3(b,x0,x1))/D(x0,x1),3)
