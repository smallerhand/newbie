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

#A. Way Too Long Words
n=int(input())
lst=dict()

for i in range(n):
    lst[i]=input()

for i in range(n):
    if len(lst[i])>10:
        print(lst[i][0]+str(len(lst[i])-2)+lst[i][-1])
    else:
        print(lst[i])

#A. Next Round
n, k=map(int, input().split(' '))
if n < k:
    z = n
    n = k
    k = z

lst = input().split(' ')
a = int(lst[k-1])
output = 0
for i in lst:
    if int(i)>0:
        if int(i)>=a:
            output+=1
print(output)            
        
#A. String Task (아직 작성중)
A = input()
A = A.lower()
str = ''
for i in A:
    if i not in  ['a','o','y','e','u','i']:
        str += '.'
        str += i

print(str)

#A. Domino piling




