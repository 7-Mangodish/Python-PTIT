
import math

class Athlete:
    def __init__(self, id, name, add, time):
        self.id = id
        self.name = name
        self.add = add
        self.time = time
        self.v = 0
        self.setV()

    def setV(self):
        self.v = round(120/self.time)
    
    def out(self):
        print(f'%s %s %s %d Km/h'%(self.id, self.name, self.add, self.v))

t = int(input())
l = []
for i in range(t):
    name = input()
    add = input()
    h, m = [int(x) for x in input().split(':')]
    h -= 6
    m /=60
    time = h + m
    id =''
    for j in add.split():
        id += j[0]
    for j in name.split():
        id += j[0]
    l.append(Athlete(id, name, add, time))

l = sorted(l, key=lambda x:x.time)
for i in l:
    i.out()
"""
3
Tran Vu Minh
Ha Noi
8:30
Vu Ngoc Hoang
Hoa Binh
8:20
Pham Dinh Tan
An Giang
8:45
"""