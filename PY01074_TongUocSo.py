from math import*

Nmax= 20**6+3
l=[0]*Nmax
l[0]=l[1]=0

def isPrime(n):
    if n<2:
        return False
    for i in range(2, isqrt(n)+1):
        if n%i ==0:
            return False
    return True

def sol(n):
    if n==1:
        return 0
    if isPrime(n):
        return n
    if n%2 == 0:
        if l[n//2]==0:
            l[n//2]= sol(n//2)
        return 2+l[n//2]
    if n%3 == 0:
        if l[n//3]==0:
            l[n//3]= sol(n//3)
        return 3+l[n//3]
    if n%5 == 0:
        if l[n//5]==0:
            l[n//5]= sol(n//5)
        return 5+l[n//5]
    if n%7 == 0:
        if l[n//7]==0:
            l[n//7]= sol(n//7)
        return 7+l[n//7]


if __name__ =='__main__':
    t= int(input())
    s= 0
    for _ in range(t):
        n= int(input())
        s+=sol(n)
    print(s)