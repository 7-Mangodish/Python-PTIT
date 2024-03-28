from math import*

n= int(input())
l= [int(x) for x in input().split()]
l.sort()
for i in range(len(l)-1):
    for j in range(i+1, len(l)):
        if gcd(l[i], l[j])==1:
            print(l[i], l[j], end=' ')
            print()
