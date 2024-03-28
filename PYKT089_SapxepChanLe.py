t= int(input())
arr= []
while True:
    if len(arr) == t:
        break
    ip= [int(x) for x in input().split()]
    for x in ip:
        arr.append(x)
a=[]
b=[]
for i in arr:
    if i%2==0:
        a.append(i)
    else:
        b.append(i)
a.sort()
b.sort(reverse= True)
ind1=0
ind2=0
for i in range(len(arr)):
    if arr[i]%2 ==0:
        print(a[ind1],end=' ')
        ind1+=1
    else:
        print(b[ind2], end=' ')
        ind2+=1
        

"""
10
1 2 3 4 5 6 7 7 9 6
3
2 4 6
"""