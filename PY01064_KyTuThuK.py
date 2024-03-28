def sol(n, k):
    m= 2**(n-1)
    if k == m:
        return chr(64+n)
    if k<m:
        return sol(n-1,k)
    return sol(n-1, k-m)

t= int(input())
for _ in range(t):
    n, k= map(int, input().split())
    print(sol(n,k))
"""
2
3 2
4 8
"""