#www.codeforces.com
#4A. Watermelon 
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

#1A. Theatre Square
lst=input().split(' ')

x = int(lst[0])/int(lst[2])
if x%1!=0:
    x = int(x+1)

y = int(lst[1])/int(lst[2])
if y%1!=0:
    y = int(y+1)
    
print(int(x*y))

#71A. Way Too Long Words
n=int(input())
lst=dict()

for i in range(n):
    lst[i]=input()

for i in range(n):
    if len(lst[i])>10:
        print(lst[i][0]+str(len(lst[i])-2)+lst[i][-1])
    else:
        print(lst[i])

#158A. Next Round
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
        
#118A. String Task
A = input()
A = A.lower()
str = ''
for i in A:
    if i not in  ['a','o','y','e','u','i']:
        str += '.'
        str += i

print(str)

#50A. Domino piling
m, n=map(int, input().split(' '))
print(int(m*n/2))

#231A. Team
n=int(input())
output=0
for i in range(n):
    a, b, c = map(int, input().split(' '))
    if a+b+c>=2:
        output+=1
print(output)

#282A. Bit++
n=int(input())
output=0
for i in range(n):
    op = input()
    if '--' in op:
        output -=1
    else:
        output +=1
print(output)

#96A. Football
inp=input()
for i in range(len(inp)):
    if inp[i:i+7]=='0000000':
        print('YES')
        break;
    elif inp[i:i+7]=='1111111':
        print('YES')
        break;
    elif i == len(inp)-1:
        print('NO')
        
#112A. Petya and Strings
l1=input().lower()
l2=input().lower()

alp='abcdefghijklmnopqrstuvwxyz'

for i in range(len(l1)):
    if alp.index(l1[i])>alp.index(l2[i]):
        print(1)
        break;
    elif alp.index(l1[i])<alp.index(l2[i]):
        print(-1)
        break;
    elif i == len(l1)-1:
        print(0)

#339A. Helpful Maths
lst=input()
if len(lst)==1:
    output = lst
else:
    lst=lst.split('+')
    while 0==0:
        for i in range(len(lst)-1):
            if int(lst[i]) > int(lst[i+1]):
                cons = lst[i]
                lst[i] = lst[i+1]
                lst[i+1] = cons
        count = 0
        for i in range(len(lst)-1):
            if lst[i]>lst[i+1]:
                break;
            elif i==len(lst)-2:
                count = 1
        if count == 1:
            break;
    output=lst[0]
    for i in lst[1:]:
        output += '+' + i
print(output)

#266A. Stones on the Table 
n=int(input())
s=input()
output = 0

for i in range(n-1):
    if s[i]==s[i+1]:
        output += 1
print(output)

#281A. Word Capitalization
alp='abcdefghijklmnopqrstuvwxyz'
ALP='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
s = input()
output = ALP[(alp+ALP).index(s[0])%26]
for i in s[1:]:
    output += i
print(output)

#116A. Team
n = int(input())
total = [0]
for i in range(n):
    a, b = map(int, input().split(' '))
    total.append(total[-1]-a)
    total.append(total[-1]+b)
print(max(total))

#263A. Beautiful Matrix


#158B. Taxi (예시 답은 맞게 나오는데 제출하면 wrong. 다시 풀어야 함.)
n = int(input())
s = input().split(' ')
lst = [int(i) for i in s]

n1 = lst.count(1)
n2 = lst.count(2)
n3 = lst.count(3)
n4 = lst.count(4)
output = n4
n4 = 0
min1 = min(n1, n3)
output += min1
n1 -= min1
n3 -= min1
int2 = int(n2/2)
output += int2
n2 -= 2*int2
if n1 == 0:
    output += n3
    if n2 == 1:
        output += 1
elif n1%4 == 0:
    output += n1/4
    if n2 == 1:
        output += 1
elif n1%4 == 3:
    output += int(n1/4)+1
else:
    output += int(n1/4)+1        

print(output)
    



