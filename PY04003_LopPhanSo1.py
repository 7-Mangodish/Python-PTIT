from math import *

class ps:
    def __init__(self, tu, mau):
        self.tu = tu
        self.mau = mau
    
    def simple(self):
        n = gcd(self.tu, self.mau)
        self.tu //= n
        self.mau //= n
        return f'{self.tu}/{self.mau}'

#main
x, y= map(int, input().split())
n = ps(x, y)
print(n.simple())