##http://codingdojang.com/scode/266?answer=10459#answer_10459

f1<-function(x,y){
m<-matrix(rep(NA, x*y), nrow=y, ncol=x)
i<-1
j<-0
k<-0
a<-1
repeat{
  if(sum(is.na(m))==0){
    break
  }
  if(a%%2==1){
    j<-j+(-1)**(((a-1)%/%2)%%2)
    repeat{
      if(j>x|j==0){
        a<-a+1
      if(j>x){
        j<-j-1
        break
        }else{
        j<-1
        break
        }}else{
      if(!is.na(m[i,j])){
        j<-j+(-1)**(((a+1)%/%2)%%2)
        a<-a+1
        break
        } }
      m[i,j]<-k
      j<-j+(-1)**(((a-1)%/%2)%%2)
      k<-k+1
      }}else{
        i<-i+(-1)**(((a-1)%/%2)%%2)
        repeat{
          if(i>y|i==0){
            a<-a+1
          if(i>y){
            i<-i-1
            break
            }else{
            i<-1
            break
            } } else{
          if(!is.na(m[i,j])){
            i<-i+(-1)**(((a+1)%/%2)%%2)
            a<-a+1
            break
          } }
          m[i,j]<-k
          i<-i+(-1)**(((a-1)%/%2)%%2)
          k<-k+1
        } }
}
return(m)}

f1(6,5)