##http://codingdojang.com/scode/314?answer=10537#answer_10537

f2<-function(...){
f1<-function(s, number){
number<-unlist(strsplit(as.character(number), ""))
a<-length(number)
for(i in 1:a){
  cat(" ")
  for(j in 1:s){
  if(number[i]%in%c("1","4")){
    cat(" ")
  }else if(number[i]%in%c("2","3","5","6","7","8","9","0")){
    cat("-") }}
  cat(" ")
  cat(" ") }
cat("\n")
for(j in 1:s){
for(i in 1:a){
  if(number[i]=="1"){
    cat(" ")
    for(k in 1:s){
      cat(" ") }
    cat("|")
  }else if(number[i]%in%c("2","3","7")){
    cat(" ")
    for(k in 1:s){
      cat(" ") }
    cat("|")
  }else if(number[i]%in%c("4","8","9","0")){
    cat("|")
    for(k in 1:s){
      cat(" ") }
    cat("|")
  }else if(number[i]%in%c("5","6")){
    cat("|")
    for(k in 1:s){
      cat(" ") }
    cat(" ") }
  cat(" ") }
cat("\n") }
for(i in 1:a){
  cat(" ")
  for(j in 1:s){
  if(number[i]%in%c("1","7","0")){
    cat(" ")
  }else if(number[i]%in%c("2","3","4","5","6","8","9")){
    cat("-") }}
  cat(" ")
  cat(" ") }
cat("\n")
for(j in 1:s){
for(i in 1:a){
  if(number[i]=="1"){
    cat(" ")
    for(k in 1:s){
      cat(" ") }
    cat("|")
  }else if(number[i]%in%c("3","4","5","7","9")){
    cat(" ")
    for(k in 1:s){
      cat(" ") }    
    cat("|")
  }else if(number[i]%in%c("6","8","0")){
    cat("|")
    for(k in 1:s){
      cat(" ") }    
    cat("|")
  }else if(number[i]%in%c("2")){
    cat("|")
    for(k in 1:s){
      cat(" ") }
    cat(" ") }
  cat(" ") }
cat("\n") }
for(i in 1:a){
  cat(" ")
  for(j in 1:s){
  if(number[i]%in%c("1","4","7")){
    cat(" ")
  }else if(number[i]%in%c("2","3","5","6","8","9","0")){
    cat("-") }}
  cat(" ")
  cat(" ") }
cat("\n") } 
  v<-c(...)
  if(v[length(v)]==0&v[length(v)-1]==0){
    for(l in 1:((length(v)/2)-1)){
      f1(v[2*l-1],v[2*l])
    }
  }
}

f2(2,12345,3,67890,0,0)