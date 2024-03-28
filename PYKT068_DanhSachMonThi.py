
class  sub:
    def __init__(self, id, name, form):
        self.id = id
        self.name = name
        self.form = form
    
    def out(self):
        print(self.id, self.name, self.form)

t = int(input())
l=[]
for i in range(t):
    id = input()
    name = input()
    form = input()
    l.append(sub(id, name, form))

l.sort(key = lambda x: x.id)

for i in l:
    i.out()
"""
2
MUL1320
Nhap mon da phuong tien
Bai tap lon + Van dap truc tuyen
BAS1203
Giai tich 1
Thi viet + Van dap truc tuyen
"""
