#www.codeforces.com
#A. Watermelon 
#4이상의 짝수면 yes

A = int(input())
if (A >= 4) and (A%2==0):
    print('yes')
else :
    print('no')
    
#A. Adaptation Stories
A=int(input())
lst=input().split(' ')
s=0
r=0
for i in lst:
    s+=int(i)
    if s<0:
        r-=s
        s=0
print(r)

#A. Theatre Square
lst=input().split(' ')

x = int(lst[0])/int(lst[2])
if x%1!=0:
    x = int(x+1)

y = int(lst[1])/int(lst[2])
if y%1!=0:
    y = int(y+1)
    
print(int(x*y))

