##http://codingdojang.com/scode/401?answer=10422#answer_10422

#우선 n자리수에 앞뒤 같은 수가 몇개인지 계산하는 함수를 만듬.
  a <- function(n){
    if(n==1){
      return(10)     #1자리수는 10개임.
    } else {
      if(n==2){
        return(9)    #2자리수(11~99)는 9개임.
        } else {
          m <- n%/%2
          if(n%%2==1){    #3,5,7,9,...자리수인 경우
            return((10**m-10**(m-1)) * a(1))
            } else {      #4,6,8,10,...자리수인 경우
              return(10**m-10**(m-1)) 
            }}}}
#근데 n이 617~619일 때 Inf로 나오고, 620이상이면 NaN이 나옴. 
#R의 오류인지 이 함수의 오류인지 확인 못 함. 하지만 617자릿수 미만까진 문제 없을 것으로 봄.

#위 함수a(n)를 이용해서 m번째 앞뒤 같은 수를 출력하는 함수를 만듬.
apdui<-function(m){
  if(m<=10){
    return(m-1)
  }else{
k<-a(1)
i<-2
while(m>k){
  k<-k+a(i)
  i<-i+1
}
if(i%%2==1){
r<-10**((i-1)/2-1)-1+m-k+a(i-1)
result<-r
c<-trunc(log10(r))
for(h in 1:(c+1)){
  result<-paste0(result,r%%10)
  r<-r%/%10
}
return(result)
}else{
r1<-(m-k+a(i-1))%/%10+10**((i-2)/2-1)
r2<-((m-k+a(i-1)))%%10-1
result<-paste0(r1, r2)
c<-trunc(log10(r1))
for(h in 1:(c+1)){
  result<-paste0(result,r1%%10)
  r1<-r1%/%10
}
return(result)
}}}

apdui(1000000)