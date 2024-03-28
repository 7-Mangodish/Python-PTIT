n =int(input())
l= [int(x) for x in input().split()]
cnt=0
for i in range(n-1):
    for j in range(i+1, n):
        if l[i] >l[j]:
            cnt+=1
            # print(l[i], l[j])
print(cnt)
