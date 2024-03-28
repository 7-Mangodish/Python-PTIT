
class Bill:
    def __init__(self, id, name, cnt, price, dis):
        self.id = id
        self.name = name
        self.cnt =  cnt
        self.price = price 
        self.dis = dis
        self.total =  self.price * self.cnt - self.dis
    
    def out(self):
        print(self.id, self.name, self.cnt, self.price, self.dis, self.total)

t = int(input())
l = []
for i in range(t):
    id = input()
    name = input()
    cnt = int(input())
    price = int(input())
    dis = int(input())
    l.append(Bill(id, name, cnt, price, dis))

l.sort(key = lambda x: x.total, reverse = True)
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