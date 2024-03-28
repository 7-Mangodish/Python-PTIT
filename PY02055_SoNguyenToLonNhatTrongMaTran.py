from math import*

def isPrime(n):
    if n<2:
        return False
    for i in range(2, isqrt(n)+1):
        if n%i ==0:
            return False
    return True

n, m= map(int, input().split())
a=[]
for i in range(n):
    a.append([int(x) for x in input().split()])
g=0
for i in range(n):
    for j in range(m):
        if isPrime(a[i][j]) == False:
            a[i][j]= 0
        else:
            g= max(g, a[i][j])
# print(a)

if g== 0:
    print('NOT FOUND')
else:
    print(g)
    for i in range(n):
        for j in range(m):
            if a[i][j]==g:
                print('Vi tri [%d][%d]'%(i,j))

"""
6 4
23 21 26 10
13 13 22 14
28 29 28 23
29 19 11 19
16 26 24 21
13 25 21 29
3 4
4 4 4 7 
4 4 4 6
4 4 4 4

Vi tri [2][1]
Vi tri [3][0]
Vi tri [5][3]
"""
