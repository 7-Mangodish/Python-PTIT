from math import *

def IsPrime(n):
    if n<2:
        return False
    for i in range(2, isqrt(n)+1, 1):
        if n%i==0:
            return False
    return True

def gcd(a, b):
    while b!=0:
        tmp=a%b
        a=b
        b=tmp
    return a

    

if __name__ == '__main__':
     
    t =int(input())
    while t>0:
        n =int(input())
        cnt=0
        for i in range(1, n, 1):
            if gcd(i, n)==1:
                cnt+=1
        if IsPrime(cnt):
            print('YES')
        else:
            print('NO')
        t-=1

