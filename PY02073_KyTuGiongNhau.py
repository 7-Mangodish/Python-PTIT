
t = int(input())
for _ in range(t):
    n =int(input())
    l = [105]*(n+5)
    x, y ,z = map(int, input().split())
    l[0] =0
    for i in range(1, n+1):
        l[i] = min(l[i], l[i-1]+x)
        if i %2 ==0:
            l[i] = min(l[i], l[i//2]+z)
        l[i-1] = min(l[i-1], l[i]+y)
    # print(l)
    print(l[n])