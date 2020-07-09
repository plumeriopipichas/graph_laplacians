b<-1.1
r<-1.7

A<-matrix(c(1,-2,1,1),2,2)

indirecto1<-A%*%c(2*b-lambda1(b,r),2*(r+b-lambda1(b,r)))
indirecto1<-completar(indirecto1)

indirecto2<-A%*%c(2*b-lambda2(b,r),2*(r+b-lambda2(b,r)))
indirecto2<-completar(indirecto2)

directos<-eigen(crea_lap(c,r,b))[2]

indirecto3<-A%*%c(1,(r+b-2*c+2*la_fi2(b,r))/(2*b-r+la_fi2(b,r)-c))
indirecto3<-completar(indirecto3)

