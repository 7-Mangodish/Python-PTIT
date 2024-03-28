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
w= ' '
pat = '[a-zA-z]+'
for i in range(t):
    w += input().lower() + ' '
l = re.findall(pat, w)
# print(l)

d = dict()
for i in l:
    if i not in d.keys():
        d[i] = 1
    else:
        d[i] = d[i] +1


d = sorted(d.items(), key = f.cmp_to_key(cmp))
for i in d:
    print(i[0], i[1])

"""
3
(PTIT duy tri000 )hoc phi on dinh nam 2019 va khong tang trong nam 2020-2021 va 2021-2022!
Khi dich benh xuat hien PTIT trich hon 6 ty dong ho tro sinh vien PTIT
voi muc ho tro 500000 dong/sinh vien PTIT.
"""