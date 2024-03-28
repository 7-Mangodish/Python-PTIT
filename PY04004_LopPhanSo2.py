from math import *
class ps:
    def __init__(self, tu, mau):
        self.tu = tu
        self.mau = mau
    
    def simple(self):
        n = gcd(self.tu, self.mau)
        self.tu //= n
        self.mau //= n
    
    def sum (self, o):
        self.tu = self.tu * o.mau + o.tu*self.mau
        self.mau = self.mau *o.mau
        self.simple()
    

# main
l = input().split()
x = ps(int(l[0]), int(l[1]))
y = ps(int(l[2]), int(l[3]))
x.sum(y)
print(f'{x.tu}/{x.mau}')

#123 456 12 34