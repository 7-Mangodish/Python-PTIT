n= int(input())
ans= 0
for i in range(n):
    l= [int(x) for x in input().split()]
    cnt= 0
    for i in l:
        if i==1:
            cnt+=1
    if cnt > n//2:
        ans+=1
print(ans)


###