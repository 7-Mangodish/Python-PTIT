n = int(input())
l= []
for i in range(n):
    l.append([int(x) for x in input().split()])
sumTop=0
sumBelow=0
for i in range(n):
    for j in range( n-i-1):
        sumTop+=l[i][j]
    for j in range (n-i, n):
        sumBelow+= l[i][j]
k =int(input())
if abs(sumTop -sumBelow) <=k:
    print('YES')
else:
    print('NO')
print(abs(sumTop - sumBelow))
"""
5
2 8 10 6 7
6 3 2 6 9
10 2 6 2 8
9 9 7 9 8
9 6 5 6 9
5
"""