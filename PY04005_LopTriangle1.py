import math as mh

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def distance(self, o):
        ans= mh.sqrt((self.x - o.x)*(self.x -  o.x) + (self.y - o.y)*(self.y -  o.y) )
        return ans
    
#main
t= int(input())
l =list()
for _ in range(t):
    a= [float(x) for x in input().split()]
    l.extend(a)

    # print(a, b, c)


for i in range(t):
    ind = 6*i
    p1 = Point(l[ind+0], l[ind+1])
    p2 = Point(l[ind+2], l[ind+3])
    p3 = Point(l[ind+4], l[ind+5])
    a = p1.distance(p2)
    b = p2.distance(p3)
    c = p1.distance(p3)
    if b +c<= a or a+c <= b or a+b<= c:
        print('INVALID')
    else:
        print('%.3f'%(a+b+c))

"""
3
0 0 0 5 0 199
1 1 1 1 1 1
0 0 0 5 5 0
"""