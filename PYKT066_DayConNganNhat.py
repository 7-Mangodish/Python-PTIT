from math import *
from sys import stdin
def gcd(a, b):
    if a == 0: return b
    return gcd(b%a, a)

a =[]
while True:
    try: a += [int(x) for x in input().split()]
    except EOFError: break
t = a[0]
ind =1
for _ in range(t):
    n , k = a[ind], a[ind+1]
    ind +=2
    l =[]
    l.extend(a[ind:ind+n])
    ind +=n

    ans = 1001
    for i in range(n):
        tmp = l[i]
        for j in range(i, n):
            tmp = gcd(tmp, l[j])
            if(tmp == k):
                ans = min(ans, j-i+1)
                break
    if ans != 1001:
        print(ans)
    else:
        print(-1)
"""
3
8 3
6 9 7 10 12 24 36 27
4 3
2 4 6 8
4 6
1 2 3 6
"""