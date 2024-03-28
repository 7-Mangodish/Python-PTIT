a=[]
n=0; m=0
directX=[-1, -1, -1, 0, 0, 1, 1, 1]
directY=[-1, 0, 1, -1, 1, -1, 0, 1]
 
if __name__=='__main__':
    n, m= map(int, input().split())
    for i in range(n):
        l=[int(x) for x in input().split()]
        a.append(l)
    ans=0
    q= []
    for i in range(n):
        for j in range(m):
            if a[i][j]==-1:
                q.append([i,j])
    while len(q) >0:
        top= q.pop(0)
        for i in range(8):
            x= top[0]+directX[i]; y= top[1] + directY[i]
            if x >=0 and x<n and y >=0 and y <m:
                ans += a[x][y]
                a[x][y] =0 
    print(ans)
"""
5 6
1 1 0 1 1 1
1 1 1 5 1 2
0 0 0 0 1 3
1 0 2 1 1 4
1 1 1 1 1 -1

4 4
1 1 0 1
2 -1 4 5
0 0 0 0
1 0 2 1
"""
