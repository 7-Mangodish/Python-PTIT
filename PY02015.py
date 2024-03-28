from math import*
while True:
    l= [int(x) for x in input().split()]
    ok= False
    for i in l:
        if i!=0:
            ok=True
            break
    if  ok== False:
        break
    cnt=0
    while True:
        if l[0]==l[1]==l[2]==l[3]:
            break
        cnt+=1
        tmp=l[0]
        for i in range(0, 3, 1):
            l[i]= abs(l[i]- l[i+1])
        l[3]= abs(l[3]-tmp)       
    print(cnt)

