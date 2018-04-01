##코딩도장 1번 문제 http://codingdojang.com/scode/365?langby=r#answer-filter-area
v<-NULL
for(i in 1:5000){
  v<-c(v, i+i%%10+i%/%10%%10+i%/%100%%10+i%/%1000%%10)
}
unique(v)
sum(setdiff(c(1:5000), unique(v)))