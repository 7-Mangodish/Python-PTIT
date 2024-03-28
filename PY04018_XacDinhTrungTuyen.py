

class Candicate:
    def __init__(self, id, name, extraId, p1, p2 ):
        self.id = id
        self.name = name
        self.extraId = extraId
        self.p1 = p1
        self.p2 = p2
        self.sub =''
        self.total = 0
        self.status = ''

        self.setSub()
        self.setTotal()
        self.setStatus()
    
    def setSub(self):
        if self.extraId.startswith('A'):
            self.sub = 'TOAN'
        if self.extraId.startswith('B'):
            self.sub = 'LY'      
        if self.extraId.startswith('C'):
            self.sub = 'HOA' 

    def setTotal(self):   
        bonus = 0
        if self.extraId.endswith('1'):
            bonus = 2          
        if self.extraId.endswith('2'):
            bonus = 1.5        
        if self.extraId.endswith('3'):
            bonus = 1             
        if self.extraId.endswith('4'):
            bonus = 0    
        self.total = self.p1 *2 + self.p2 + bonus

    def setStatus(self):
        if self.total >= 18:
            self.status = 'TRUNG TUYEN'
        else:
            self.status = 'LOAI'
    
    def out(self):
        print(self.id, self.name, self.sub, self.total, self.status)

t = int(input())
l=[]
for i in range(t):
    name = input()
    extraId = input()
    p1 = float(input())
    p2 = float(input())
    id = f'GV%02d'%(i+1)
    l.append(Candicate(id, name, extraId, p1, p2))

l.sort(key= lambda x: x.total, reverse = True)
for i in l:
    i.out()

"""
3
Le Van Binh
A1
7.0
3.0
Tran Van Toan
B3
4.0
7.0
Hoang Thi Tam
C2
7.0
6.0
"""