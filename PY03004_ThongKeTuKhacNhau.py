import re
import functools as f

def cmp(o1, o2):
    if o1[1] > o2[1]:
        return -1
    elif o1[1] == o2[1]:
        if o1[0] < o2[0]:
            return -1
    return 1

t = int(input())
w=[]
pat = '[\,\.\?\!\;\:\(\)\-\/\s]'
for i in range(t):
    ar =  re.split(pat, input().lower())
    for j in ar:
        if j != '':
            w.append(j)

d = dict()
for i in w:
    if i not in d.keys():
        d[i] = 1
    else:
        d[i] = d[i] + 1

d = sorted(d.items(), key = f.cmp_to_key(cmp))
for i in d:
    print(i[0], i[1])
"""
3
(PTIT duy tri )hoc phi on dinh nam 2019 va khong tang trong nam 2020-2021 va 2021-2022!
Khi dich benh xuat hien PTIT trich hon 6 ty dong ho tro sinh vien PTIT
voi muc ho tro 500000 dong/sinh vien PTIT.

ptit 4
2021 2
dong 2
ho 2
nam 2
sinh 2
tro 2
va 2
vien 2
2019 1
2020 1
2022 1
500000 1
6 1
benh 1
dich 1
dinh 1
duy 1
hien 1
hoc 1
hon 1
khi 1
khong 1
muc 1
on 1
phi 1
tang 1
tri 1
trich 1
trong 1
ty 1
voi 1
xuat 1
"""