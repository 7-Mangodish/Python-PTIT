
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
    r, c = map(int, input().split())
    l=[]
    for i in range(r):
        l.append([int(x)  for x in input().split()])
    matrix1 = Matrix(l, r, c)

    l1=[]
    for j in range(c):
        x=[]
        for i in range(r):
            x.append(matrix1.l[i][j])
        l1.append(x)
    matrix2= Matrix(l1, r, c)
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