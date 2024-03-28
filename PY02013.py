
while True:
    n=int(input())
    if n==0:
        break
    l=[]
    l+=[n]
    while l[len(l)-1]!=1:
        tmp= l[len(l)-1]
        if tmp%2==1:
            l.append(tmp*3+1)
        else:
            l.append(tmp//2)
    print(len(l))
    