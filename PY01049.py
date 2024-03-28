from math import*

def IsPrime(n):
    if n<2:
        return False
    for i in range(2, isqrt(n)+1, 1):
        if n%i==0:
            return False
    return True

if __name__ == '__main__':
    t= int(input())
    while t>0:
        s= input()
        chk=0
        for i in range(len(s)):
            if IsPrime(int(s[i])):
                chk+=1
            else:
                chk-=1
        if IsPrime(len(s)) and chk>0:
            print('YES')
        else:
            print('NO')
        t-=1