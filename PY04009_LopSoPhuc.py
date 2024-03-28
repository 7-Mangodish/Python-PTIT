
class ComplexNum:
    def __init__(self, re, im):
        self.re = re
        self.im = im
    
    def add(self, o):
        x = self.re + o.re 
        y = self.im + o.im 
        return ComplexNum(x, y)
    
    def multiply(self, o):
        x = self.re * o.re 
        y1 = self.re * o.im 
        y2 = self.im * o.re 
        z = self.im * o.im 

        y = y1 + y2
        x = x + -z
        return ComplexNum(x, y)

    def out(self):
        print(f'%d + %di'%(self.re, self.im), sep='', end='')

t = int(input())
for _ in range(t):
    l = [int(x) for x in input().split()]
    a = ComplexNum(l[0], l[1])
    b = ComplexNum(l[2], l[3])
    
    tmp= a.add(b)
    c = tmp.multiply(a)
    d = tmp.multiply(tmp)
    c.out()
    print(', ', sep='', end='')
    d.out()
    print()

"""
3
1 2 3 4
2 3 4 5
1 -2 5 -6
"""