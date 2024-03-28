def check(a, b):
    for i in range(len(a)):
        if a[i] >b[i]:
            return False
    return True

t= int(input())
for _ in range(t):
    n= int(input())
    a=[int(x) for x in input().split()]
    b=[int(x) for x in input().split()]
    a.sort(); b.sort()
    if check(a, b):
        print('YES')
    else:
        print('NO')
"""
2
4
7 5 3 2
5 4 8 7
8
7 5 3 2 5 105 45 10
2 4 0 5 6 9 75 84
"""