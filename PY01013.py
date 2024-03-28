from math import*

def gcd(a, b):
    if(b==0):
        return a
    return gcd(b, a%b)

def IsPrime(a):
    if (a<2):
        return False
    for i in range(2, isqrt(a)+1, 1):
        if(a%i==0):
            return False
    return True

if __name__=='__main__':
    t=int(input())
    while(t>0):
        x, y= map(int, input().split())
        tmp= gcd(x,y)
        s=0
        for i in str(tmp):
            s+=int(i)
        print(tmp, s)
        if(IsPrime(s)):
            print('YES')
        else:
            print('NO')
        t-=1

