import functools as f

def cmp(o1, o2):
    if o1.hour > o2.hour:
        return -1
    elif o1.hour == o2.hour:
        return o1.minute < o2.minute
    return 1


class Time:
    def __init__(self, id, name, hour, minute):
        self.id = id
        self.name = name
        self.hour = hour
        self.minute = minute

    def out(self):
        print(self.id, self.name, self.hour,'gio', self.minute,'phut')

t = int(input())
l=[]
for _ in range(t):
    id = input()
    name = input()

    w1 = input().split(':')
    h1 = int(w1[0])
    m1 = int(w1[1])

    w2 = input().split(':')
    h2 = int(w2[0])
    m2 = int(w2[1])

    minute = (h2-h1)*60 + m2-m1
    # print(minute)
    h = minute // 60
    minute %= 60
    l.append(Time(id, name, h, minute))
l.sort(key = f.cmp_to_key(cmp))
for i in l:
    i.out()

"""
3
01T
Nguyen Van An
09:00
10:30
06T
Hoang Van Nam
15:30
18:00
02I
Tran Hoa Binh
09:05
10:00
"""