import functools as f 

def cmp(o1, o2):
    if o1.total() > o2.total():
        return -1
    return 1


class SP:
    def __init__(self, id, name, cnt, pr, ck):
        self.id = id
        self.name = name
        self.cnt = cnt
        self.pr = pr
        self.ck = ck
    
    def total(self):
        return self.cnt * self.pr - self.ck
    
    def out(self):
        print(self.id, self.name, self.cnt, self.pr, self.ck , self.total())
t = int(input())
l =[]
for _ in range(t):
    id = input()
    name = input()
    cnt = int(input())
    pr = int(input())
    ck = int(input())
    l.append(SP(id, name, cnt, pr, ck))

l.sort(key = f.cmp_to_key(cmp))
for i in l:
    i.out()

"""
3
ML01
May lanh SANYO
12
4000000
2400000
ML02
May lanh HITACHI
4
2550000000
0
ML03
May lanh NATIONAL
5
3000000
150000
"""