
room = {}

def unit(gr, year):
    if year >=1 and year <=3:
        if gr =='A' : return 10
        elif gr == 'B' : return 10
        elif gr == 'C' : return 9
        else: return 8
    elif year >=4 and year <=8:
        if gr =='A' : return 12
        elif gr == 'B' : return 11
        elif gr == 'C' : return 10
        else: return 9
    elif year >=9 and year <=15:
        if gr =='A' : return 14
        elif gr == 'B' : return 13
        elif gr == 'C' : return 12
        else: return 11
    else:
        if gr =='A' : return 20
        elif gr == 'B' : return 16
        elif gr == 'C' : return 14
        else: return 13

t = int(input())
for _ in range(t):
    s = input().split()
    id = s[0]
    name = ''
    for i in range(1, len(s)):
        name += s[i] +' '
    name = name.rstrip()
    room[id] = name

n= int(input())
for _ in range(n):
    id_emp = input()
    name = input()
    salary = int(input())
    day = int(input())

    gr = id_emp[0]
    year = int(id_emp[1:3])
    id_room = id_emp[-2:]
    month_salary = unit(gr, year) * salary * day * 1000
    print(id_emp, name, room[id_room], month_salary)

"""
2
HC Hanh chinh
KH Ke hoach Dau tu
2
C06HC
Tran Binh Minh
65
25
D03KH
Le Hoa Binh
59
24
"""