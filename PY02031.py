from math import*

def IsPrime(n):
    if n<2:
        return False
    for i in range(2, isqrt(n)+1):
        if n%i==0:
            return False
    return True

if __name__ == '__main__':
    a=[]
    n, m= map(int, input().split())
    for i in range(0, n):
        tmp= list(map(int, input().split()))
        a.append(tmp)
    for i in range(0, n):
        for j in range(0, m):
            if IsPrime(a[i][j]):
                a[i][j]= 1
            else:
                a[i][j]= 0
    for i in a:
        print(*i)
            
