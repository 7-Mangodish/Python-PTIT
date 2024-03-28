from math import*

def IsPrime(n):
    if n<2:
        return False
    for i in range(2, isqrt(n)+1, 1):
        if n%i ==0:
            return False
    return True

def check(s):
    ind=0
    for i in range(len(s)):
        if IsPrime(int(s[i])):
            ind+=1
        else:
            ind-=1
    if ind>0:
        return True
    return False

if __name__=='__main__':
    t =int(input())
    while t>0:
        s= input()
        if IsPrime(len(s)) and check(s):
            print('YES')
        else:
            print('NO')
        t-=1

