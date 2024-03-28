n, m= map(int, input().split())
s1= set(int(x) for x in input().split())
s2= set(int(x) for x in input().split())
# Giao cua 2 tap hop: &
a= list(s1 & s2)
# s1- s2: phan tu chi co trong s1 va ngc lai
b= list(s1 - s2)
c= list(s2 - s1)
a.sort(); b.sort(); c.sort()
for i in a:
    print(i, end=' ')
print()
for i in b:
    print(i, end=' ')
print()
for i in c:
    print(i, end=' ')
"""
5 6
1 2 3 4 5
3 4 5 6 7 8
"""