t= int(input())
for _  in range(t):
    n= int(input())
    a= [int(x) for x in input().split()]
    ind= 0
    maxL= 0
    minR= 0
    ans= 0
    for i in range(0, len(a)-1):
        if i==0:
            minR= min(a[i+1:])
        else:
            maxL= max(a[:i])
            minR= min(a[i+1:])
        # print(maxL, minR)
        if maxL <= a[i] and a[i] < minR:
            ans+=1
    ans+=1
    print(ans)
"""
3
3
1 1 1
3
1 2 3
7
2 1 3 4 6 5 7
"""
