import math

t = int(input())
for _ in range(t):
    s = input()
    l = len(s)
    n = int(s)
    ind = 1
    while ind < l:
        tmp = n /(10 ** ind)
        n = n//(10 ** ind)
        if tmp>= n + 0.5:
            n+=1
        n *= (10 ** ind)
        ind +=1
    print(n)
        
"""
7
15
14
5
99
12345678
44444445
1445
"""