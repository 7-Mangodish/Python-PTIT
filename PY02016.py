t= int(input())
while t>0:
    n= int(input())
    l=[0]*(10**6+2)
    for x in input().split():
        l[int(x)]+=1
    ts=0
    ans=0
    for i in range(len(l)):
        if l[i]>ts:
            ts= l[i]
            ans= i
    if ts > (n//2):
        print(ans)
    else:
        print('NO')
    t-=1
