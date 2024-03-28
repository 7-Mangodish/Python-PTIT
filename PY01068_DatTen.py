import itertools as it

n, k= map(int, input().split())
l=set(x for x in input().split())
l= list(l)
l.sort()
ans=list(it.combinations(l,k))
for i in ans:
    for j in i:
        print(j, end=' ')
    print()
"""
6 3
DONG TAY NAM BAC TAY BAC
"""