from math import*
t= int(input())
a= [int(x) for x in input().split()]
ts=[0]*t
for i in range(t):
    for j in range(t):
        if i!=j:
            ts[i]+= abs(a[i]- a[j])
minVal= min(ts)
ind = ts.index(minVal)
print(minVal, a[ind])
"""
8
13 5 8 7 9 15 26 34
"""