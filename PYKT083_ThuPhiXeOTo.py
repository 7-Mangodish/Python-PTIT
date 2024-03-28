
def Fee(name, cnt):
    if name=='Xe_con':
        if cnt==5:
            return 10000
        else:
            return 15000
    elif name=='Xe_tai':
        return 20000
    else:
        if cnt==29:
            return 50000
        else:
            return 70000

if __name__ =='__main__':
    t= int(input())
    s=0
    day={}
    for _ in range(t):
        l=[x for x in input().split()]
        if l[3]== 'IN':
            if l[4] not in day.keys():
                s=0
            s+= Fee(l[1], int(l[2]))
            day[l[4]]=s

    for k, v in day.items():
        print(k,':',sep='', end=' ')
        print(v)

"""
5
30F-123.15 Xe_con 5 OUT 06/11/2021
30F-123.15 Xe_con 5 IN 06/11/2021
30H-123.15 Xe_con 7 IN 06/11/2021
29H-222.68 Xe_tai 2 IN 07/11/2021
30G-511.15 Xe_con 5 IN 07/11/2021
"""

