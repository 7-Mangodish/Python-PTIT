import math as mh
from decimal import *

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def distance(self, o):
        ans= mh.sqrt((self.x - o.x)*(self.x -  o.x) + (self.y - o.y)*(self.y -  o.y) )
        return '%.4f'% ans
    
#--Main 
if __name__ == '__main__':
    t = int(input())
    while t > 0:
        arr = input().split()
        p1 = Point(Decimal(arr[0]), Decimal(arr[1]))
        p2 = Point(Decimal(arr[2]), Decimal(arr[3]))
        print(p1.distance(p2))
        t -= 1
"""
2
0 0 0 5
0 199 5 6
"""