p=[0]*100
for i in range(41):
    if i<=4: p[i]=2.5
    elif i>=5 and i <=6: p[i]=3.0
    elif i>=7 and i<=9: p[i]=3.5
    elif i >=10 and i <=12: p[i]=4.0
    elif i >=13 and i<=15: p[i]=4.5
    elif i >=16 and i<=19: p[i]=5.0
    elif i >=20 and i <=22: p[i]=5.5
    elif i >=23 and i <=26: p[i]=6.0
    elif i >=27 and i <=29: p[i]=6.5
    elif i >=30 and i <=32: p[i]=7.0
    elif i >=33 and i <=34: p[i]=7.5
    elif i >=35 and i <=36: p[i]=8.0
    elif i >=37 and i <=38: p[i]=8.5
    else :p[i]=9.0
t= int(input())
for _ in range(t):
    l=[float(x) for x in input().split()]
    sum = p[ int(l[0]) ]+ p[ int(l[1]) ] + l[2] + l[3]
    ans= sum/4 
    if ans - int(ans) >=0.75:
        ans = int(ans) +1.0
    elif ans - int(ans) >=0.25:
        ans = int(ans) +0.5
    else: ans=int(ans) + 0.0
    print(ans)


"""
2
15 25 5.0 5.5
22 32 6.0 6.0
"""