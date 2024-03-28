
def check(d, n):
    for i in d.keys():
        print(i, d.get(i))
        if d.get(i) == n-1:
            return True
    return False

d = dict()
t = int(input())
for _ in range(t-1):
    n, m = map(int, input().split())
    if n not in d.keys():
        d[n] =1
    else:
        d[n] = d[n]+1
    if m not in d.keys():
        d[m] = 1
    else:
        d[m] = d[m] +1

def check():
    for i in d.keys():
        if d[i] == t-1:
            return True
    return False

if check():
    print('Yes')
else:
    print('No')
"""
5
1 2
1 3
1 4
3 2
"""