import functools as f

def bonus(id, nation):
    s= 0
    if nation !='Kinh':
        s += 1.5
    if id ==1:
        s += 1.5
    if id == 2:
        s +=1
    return s

def cmp(o1, o2):
    if o1[2] > o2[2]:
        return -1
    elif o1[2] == o2[2]:
        if o1[0] < o2[0]:
            return -1
        elif o1[0] > o2[0]:
            return 1
        else:
            return 0
    return 1
    

t = int(input())
l=[]
for _ in range(1,t+1):
    s = input().split()
    point = float(input())
    nation = input()
    area = int(input())

    name =''
    for i in s:
        name += i.strip().title() + ' '
    name = name.rstrip()
    status ='Truot'
    point += bonus(area, nation)
    if point >= 20.5: status= 'Do'
    id = str(_)
    while len(id) <2:
        id = '0'+id
    id = 'TS' +id
    tmp=[id, name, point, status]
    l.append(tmp)
l.sort(key = f.cmp_to_key(cmp))
for i in l:
    print('%s %s %.1f %s' %(i[0], i[1], i[2], i[3]))
"""
2
Nguyen   hong ngat
22
Kinh
1
  Chu thi MINh
14
Dao
3

2
Nguyen   hong ngat
22
Kinh
1
Nguyen   hong ngat
22
Kinh
1
"""
