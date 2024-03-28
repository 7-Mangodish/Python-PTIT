from math import*

t= int(input())
for _ in range(t):
    n, d= map(int, input().split())
    a= [int(x) for x in input().split()]
    for i in range(d, n):
        print(a[i], end=' ')
    for i in range(d):
        print(a[i], end=' ')
    print()
"""
2
5 2
1 2 3 4 5 
10 3
2 4 6 8 10 12 14 16 18 20
"""