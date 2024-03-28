from math import *

n= int(input())
l=[]
for i in range(n):
    l.append(list(input()))
ans=0
for i in l:
    tmp= i.count('C')
    ans+= comb(tmp,2)
for i in range(len(l)):
    tmp =0
    for j in range(len(l)):
        if l[j][i] =='C':
            tmp+=1
    ans += comb(tmp,2)
print(ans)

"""
4
CC..
C..C
.CC.
.CC.
"""
