from math import*

t= int(input())
l=[]
for _ in range(t):
    s= input()
    s.strip()
    if s not in l:
        l.append(s)
print(len(l))
"""
4
CHUC MUNG NAM MOI
HAPPY NEW YEAR
CHUC MUNG TUOI MOI
CHUC MUNG NAM MOI
"""