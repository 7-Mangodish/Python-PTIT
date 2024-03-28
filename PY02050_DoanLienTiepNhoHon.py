t =int(input())
while t>0:
    n =int(input())
    l=[int(x) for x in input().split()]
    dp=[]

    for i in range(n):
        while len(dp)>0 and l[i]>=l[dp[-1]]:
            dp.pop()
        if len(dp)==0:
            print(i+1, end=' ')
        else:
            print(i-dp[-1], end=' ')
        dp.append(i)
    print()
    t-=1

"""
1
7
100 80 60 70 60 75 85
"""