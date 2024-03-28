t= int(input())
for _ in range(t):
    n, p=map(int, input().split())
    ind=1
    ans=0
    while n//(p**ind) >=1:
        ans += (n//(p**ind))
        ind+=1
    print(ans)
"""
3
62  7
76  2
3  5
"""
