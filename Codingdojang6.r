##http://codingdojang.com/scode/398?answer=10575#answer_10575

f1<-function(x){
  if(x==0){
    print("0")
  }else{
    if(x<0){
      n<--x
    }else{
      n<-x }
    t<-trunc(log10(n))%/%3+1
    v<-NULL
    for(i in 1:t){
      v[i]<-(n%%(10**(3*i)))%/%(10**(3*(i-1))) }
    p<-NULL
    if(is.double(n)){
      p<-sub("0", "",as.character(round(n%%1,2))) }
    for(u in v[-length(v)]){
      if(u<10){
        p<-paste0(",","00", u, p)
      }else if(u<100){
        p<-paste0(",","0", u, p)
      }else{
        p<-paste0(",",u,p)  } }
    p<-paste0(v[length(v)],p)
    if(x<0){
      p<-paste0("-",p) }
    print(p) } }

f1(1000)
f1(20000000)
f1(-3545.24)