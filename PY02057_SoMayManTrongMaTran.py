
n, m= map(int, input().split())
a=[]
gMax= 0
gMin= 10**6
for i in range(n):
    l=[int(x) for x in input().split()]
    tmp1 = max(l)
    gMax= max(gMax, tmp1)
    tmp2= min(l)
    gMin= min(gMin, tmp2)
    a.append(l)

ok= False
for i in range(n):
    for j in range(m):
        if a[i][j] != gMax - gMin:
            a[i][j]=0
        else:
            if ok== False:
                ok= True
if ok==False:
    print('NOT FOUND')
else:
    print(gMax - gMin)
    for i in range(n):
        for j in range(m):
            if a[i][j] !=0:
                print('Vi tri [%d][%d]'%(i,j))
"""
6 4
23 21 77 10
13 13 22 14
28 67 28 23
29 77 11 67
16 51 24 21
13 25 77 77
3 3
1 1 1
1 1 1
1 1 1


"""