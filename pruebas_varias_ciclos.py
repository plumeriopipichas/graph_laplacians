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


def alfil(p):
	alfa = (p-2)/(p-1)
	return alfa 

"""
def rayleigh_especial():  
	x = []
	y = []	

	for j in range(2,5):
		p = float(j)
		ye = (1+alfil(p))**2+(p/(p-1))*(1+2*alfil(p))**2+p*(1-alfil(p))**2

		x.append(p)
		y.append(ye)
		
		
	prueba1 = plt.figure()
	plt.plot(x,y)
	plt.show()


rayleigh_especial()	
"""

def rayleigh_especial2():  
	x = []
	y = []	

	for j in range(2,5):
		p = float(j)
		ye = 2*(1+alfil(p))**2+(p/(p-1))*(1+alfil(p))**2+p*(1-alfil(p))**2

		x.append(p)
		y.append(ye)
		
		
	prueba1 = plt.figure()
	plt.plot(x,y)
	plt.show()


rayleigh_especial2()	

