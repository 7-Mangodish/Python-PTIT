
class Student:
    def __init__(self, id, name, cl):
        self.id = id
        self.name = name
        self.cl = cl
        self.point = 10
        self.status = ''
    
    def setPoint(self, p):
        self.point += p

    def setStatus(self):
        if self.point <=0:
            self.point = 0
            self.status = 'KDDK'
    
    def out(self):
        self.setStatus()
        print(self.id, self.name, self.cl, self.point, self.status)

t = int(input())
l = []
for i in range(t):
    id = input()
    name = input()
    cl = input()
    l.append(Student(id, name, cl))
for i in range(t):
    id, s = map(str, input().split())
    for j in l:
        if j.id == id:
            for k in s:
                if k =='v':
                    j.setPoint(-2)
                if k =='m':
                    j.setPoint(-1)
            break

for i in l:
    i.out()
"""
3
B19DCCN999
Le Cong Minh
D19CQAT02-B
B19DCCN998
Tran Truong Giang
D19CQAT02-B
B19DCCN997
Nguyen Tuan Anh
D19CQCN04-B
B19DCCN998 xxxmxmmvmx
B19DCCN997 xmxmxxxvxx
B19DCCN999 xvxmxmmvvm
"""