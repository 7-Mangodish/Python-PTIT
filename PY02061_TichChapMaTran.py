from math import*

def sol(a, kl, r, c):
    s= 0
    for i in range(3):
        for j in range(3):
            s+= a[r+i][c+j] * kl[i][j]
    return s
            
if __name__=='__main__':
    t= int(input())
    for _ in range(t):        
        a=[]
        n, m= map(int, input().split())
        for i in range(n):
            l= [int(x) for x in input().split()]
            a.append(l)
        kl= []
        for i in range(3):
            l= [int(x) for x in input().split()]
            kl.append(l)
        
        ans=0
        for i in range(n-2):
            for j in range(m-2):
                # print(i,j, sol(a, kl, i, j))
                ans+= sol(a, kl, i, j)
        print(ans)
"""
2
4 4
2 1 0 0
3 2 1 1
4 3 2 1
2 2 1 0
-1 -1 -1
-1 8 -1
-1 -1 -1
3 3
1 2 3
4 5 6
7 8 9
1 1 1
1 1 1
1 1 1
"""