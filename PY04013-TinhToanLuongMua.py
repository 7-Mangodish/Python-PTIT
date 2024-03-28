
def toMinute(s):
    w = [int(x) for x in s.split(':')]
    return w[0] * 60 + w[1]

class Rain:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.cnt = 0
        self.totalTime = 0
    
    def setTotalTime(self, n):
        self.totalTime +=n
    
    def setCnt(self, n):
        self.cnt += n
    
    def out(self):
        hour = self.totalTime /60
        ave = self.cnt / hour
        print(f'%s %s %.2f'%(self.id, self.name, ave))

t = int(input())
l = []
ind =0
for _ in range(t):
    name = input()
    begin = input()
    end = input()
    cnt = int(input())

    t1 = toMinute(begin)
    t2 = toMinute(end)
    ok= False

    for i in l:
        if(i.name == name):
            i.setTotalTime(t2-t1)
            i.setCnt(cnt)
            ok = True
            break

    if(ok == False):
        ind+=1
        x = Rain((f'T%02d'%ind),name)
        x.setTotalTime(t2-t1)
        x.setCnt(cnt)
        l.append(x)

for i in l:
    i.out()
"""
10
Dong Anh
07:30
08:00
60
Cau Giay
07:45
08:12
50
Soc Son
08:00
09:15
78
Dong Anh
18:50
20:00
88
Cau Giay
19:01
20:00
77
Soc Son
19:06
20:21
66
Dong Anh
21:00
21:40
49
Cau Giay
21:50
22:20
68
Dong Anh
22:15
23:45
30
Cau Giay
22:50
23:45
35
"""

    

