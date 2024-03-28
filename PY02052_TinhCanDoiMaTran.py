t= int(input())
a=[]
for i in range(t):
    a.append([int(x) for x in input().split()])
sum1=0
sum2=0
for i in range(t):
    for j in range(i+1, t):
        sum1 +=a[i][j]
for i in range(t):
    for j in range(i):
        sum2 +=a[i][j]
k= int(input())
if abs(sum1 - sum2) <=k:
    print('YES')
else:
    print('NO') 
print(abs(sum1-sum2))
"""
5
2 8 10 6 7
6 3 2 6 9
10 2 6 2 8
9 9 7 9 8
9 6 5 6 9
5
"""