
l =[]
t = int(input())
for i in range(t+1):
    l.append([])
for i in range(t-1):
    n, m = map(int, input().split())
    l[n] += [m]
    l[m] += [n] 
ok = False
for i in l:
    if len(i) == t-1:
        ok = True
        break
if ok == True:
    print('Yes')
else:
    print('No')
"""
5
1 2
1 3
1 4
1 5
"""