import functools as f

def cmp(o1, o2):
    if o1.fee > o2.fee:
        return -1
    return 1

class HoaDon:
    def __init__(self, id, name, cnt):
        self.id = id
        self.name = name
        self.cnt = cnt
        self.fee =0
        self.setFee()
    
    def setFee(self):
        if self.cnt <= 50:
            self.fee = (self.cnt *100)*1.02
        elif self.cnt>50 and self.cnt <=100 :
            self.fee = (50*100 + (self.cnt-50)*150)*1.03
        else:
            self.fee = (50*100 + 50*150 + (self.cnt - 100)*200)*1.05
        self.fee = round(self.fee)
    
    def out(self):
        print(self.id , self.name, self.fee)
    
t = int(input())
l=[]
for _ in range(t):
    name = input()
    t1 = int(input())
    t2 = int(input())
    x = HoaDon('KH%02d'%(_+1), name, t2-t1)
    l.append(x)

l.sort(key = f.cmp_to_key(cmp))
for i in l:
    i.out()
"""
3
Le Thi Thanh
468
500
Le Duc Cong
160
230
Ha Hue Anh
410
612
"""