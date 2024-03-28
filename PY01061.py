from math import*

def IsPrime(n):
    if n<2:
        return False
    for i in range(2, isqrt(n)+1, 1):
        if n%i ==0:
            return False
    return True

if __name__ =='__main__':
    t= int(input())
    while t>0:
        s= input()
        a= int(s[:3])
        b= int(s[-3:])
        if IsPrime(a) and IsPrime(b):
            print('YES')
        else:
            print('NO')
