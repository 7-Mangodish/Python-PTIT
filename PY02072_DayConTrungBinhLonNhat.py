from math import *

n= int(input())
a= [float(x) for x in input().split()]
dp= [x for x in a]
length= [1]*len(a)
for i in range(1, len(a)):
    cnt= length[i-1] + 1
    if (dp[i-1]+a[i])/cnt > a[i]:
        dp[i]= (dp[i-1]+a[i])/2
        length[i]= length[i-1] + 1
print(dp)
print(length)
"""
5
5 1 6 7 2
"""
    