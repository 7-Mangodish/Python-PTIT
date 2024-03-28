t= int(input())
for _ in range(t):
    a=list(input())
    l=[]
    cnt=0
    for i in a:
        if len(l)==0:
            l.append(i)
            cnt=1
        else:
            if i in l:
                cnt+=1
            else:
                print(cnt, l[-1], sep='', end='')
                l.clear()
                l.append(i)
                cnt=1
    if len(l)!=0:
        print(cnt, l[-1],sep='', end='')
    print()
"""
3
AACDDPQ
11111147g
1111111111
"""