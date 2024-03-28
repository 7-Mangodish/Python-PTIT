from math import*

def isPrime(n):
    if n<2:
        return False
    for i in range(2, isqrt(n)+1):
        if n%i==0:
            return False
    return True

n= int(input())
a= [int(x) for x in input().split()]
l=[]
for i in a:
    if i not in l:
        l.append(i)
sumL=0
sumR=0
for i in range(0, len(l)):
    sumR+=l[i]
ans=-1
for i in range(0, len(l)):
    sumL+= l[i]; sumR -=l[i] 
    if isPrime(sumL) and isPrime(sumR):
        ans=i
        break
if ans== -1:
    print('NOT FOUND')
else:
    print(ans)
"""
10
3 6 7 3 4 7 3 6 4 4
10
3 6 7 3 5 7 3 6 6 7
"""