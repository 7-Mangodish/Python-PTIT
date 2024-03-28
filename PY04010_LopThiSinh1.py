
class ThiSinh:
    def __init__(self, name, date, p1, p2, p3):
        self.name = name
        self.date = date
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
    
    def out(self):
        print(self.name, self.date, f'%.1f'%(self.p1 + self.p2 + self.p3))

name = input()
date = input()
p1 = float(input())
p2 = float(input())
p3 = float(input())
a = ThiSinh(name, date, p1, p2, p3)
a.out()
"""
Nguyen Hoang Ha
11/10/2001
4.5
10.0
5.5
"""