import functools as f 

def cmp(o1, o2):
    if(o1.p2 < o2.p2):
        return -1
    return 1
class pair:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def out(self):
        print(self.p1, self.p2)
t = int(input())
for _ in range(t):
    n = int(input())
    l=[]
    for i in range(n):
        p1, p2 = map(int, input().split())
        l.append(pair(p1, p2))
    l.sort(key = f.cmp_to_key(cmp))
    cnt =1
    p = l[0]
    for i in range(1, len(l)):
        if l[i].p1 > p.p2:
            cnt +=1
            p = l[i]
    print(cnt)
    # for i in l:
    #     i.out()
"""
1
10
39 55
37 74
0 1
19 25
65 76
51 52
19 21
5 94
46 65
32 40
"""