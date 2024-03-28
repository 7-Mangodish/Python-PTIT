import math as mh

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def distance(self, o):
        ans= mh.sqrt((self.x - o.x)*(self.x -  o.x) + (self.y - o.y)*(self.y -  o.y) )
        return ans
    
class Triangle:
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
    def sol(self):
        a = self.p1.distance(self.p2)
        b = self.p2.distance(self.p3)
        c = self.p1.distance(self.p3)
        if b+c<= a or a+c <= b or a+b<= c: print('INVALID')
        else :
            d = mh.sqrt((a + b + c) * (a + b - c) * (a - b + c) * (-a + b + c)) / 4
            ans = mh.sqrt(( a+b+c) * (a+b-c) * (a-b+c) * (-a+b+c)) / 4
            print('%.2f'%ans)


t = int(input())
l=[]
for i in range(t):
    a = [float(x) for x in input().split()]
    l +=a

# print(l)
ind =0
for i in range(t):
    p1 = Point(l[ind+0], l[ind+1])
    p2 = Point(l[ind+2], l[ind+3])
    p3 = Point(l[ind+4], l[ind+5])
    a = Triangle(p1, p2, p3)
    a.sol()
    ind +=6
"""
3
0 0 0 5 0 199
1 1 1 1 1 1
0 2.1 2 5 5 2.5
"""