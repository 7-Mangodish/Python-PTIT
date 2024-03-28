
t = int(input())
l=[]
sum =[]
for i in range(t):
    a = [int(x) for x in input().split()]
    tmp =0
    for x in a:
        tmp+=x
    sum.append(tmp)
    l.append(a)

y =[]
for i in range(len(sum) -1):
    y.append((sum[i] - sum[i+1]) //2)

ans =[]
ans.append((l[0][1] + y[0])//2)
for i in y:
    ans.append(ans[-1] - i)

for i in ans:
    print(i, end=' ')
"""
2
0 2
2 0
4
0 3 6 7
3 0 5 6
6 5 0 9
7 6 9 0
"""