
def check(s):
    if len(s)<2:
        return False
    l=0
    r= len(s)-1
    while l<r:
        if s[l]!=s[r]:
            return False
        l+=1
        r-=1
    return True

n, m= map(int, input().split())
a=[]
for i in range(n):
    a.append([int(x) for x in input().split()])
g= 0
for i in range(n):
    for j in range(m):
        if check(str(a[i][j])) == False:
            a[i][j]=0
        else:
            g= max(g, a[i][j])
if g== 0:
    print('NOT FOUND')
else:
    print(g)
    for i in range(n):
        for j in range(m):
            if a[i][j] == g:
                print('Vi tri [%d][%d]'%(i,j))
        
"""
6 4
23 21 77 10
13 13 22 14
28 29 28 23
29 77 11 19
16 26 24 21
13 25 77 77
6 4
23 21 77 1331
13 13 22 14
28 29 28 23
29 77 11 19
16 26 24 21
13 25 77 77
3 3
1 2 3
1 2 3
1 2 3
3 3
10 12 13
10 12 10
10 10 10
"""