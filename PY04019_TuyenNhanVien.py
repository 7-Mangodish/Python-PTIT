import functools as f

def cmp(o1, o2):
    if o1.p > o2.p:
        return -1
    return 1

class NV:
    def __init__(self, id, name, p1, p2):
        self.id = id
        self.name = name
        self.p = (p1+p2)/2
        self.status =""
        self.setStatus()

    def setStatus(self):
        if self.p < 5:
            self.status = "TRUOT"
        elif self.p < 8:
            self.status = "CAN NHAC"    
        elif self.p <=9.5:
            self.status = "DAT"
        else:
            self.status = "XUAT SAC"

    def out(self):
        print(self.id, self.name, '%.2f'%self.p, self.status)
    
t = int(input())
l=[]
for _ in range(t):
    id = 'TS0%01d'%(_+1)
    name = input()
    p1 = float(input())

    if p1 >10:
        p1/=10
    p2 = float(input())
    if p2 >10:
        p2/=10
    l.append(NV(id, name, p1, p2))

l.sort(key = f.cmp_to_key(cmp))
for i in l:
    i.out()

"""
10
Nguyen Thai Binh
45
75
Le Cong Hoa
4
4.5
Phan Van Duc
56
56
Nguyen Thai Binh
45
75
Le Cong Hoa
4
4.5
Phan Van Duc
56
56
Nguyen Thai Binh
45
75
Le Cong Hoa
4
4.5
Phan Van Duc
56
56
Phan Van Duc
56
60
"""

    