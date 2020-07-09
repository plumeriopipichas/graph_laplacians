
las_bes<-seq(1.005,1.99,0.005)

# pendientes<-numeric()
# finicial<-numeric()
# 
# for (b in las_bes){
#   base<-hacer_base(b)
#   pendientes<-c(pendientes,(base$fi[101]-base$fi[1])/(base$r[101]-base$r[1]))
#   finicial<-c(finicial,la_fi(b,b))
# }
# 
# # base2<-data.frame(b=las_bes,pendientes,finicial)
# # base2<-mutate(base2,fifinal=finicial+pendientes*(b/(b-1)-b))
# # 
# b<-1.1
# 
# base1<-hacer_base(b)
# base1<-mutate(base1,lizq=(4*(r+b-lambda1(b,r))**2)/((2*b-lambda1(b,r))**2),
#               lder=(r+b-1)**2/(b**2-b+1))
# 
# 
# g<-ggplot(base1)+
#  geom_line(aes(r,lizq),color="blue")+
#   geom_line(aes(r,lder),color="green")
# 
# show(g)
# 
# #h<-ggplot(base1,aes(r,r-fi-c))+geom_point()+geom_smooth(method="lm")
# 
# #show(h)
# 
# #rm(g,h)
# 
# # b<-1.1
# # r<-1.3
# # 
# # base_CR<-hacer_base_rayleighs(b,r)
# # alfa1<-2*(r+b-lambda1(b,r))/(2*b-lambda1(b,r))
# # alfa2<-2*(r+b-lambda2(b,r))/(2*b-lambda2(b,r))
# # 
# # alfa3<-(r-b)/(r-la_fi(b,r)-ce(b,r))
# #   
# # g<-ggplot(base_CR,aes(y_entre_x,cociente))+geom_line()+geom_vline(xintercept = alfa1,color="red")+
# #   geom_vline(xintercept = alfa2,color="blue")+geom_vline(xintercept = alfa3,color="green")
# #show(g)
# 
# b<-1.32
# 
# base3<-hacer_base(b)
# 
# am<-numeric()
# for (k in 1:nrow(base3)){
#   r<-base3$r[k]
#   A<-crea_lap(r,b,ce(b,r))
#   am[k]<-algebraic_mult(A)
# }
# base3$mult.alg<-am
# 
# r0<-1.71
# 
# base4<-hacer_base_rayleighs2(b,r0)
# 
# g<-ggplot()+geom_line(data=base3,aes(r,mult.alg),color="red")+
#   geom_line(data=base4,aes(r,cociente_xy),color="purple")+geom_vline(xintercept = r0)
# 
# #show(g)
# 
# rm(A,k,am,b,r,r0)

expora<-data.frame(b=las_bes,mayor_r=superior_b(las_bes),
                   sirve_con_y2=cota_r_para_y2(las_bes))
expora<-mutate(expora,rext1=min(mayor_r,sirve_con_y2))
for (k in 1:nrow(expora)){expora$rext1[k]<-min(expora$mayor_r[k],expora$sirve_con_y2[k])}

expora$nueva_y<-num_ev_min(expora$b,expora$rext1)/den_ev_min(expora$b,expora$rext1)

View(expora)

