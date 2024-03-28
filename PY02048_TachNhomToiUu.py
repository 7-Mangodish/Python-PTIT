
Nmax = 10**6 +3
n, k= map(int, input().split())
a= [int(x) for x in input().split()]
a.sort()
used=[0]*Nmax
ans=0
for i in range(len(a)):
    if used[a[i]] ==0:
        ans+=1
        used[a[i]] =1
        j= i+1
        while j<len(a) and a[j] - a[j-1] <=k:
            used[a[j]]=1
            j+=1
print(ans)
"""
7 1
2 6 1 7 3 4 9
"""