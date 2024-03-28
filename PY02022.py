from math import*

def IsPrime(n):
    if n<2:
        return False
    for i in range(2, isqrt	(n)+1):
        if n%i==0:
            return False
    return True

if __name__=='__main__':
    n= int(input())
    l= [int(x) for x in input().split()]
    ts=[0]*(10**6+2)
    for i in l:
        if IsPrime(i):
            ts[i]+=1
    for i in l:
        if ts[i]!=0:
            print(i, ts[i])
            ts[i]=0
    