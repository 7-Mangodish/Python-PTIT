n,m= map(int, input().split())
x= set(int(x) for x in input().split())
y= set(int(x) for x in input().split())
tmp= x-y
if len(tmp) ==0:
    print('YES')
else:
    print('NO')
"""
12 18
1 2 3 4 5 1 2 3 5 4 1 2
1 1 1 1 1 1 1 1 1 2 3 4 5 5 5 5 5 5
"""