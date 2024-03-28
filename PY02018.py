t= int(input())
l= [int(x) for x in input().split()]
l.sort()
ans=-1
for i in range(len(l)-1):
    if l[i+1] - l[i] !=1:
        ans= l[i]+1
        break
if ans==-1:
    print(l[len(l)-1]+1)
else:
    print(ans)