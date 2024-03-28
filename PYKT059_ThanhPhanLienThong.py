
n, m , u = [int(x) for x in input().split()]
# Nhap
a=[]
used = [0] * (n+1)
for i in range(n+1):
    a.append([])
for i in range(m):
    x, y = map(int, input().split())
    a[x].append(y)
    a[y].append(x)
# Ham DFS
def dfs(u):
    used[u] = 1 # Danh dau la da tham
    for v in a[u]:
        if used[v] == 0:
            dfs(v)

# Duyet tai x de tim thanh phan lien thong cua x
dfs(u)
for i in range(1, len(used)):
    if used[i] == 0:
        print(i)
"""
6 4 2
1 3
2 3
1 2
4 5
"""