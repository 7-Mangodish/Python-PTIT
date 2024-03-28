from math import*

def isPrime(n):
    if n<2:
        return False
    for i in range(2, isqrt(n)+1, ):
        if n%i==0:
            return False
    return True

def check(n):
    sum=0
    rev_n=0
    while n>0:
        tmp= n%10
        if isPrime(tmp)== False:
            return False
        rev_n= rev_n*10+tmp
        sum+=tmp
        n//=10
    if isPrime(sum)==False:
        return False
    if isPrime(rev_n)== False:
        return False
    return True

if __name__ =='__main__':
    t= int(input())
    for _ in range(t):
        n= int(input())
        if isPrime(n) and check(n):
            print('Yes')
        else:
            print('No')