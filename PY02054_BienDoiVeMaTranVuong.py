
n, m= map(int, input().split())
a=[]
ans=[]
for i in range(n):
    a.append([int(x) for x in input().split()])
if n>m:
    tmp= n-m
    for i in range(n):
        if i%2 ==1:
            ans.append(a[i])
        else:
            if tmp>0:
                tmp-=1
            else:
                ans.append(a[i])
elif m>n:
    cnt= m-n
    for i in range(n):
        tmp= cnt
        l=[]
        for j in range(m):
            if j%2==0:
                l.append(a[i][j])
            else:
                if tmp>0:
                    tmp-=1
                else:
                    l.append(a[i][j])
        ans.append(l)
else:
    for i in a:
        ans.append(i)
for i in ans:
    for j in i:
        print(j, end=' ')
    print()
"""
6 4
2 8 7 6
6 3 2 6
7 2 2 8
9 9 9 8
9 6 6 3
7 7 4 9
4 6
2 8 7 6 4 3
6 3 2 6 7 2
7 2 2 8 9 1
9 9 9 8 0 7
3 3
1 2 3
4 5 6
7 8 9

"""