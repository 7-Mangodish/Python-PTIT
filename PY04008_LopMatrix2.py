
class Matrix:
    def __init__(self, l, row, col):
        self.l = l
        self.row = row
        self.col = col
        
    def sol(self, o):
        for i in range(self.row):
            for j in range(self.row):
                x=0
                for k in range(self.col):
                    x += self.l[i][k]*o.l[k][j]
                print(x, end=' ')
            print()

t = int(input())
for _ in range(t):
    inp = []
    while(len(inp) < 2):
        tmp=[int(x) for x in input().split()]
        inp.extend(tmp)
    r, c= inp[0], inp[1]

    l=[]
    while(len(l) < r*c):
        l.extend(int(x) for x in input().split())
    # print(l)

    a=[]
    for i in range(r):
        tmp=[]
        for j in range(c):
            tmp.append(l[c*i+j])
        a.append(tmp)
    a_rev =[]
    for j in range(c):
        tmp=[]
        for i in range(r):
            tmp.append(a[i][j])
        a_rev.append(tmp)
    
    matrix1 = Matrix(a, r, c)
    matrix2 = Matrix(a_rev, c, r)
    matrix1.sol(matrix2)
"""
2
2  2
1  2
3  4
2 3
1 2 3
4 5 6
"""
