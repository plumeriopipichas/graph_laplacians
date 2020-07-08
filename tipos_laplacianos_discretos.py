# -*- coding: utf-8 -*-
#!/usr/bin/env python


def ciclo_basico(n):
	Cn=[]
	for k in range(n):
		Cn.append([0.0]*n)
		print k
		print Cn		
		Cn[k][k]=2.0		
		if k>0:
			Cn[k][k-1]=-1.0
		if k<n-1:
			Cn[k][k+1]=-1.0
		 

	Cn[0][n-1]=-1.0
	Cn[n-1][0]=-1.0
												  
	return(Cn)

def lap_completo(n):
	Ln=[]
	for k in range(n):
		Ln.append([-1]*n)
		Ln[k][k]=n-1
	return(Ln)


