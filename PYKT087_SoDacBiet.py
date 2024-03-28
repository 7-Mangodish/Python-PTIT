
mod = 10 ** 9 + 7

def sol(n, k):
    ans, p = 0, 1
    while k > 0:
        if k % 2 == 1:
            ans += p
            ans %= mod
        p *= n
        k //= 2
    return ans

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    print(sol(n,k))
"""
3
3 4
2 12
105 564
"""