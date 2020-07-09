#Calculos para un tres ciclo y resistencia global fija (igual a 2).

traza<-function(b,r){
  tr<-((b+r)**2+b**2+r**2)/(b+r-1)
  return(tr)
}

crea_lap<-function(a,b,c){
  lap<-matrix(c(a+b,-b,-a,-b,b+c,-c,-a,-c,a+c),3,3)
  return(lap)
}

lap_rf<-function(b,r){
  #if (b+r>b*r)
  c3<-(b+r-b*r)/(b+r-1)
  lapo<-crea_lap(b,r,c3)  
} 

explora_trazas<-function(b){
  x<-numeric()
  y<-numeric()
  for (r in seq((b+1)/2,b/(b-1),by=0.01)){
    x<-c(x,r)
    y<-c(y,traza(b,r))
  }
  qplot(x,y,geom="line")
}

la_fi <- function(b,r){
  c <- (b+r-b*r)/(b+r-1)
  fi <- sqrt(b**2+c**2+r**2-(b+c+r))
  return(fi)
}

la_fi2 <- function(b,r){
  c <- (b+r-b*r)/(b+r-1)
  fi <- sqrt(b**2+c**2+r**2-(b*r+c*r+b*c))
  return(fi)
}

genera_erres<- function(b){
  if (b>1 & b<2){
    erres<-seq(b,b/(b-1),(b/(b-1)-b)/100)  
  }
  else{
    print ("b fuera de rango")
    break
  }
  return(erres)
}

hacer_base <- function(b){
  x<-genera_erres(b)
  infos<-data.frame(r=x,fi=la_fi(b=b,r=x),c=(b+x-b*x)/(b+x-1))
}

ce<-function(b,r){
  c<-(b+r-b*r)/(b+r-1)
  return(c)
}

rayleigh_xy <- function(b,r,x,y){
  cociente<-(3/2)*(r*x**2+b*(x-y)**2+ce(b,r)*y**2)/(x**2-x*y+y**2)
  return(cociente)
}

hacer_base_rayleighs<-function(b,r){
  alfa <- seq(0.01,10,0.01)
  cociente<-rayleigh_xy(b,r,1,alfa)
  base<-data.frame(y_entre_x=alfa,cociente)
}

hacer_base_rayleighs2<-function(b,r0){
  B<-as.data.frame(hacer_base(b)[ ,1])
  names(B)[1]<-"r"
  x<-2*b-r0-ce(b,r0)+la_fi(b,r0)
  y<-r0+b-2*ce(b,r0)+2*la_fi(b,r0)
  cociente_xy<-numeric()
  for (k in B$r){
    cociente_xy<-c(cociente_xy,rayleigh_xy(b,k,x,y))
  }
  B$cociente_xy<-cociente_xy  
  return(B)
}

lambda1<-function(b,r){
  (2/3)*(r+b+ce(b,r)-la_fi(b,r))
}

lambda2<-function(b,r){
  (2/3)*(r+b+ce(b,r)+la_fi(b,r))
}

completar<-function(v){
  v<-append(v,-sum(v))
  v<-v/norm(as.matrix(v),"F")
  return(v)
}

algebraic_mult<-function(L){
  am<-eigen(L)$values[length(eigen(L)$values)-1]
  return(am)
}

cota_r_para_y2 <-  function(b){
  cota<-b+3/(2*b-1)
  return(cota)
}

superior_b<-function(b){
  sup <- b/(b-1)
  return(sup)
}

num_ev_min<-function(b,r){
  num<-2*(lambda1(b,r)-(b+r))
  return(num)
}

den_ev_min<-function(b,r){
  den<-(lambda1(b,r)-(b+b))
  return(den)
}

num_ev_max<-function(b,r){
  num<-2*(lambda2(b,r)-(b+r))
  return(num)
}

den_ev_max<-function(b,r){
  den<-(lambda2(b,r)-(b+b))
  return(den)
}