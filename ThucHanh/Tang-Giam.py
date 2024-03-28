
t = int(input())
for _ in range(t):
    a = list()
    b = list()
    n = int(input())
    for i in range(n):
        x,y = map(float, input().split())
        a.append(x)
        b.append(y)
    dp = [1]*(n)
    for i in range(n):
        for j in range(i):
            if a[i] > a[j] and b[i] < b[j]:
                dp[i] = max(dp[i], dp[j]+1)
    print(max(dp))

"""
3
2
1.0 1.0
1.5 0.0
3
1.0 1.0
1.0 1.0
1.0 1.0
6
1.5 9.0
2.0 2.0
2.5 6.0
3.0 5.0
4.0 2.0
10.0 5.5
"""