##http://codingdojang.com/scode/406?answer=10167#answer_10167
abc<- function(m, n){
  r<-NULL
  if(n>=1){
    if(m%%n==0){
      r<-m%/%n
    }else{
      r<-m%/%n+1
    }
  }else{r<-'error'}
return(r)  
}