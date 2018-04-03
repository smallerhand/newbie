##http://codingdojang.com/scode/393?answer=10214#answer_10214
a<-0
for(i in 1:10000){
  if(i%%10==8){
    a<-a+1}
  if((i%/%10)%%10==8){
    a<-a+1}
  if((i%/%100)%%10==8){
    a<-a+1}
  if((i%/%1000)%%10==8){
    a<-a+1}
}
print(a)