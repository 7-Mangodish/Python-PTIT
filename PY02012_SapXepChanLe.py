
n=int(input())
a=[]
while len(a)<n:
    l= [int(x) for x in input().split()]
    a.extend(l)

even=[]
odd=[]
for i in a:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
even.sort()
odd.sort(reverse=True)

ind1=0
ind2=0
for i in a:
    if i%2==0:
        print(even[ind1], end=' ')
        ind1+=1
    else:
        print(odd[ind2], end=' ')
        ind2+=1


"""
10
1 2 3 4 5 6 7 7 9 6
"""
