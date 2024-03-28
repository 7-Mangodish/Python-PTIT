

n, m =map(int, input().split())
s1 = set(int(x) for x in input().split())
s2 = set(int(x) for x in input().split())
s = {}
s = s1 - s2
if len(s) ==0:
    print('YES')
else:
    print('NO')
"""
12 18
1 2 3 4 5 1 2 3 5 4 1 2
1 1 1 1 1 1 1 1 1 2 3 4 5 5 5 5 5 5
"""