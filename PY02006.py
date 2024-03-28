t= int(input())
while t >0:
    n =int(input())
    l1= [int(x) for x in input().split()]
    l2= [int(x) for x in input().split()]
    l1.sort()
    l2.sort()
    ok= True
    for i in range (len(l1)):
        if l1[i] >l2[i]:
            ok=False
            break
    if ok:
        print('YES')
    else:
        print('NO')
    t-=1
    