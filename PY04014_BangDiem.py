import functools as f

def cmp(o1, o2):
    if o1.point > o2.point:
        return -1
    elif o1.point == o2.point:
        return o1.id < o2.id
    return 1

class Point :
    def __init__(self, id, name, point):
        self.id = id 
        self.name = name
        self.point = point
        self.status =''
    
    def setStatus(self):
        if self.point >=9:
            self.status = 'XUAT SAC'
        elif self.point >=8 and self.point <9:
            self.status = 'GIOI'
        elif self.point >=7 and self.point <8:
            self.status = 'KHA'      
        elif self.point >=5 and self.point <7:
            self.status = 'TB'
        else:
            self.status = 'YEU'
    
    def out(self):
        self.setStatus()
        print(self.id, self.name, '%.1f'%self.point, self.status)

l=[]
t = int(input())
for _ in range(t):
    name = input()
    p = [float(x) for x in input().split()]
    ave =0
    ave +=(p[0]*2 + p[1]*2)
    for i in range(2, len(p)):
        ave += p[i]
    ave /=12
    ave = round(ave * 10.0 / 10.0, 1)
    x = Point('HS%02d'%(_+1), name, ave)
    # print(name ,ave)
    l.append(x)

l.sort(key=f.cmp_to_key(cmp))
for i in l:
    i.out()

"""
4
Luu Thuy Nhi
9.3  9.0  7.1  6.5  6.2  6.0  8.2  6.7  4.8  5.5
Le Van Tam
8.0  8.0  5.5  9.0  6.8  9.0  7.2  8.3  7.2  6.8
Le Van Tam
9.0  6.4  6.0  7.5  6.7  5.5  5.0  6.0  6.0  6.0
Nguyen Thai Binh
9.0  6.4  6.0  7.5  6.7  5.5  5.0  6.0  6.0  6.0
"""