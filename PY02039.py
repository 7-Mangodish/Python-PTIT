n = int(input())
l= []
for i in range(n):
    l.append([int(x) for x in input().split()])
sumTop=0
sumBelow=0
for i in range(n):
    for j in range(i+1, n):
        sumTop+=l[i][j]
    for j in range (i):
        sumBelow+= l[i][j]
k =int(input())
if abs(sumTop -sumBelow) <=k:
    print('YES')
else:
    print('NO')
print(abs(sumTop - sumBelow))
###

###