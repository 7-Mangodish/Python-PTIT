import functools as f 

def cmp (o1, o2):
    t1 = [int(x) for x in o1.time.split('/')]
    t2 = [int(x) for x in o2.time.split('/')]
    if t1[2] < t2[2]:
        return -1
    elif t1[2] == t2[2]:
        if t1[1] < t2[1]:
            return -1
        elif t1[1] == t2[1]:
            if t1[0] < t2[0]:
                return -1
            elif t1[0] == t2[0]:
                if o1.name < o2.name:
                    return -1
                elif o1.name == o2.name:
                    return o1.cnt > o2.cnt 
    return 1
    # if o1.time < o2.time:
    #     return -1
    # elif o1.time == o2.time:
    #     if o1.name < o2.name:
    #         return -1
    #     elif o1.name == o2.name:
    #         return o1.cnt > o2.cnt
    # return 1


class Film:
    def __init__(self, id, tl, time, name, cnt):
        self.id = id
        self.tl = tl 
        self.time = time
        self.name = name
        self.cnt = cnt

    def out(self):
        print(self.id, self.tl, self.time, self.name, self.cnt)

n, m = map(int, input().split())
tl = dict()
for i in range(n):
    s = input()
    id = f'TL%03d'%(i+1)
    tl[id] = s

l=[]
for i in range(m):
    t = input()
    form = ''
    time = input()
    name = input()
    cnt = int(input())
    for j in tl.keys():
        if t == j:
            form = tl.get(j)
            break
    l.append( Film(f'P%03d'%(i+1), form, time, name, cnt))

l.sort(key = f.cmp_to_key(cmp))
for i in l:
    i.out()

"""
2 3
Hai huoc
Tinh cam
TL001
25/11/2021
Phim so 1
10
TL001
04/12/2021
Phim so 2
15
TL002
25/11/2021
Phim so 3
5
"""