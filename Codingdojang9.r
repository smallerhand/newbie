##http://codingdojang.com/scode/408?answer=10176#answer_10176

s<-c(1,3,4,8,13,17,20)

short<-function(...){
  v<-(...)
  v2<-NULL
  r<-NULL
  for(i in 2:length(v)){
    v2[i]<-v[i]-v[i-1]
  }
  r<-paste(v[which.min(v2)-1], v[which.min(v2)])
  return(r)
}

short(s)