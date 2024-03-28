t= int(input())
while t>0:
    n =int(input())
    l =[0]*1005
    for i in range(n):
        tmp =int(input())
        l[tmp]+=1
    key= 0
    ans=0
    for i in range(1001):
        if l[i]!=0 and l[i] >key:
            ans=i
            key=l[i]
    print(ans)
    t-=1