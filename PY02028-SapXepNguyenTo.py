from math import*

def isPrime(n):
    if n<2:
        return False
    for i in range(2, isqrt(n)+1):
        if n%i==0:
            return False
    return True

t= int(input())
l=[int(x) for x in input().split()]
pos=[0]*len(l)
prime=[]
for i in range(len(l)):
    if isPrime(l[i]):
        pos[i]=1
        prime.append(l[i])
prime.sort()
ind=0
for i in range(len(l)):
    if pos[i]== 0:
        print(l[i], end=' ')
    else:
        print(prime[ind], end=' ')
        ind+=1
"""
8
4 6 3 8 7 2 5 9
"""