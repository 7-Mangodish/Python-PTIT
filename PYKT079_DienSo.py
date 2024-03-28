t= int(input())
for _ in range(t):
    n= int(input())
    l={int(x) for x in input().split()}
    right= max(l); left= min(l)
    ans= (right-left+1)- len(l)
    print(ans)
"""
2
5
4 5 3 8 6
3
2 1 3
"""