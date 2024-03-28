import functools as ft
def cmp (a, b):
    m,n= a[1], b[1]
    y1, m1, d1= m[-4:], m[-7:-5], m[:2]
    y2, m2, d2= n[-4:], n[-7:-5], n[:2]
    if y1 >y2 : return 1
    elif y1<y2: return -1
    else:
        if m1 > m2: return 1
        elif m1 < m2: return -1
        else:
            if d1 > d2: return 1
            elif d1 < d2: return -1
            else:
                    t1= a[2]; t2= b[2]
                    if t1 > t2:
                        return 1
                    elif t1 < t2:
                        return -1
                    else:
                        id1 =a[0]; id2= b[0]
                        if id1 >id2: return 1
                        else:
                            return -1
with open('CATHI.in') as f:
    l= f.readlines()
a=[]
k=1
ind=1
while ind <len(l):
    tmp=[]
    for i in range(3):
        tmp.append(l[ind+i].rstrip())
    id= str(k)
    while len(id)<3:
        id= '0' +id
    id= 'C'+id
    tmp.insert(0,id)
    a.append(tmp)
    k+=1
    ind+=3
a.sort(key= ft.cmp_to_key(cmp))
for i in a:
    for j in i:
        print(j, end=' ')
    print()
