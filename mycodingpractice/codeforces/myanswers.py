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

#158B. Taxi
n = int(input())
s = input().split(' ')
lst = [int(i) for i in s]

n1 = lst.count(1)
n2 = lst.count(2)
n3 = lst.count(3)
n4 = lst.count(4)
output4 = n4
n4 = 0
output2, n2 = divmod(n2, 2)
if n2 == 1:
    n1 -= 2
    output2 += 1
min13=min(n1, n3)
output13 = min13
n1 -= min13
n3 -= min13
if n1 == 0:
    output13 += n3
else:
    div, mod = divmod(n1, 4)
    if mod == 0:
        output13 += div
    else:
        output13 += div + 1
output = sum([output4, output2, output13])
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
a, b = 0, 0
for i in range(5):
    c1, c2, c3, c4, c5 = map(int, input().split(' '))
    lst = [c1, c2, c3, c4, c5]
    if sum(lst)==1:
        a = i+1; b = lst.index(1)+1
print(abs(a-3)+abs(b-3))

#58A. Chat room
s = input()
n = len(s)
result = False
for i in range(n):
    if s[i] =='h':
        for j in range(n-i-1):
            if s[i+j+1] =='e':
                for k in range(n-i-j-2):
                    if s[i+j+k+2] =='l':
                        for l in range(n-i-j-k-3):
                            if s[i+j+k+l+3] == 'l':
                                for m in range(n-i-j-k-l-4):
                                    if s[i+j+k+l+m+4] =='o':
                                        result = True
                                        print('YES')
                                        break;
                                if result == True:
                                    break;
                        if result == True:
                            break;
                if result == True:
                    break;
        if result == True:
            break;
    elif i == n-1:
        print('NO')

#131A. cAPS lOCK (wrong)
s = input()
alp='abcdefghijklmnopqrstuvwxyz'
ALP='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

if len(s) == 1:
    if s in alp:
        print(ALP[alp.index(s)])
    else:
        print(s)
elif s[0] in alp:
    for i in range(len(s)-1):
        if s[i+1] in ALP:
            if i == len(s)-2:
                result = ALP[alp.index(s[0])]
                for j in s[1:]:
                    result += alp[ALP.index(j)]
                print(result)
                break;
        else:
            print(s)
            break;
elif s[1] in ALP:
    for i in range(len(s)-2):
        if s[i+2] in ALP:
            if i  == len(s)-3:
                result = s[0]
                for j in s[1:]:
                    result += alp[ALP.index(j)]
                print(result)
                break;
        else:
            print(s)
            break;
else:
    print(s)
        
