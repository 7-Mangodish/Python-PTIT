t= int(input())
l=[]
l.append(0); l.append(1)
for i in range(2,93):
    n= len(l)
    l.append(l[n-1] + l[n-2])
while t>0:
    a, b= map(int, input().split())
    for i in range(a, b+1, 1):
        print(l[i], sep =' ', end=" ")
    print()
    t-=1
    