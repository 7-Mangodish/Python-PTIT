import functools as ft
import math as m
class hd:
    def __init__(self, id, name, num):
        self.id = id
        self.name = name
        self.num = num
    def fee(self):
        sum=0
        day = self.num
        if self.num <=50:
            sum = 100*self.num
            sum += sum * 0.02
        elif self.num >=51 and self.num<= 100:
            sum = 100*50 + (self.num - 50)*150
            sum += sum *0.03
        else:
            sum = 100*50 + 50*150 + (self.num - 100)*200
            sum += sum * 0.05
        return sum


def cmp( a, b):
    if a.fee() > b.fee():
        return -1
    return 1

l =[]
n = int(input())
for _ in range(n):
    id = 'KH%02d'%(_+1)
    name = input()
    before = int(input())
    after = int(input())
    tmp = hd(id, name, after-before)
    l.append(tmp)

l = sorted(l, key=ft.cmp_to_key(cmp))
for i in range(len(l)):
    print(l[i].id, l[i].name, round(l[i].fee())) 
"""
3
Le Thi Thanh
468
500
Le Duc Cong
160
230
Ha Hue Anh
410
612
"""