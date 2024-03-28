from datetime import datetime

class Cust:
    def __init__(self, id, name, room, time, bonus):
        self.id = id 
        self.name = name 
        self.room = room
        self.time = time
        self.bonus = bonus
        self.setTotal()
        self.total += self.bonus
    
    def setTotal(self):
        if self.room.startswith('1'):
            self.total = self.time * 25
        if self.room.startswith('2'):
            self.total = self.time * 34        
        if self.room.startswith('3'):
            self.total = self.time * 50
        if self.room.startswith('4'):
            self.total = self.time * 80     

    def out(self):
        print(self.id, self.name, self.room, self.time, self.total)

t = int(input())
l=[]
for i in range(t):
    id = f'KH%02d'%(i+1)
    name = input().strip()
    room = input().strip()
    s1 = input().strip()
    s2 = input().strip()
    begin = datetime.strptime(s1, "%d/%m/%Y")
    end = datetime.strptime(s2, "%d/%m/%Y")
    time = end - begin
    bonus = int(input())
    l.append(Cust(id, name, room, time.days+1, bonus))

l = sorted(l, key = lambda x: x.total, reverse=True)
for i in l:
    i.out()

"""
3
Huynh Van Thanh
103 
05/06/2010
05/06/2010
15
Le Duc Cong
106 
08/03/2010
01/05/2010
220
Tran Thi Bich Tuyen
207
10/04/2010
21/04/2010
96
"""

