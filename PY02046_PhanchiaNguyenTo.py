from math import *

def isPrime(n):
    if n<2 :
        return False
    for i in range(2,isqrt(n)+1):
        if n%i ==0:
            return False
    return True

def check(a):
    suml= 0
    sumr= 0
    for i in a:
        sumr +=i
    for i in range(len(a)):
        suml +=a[i]; sumr -=a[i]
        if isPrime(suml) and isPrime(sumr):
            return i
    return -1

t= int(input())
l= [int(x) for x in input().split()]
a= list()
for i in l:
    if i not in a:
        a.append(i)
if check(a) == -1:
    print('NOT FOUND')
else:
    print(check(a))

"""
10
3 6 7 3 4 7 3 6 4 4
10
3 6 7 3 5 7 3 6 6 7
"""

