import math

def IsPrime(n):
    if n<2:
        return False
    for i in range(2, math.isqrt(n)+1, 1):
        if n%i==0:
            return False
    return True

if __name__ =='__main__':
    t= int(input())
    while t>0:
        s=input()
        n= int(s[-4:])
        if IsPrime(n):
            print('YES')
        else:
            print('NO')
        
